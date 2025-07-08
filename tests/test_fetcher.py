import pytest
from pubmed_paper_fetcher.fetcher import is_non_academic, fetch_papers_and_save
import os

def test_is_non_academic():
    assert is_non_academic("Pfizer Inc., New York") == True
    assert is_non_academic("University of California, Berkeley") == False
    assert is_non_academic("Novartis AG, Switzerland") == True
    assert is_non_academic("Massachusetts General Hospital") == False

def test_fetch_papers_and_save(tmp_path):
    query = "Pfizer 2023"
    output_file = tmp_path / "test_results.csv"

    # Should not throw an exception
    fetch_papers_and_save(query, filename=str(output_file), debug=True)

    assert output_file.exists()
    content = output_file.read_text()
    assert "PubmedID" in content  # header
