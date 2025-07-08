# pubmed_paper_fetcher/cli.py

import argparse
from pubmed_paper_fetcher.fetcher import fetch_papers_and_save

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers based on a query.")
    parser.add_argument("query", type=str, help="PubMed query string")
    parser.add_argument("-f", "--file", type=str, help="Filename to save results as CSV")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug logging")

    args = parser.parse_args()

    if args.debug:
        print(f"Running PubMed fetcher with query: {args.query}")
        if args.file:
            print(f"Saving results to: {args.file}")

    fetch_papers_and_save(args.query, args.file, args.debug)
