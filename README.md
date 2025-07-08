# pubmed-paper-fetcher
CLI tool to fetch PubMed papers with non-academic authors
# 🧬 PubMed Paper Fetcher

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Poetry](https://img.shields.io/badge/built%20with-poetry-cyan)](https://python-poetry.org/)

A Python CLI tool to fetch research papers from [PubMed](https://pubmed.ncbi.nlm.nih.gov/) and identify papers with **at least one author affiliated with a non-academic (e.g., pharmaceutical or biotech) company**.

---

## 📦 Features

- 🔍 Search PubMed with full query syntax
- 🏢 Detect non-academic authors based on affiliation
- 📧 Extract corresponding author's email
- 📄 Export results to a CSV file
- 🧪 Includes automated tests with `pytest`
- 📦 Poetry-powered packaging & dependency management

---

## 📁 Output Fields

| Field                      | Description                                  |
|---------------------------|----------------------------------------------|
| `PubmedID`                | Unique ID of the article                     |
| `Title`                   | Title of the paper                           |
| `Publication Date`        | Date of publication                          |
| `Non-academic Author(s)`  | Author names from companies                  |
| `Company Affiliation(s)`  | Affiliation strings with company info        |
| `Corresponding Author Email` | Extracted email from affiliation text     |

---

## 🚀 Installation

### 1. Clone the repo
```bash
         - git clone https://github.com/pataballapravallika/pubmed-paper-fetcher.git
         - cd pubmed-paper-fetcher
```
### 2. Install Poetry (if not already installed)
```bash
    pip install poetry
```
![Screenshot (333)](https://github.com/user-attachments/assets/2e057340-ae9f-43b8-9c59-671e00d7cccf)

### 3. Install dependencies
``` bash
    poetry install
```
## 🧪 Usage
``` bash
- poetry run get-papers-list "your pubmed query here" --file output.csv --debug
```
## 🔧 Options
### Flag	Description
``` bash
file / -f	File name to save CSV output
debug / -d	Enable debug logs
help / -h	Show help message
```
## 🔍 Example
``` bash 
   - poetry run get-papers-list "Pfizer OR Moderna 2023" --file results.csv --debug
```
### 🧪 Running Tests
```bash 
  poetry run pytest
```
![Screenshot (332)](https://github.com/user-attachments/assets/83a18f89-ba9b-410f-a1fa-5145ee47a6e5)

## ✅ Tests include:
- Non-academic affiliation detection logic

- Live PubMed API fetch & CSV export

## 📁 Project Structure
``` bash
- pubmed_paper_fetcher/
    ├── __init__.py
    ├── cli.py             # CLI entry point
    ├── fetcher.py         # Core logic for search + filtering
     tests/
    └── test_fetcher.py    # Pytest unit tests
    pyproject.toml         # Poetry config
    README.md              # This file
```

## 🛠 Tools Used

- 🔬 Biopython – PubMed API access via Entrez
- 📦 Poetry – Dependency & packaging
- 📊 Pandas – CSV export
- 🧪 Pytest – Testing


## 📝 License

- This project is licensed under the MIT License.
- See the LICENSE file for full details.


## 🙋‍♀️ Author
- Made with ❤️ by Pravallika Pataballa



## 💡 Contributing
- Pull requests are welcome!
- If you find bugs, want to improve heuristics, or add features — feel free to open an issue or PR.




## 🌟 Show Some Love
- If you found this project helpful:

- ⭐️ Star it
- 📣 Share it
- 🤝 Use it




## ✅ What Next?
### Would you like me to also generate:


✅ `LICENSE` file (MIT)
✅ GitHub Actions file (`.github/workflows/tests.yml`)

Just 

say: **"give me LICENSE and workflow file"**  
I'll generate them instantly!

