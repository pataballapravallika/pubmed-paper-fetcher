# pubmed_paper_fetcher/fetcher.py

from typing import Optional, List, Dict
from Bio import Entrez
import pandas as pd
import re
import time

Entrez.email = "pataballapravallika@gmail.com"  # Replace with your real email

def is_non_academic(affiliation: str) -> bool:
    affiliation = affiliation.lower()
    academic_keywords = ["university", "college", "school", "institute", "hospital", "center", "centre", "clinic", "department", "faculty", "lab"]
    return not any(word in affiliation for word in academic_keywords)

def fetch_papers_and_save(query: str, filename: Optional[str] = None, debug: bool = False):
    if debug:
        print(f"[DEBUG] Querying PubMed for: {query}")

    try:
        handle = Entrez.esearch(db="pubmed", term=query, retmax=20)
        record = Entrez.read(handle)
        handle.close()
        ids = record["IdList"]

        if debug:
            print(f"[DEBUG] Found {len(ids)} articles")

        if not ids:
            print("[INFO] No papers found.")
            return

        handle = Entrez.efetch(db="pubmed", id=",".join(ids), rettype="medline", retmode="text")
        records = Entrez.read(Entrez.efetch(db="pubmed", id=ids, rettype="xml", retmode="xml"))
        handle.close()

        rows = []

        for article in records["PubmedArticle"]:
            try:
                pmid = article["MedlineCitation"]["PMID"]
                title = article["MedlineCitation"]["Article"]["ArticleTitle"]
                pub_date = article["MedlineCitation"]["Article"]["Journal"]["JournalIssue"]["PubDate"]
                pub_date_str = pub_date.get("Year", "") + "-" + pub_date.get("Month", "01") + "-01"

                authors = article["MedlineCitation"]["Article"].get("AuthorList", [])
                non_acad_authors = []
                company_affiliations = []
                corr_email = None

                for author in authors:
                    aff = author.get("AffiliationInfo", [])
                    if aff:
                        aff_text = aff[0].get("Affiliation", "")
                        email_match = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", aff_text)
                        if email_match and not corr_email:
                            corr_email = email_match.group()
                        if is_non_academic(aff_text):
                            full_name = author.get("ForeName", "") + " " + author.get("LastName", "")
                            non_acad_authors.append(full_name.strip())
                            company_affiliations.append(aff_text)

                if non_acad_authors:
                    rows.append({
                        "PubmedID": pmid,
                        "Title": title,
                        "Publication Date": pub_date_str,
                        "Non-academic Author(s)": "; ".join(non_acad_authors),
                        "Company Affiliation(s)": "; ".join(company_affiliations),
                        "Corresponding Author Email": corr_email or "Not found"
                    })

            except Exception as e:
                if debug:
                    print(f"[WARNING] Skipped a paper due to error: {e}")
                continue

            time.sleep(0.3)  # Respect NCBI rate limits

        if not rows:
            print("[INFO] No papers with non-academic authors found.")
            return

        df = pd.DataFrame(rows)

        if filename:
            df.to_csv(filename, index=False)
            print(f"[INFO] Saved {len(df)} result(s) to {filename}")
        else:
            print(df)

    except Exception as e:
        print(f"[ERROR] Failed to fetch papers: {e}")
