# Deployment Guide

## Prerequisites

- Python 3.8+
- pip package manager
- Git

## Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/2DAy1/test_web_scraping.git
cd test_web_scraping
```

### 2. Create Virtual Environment
```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Project

### Run Job Scraper
```bash
cd src
python ef_jobs_scraper.py
```

### Test Regex Patterns
```bash
cd tests
python test_regex.py
```

## Project Structure

```
test_web_scraping/
├── src/                    # Source code
│   ├── __init__.py
│   └── ef_jobs_scraper.py # Main scraper
├── tests/                  # Test files
│   ├── __init__.py
│   └── test_regex.py      # Regex testing
├── docs/                   # Documentation
│   ├── deployment.md       # This file
│   ├── regex_patterns.md  # Regex patterns
│   ├── xpath_expressions.md # XPath expressions
│   └── sql_queries.md     # SQL queries
├── data/                   # Output data
├── requirements.txt        # Dependencies
├── .gitignore             # Git ignore rules
└── README.md              # Project overview
```

## Output

The scraper generates `ef_jobs.json` in the `data/` folder containing processed job information from the EF careers API.

## Troubleshooting

- Ensure virtual environment is activated
- Check Python version compatibility
- Verify all dependencies are installed
- Check internet connection for API calls
