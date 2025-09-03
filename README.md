# Test Tasks Project

Professional implementation of test tasks with clean code structure and organized project layout.

## Project Structure

```
test_scratch/
├── src/                    # Source code
│   └── ef_jobs_scraper.py # Main scraper script
├── tests/                  # Test files
│   └── test_regex.py      # Regex pattern testing
├── docs/                   # Documentation
│   ├── regex_patterns.md  # Regular expressions
│   ├── xpath_expressions.md # XPath expressions
│   └── sql_queries.md     # SQL queries
├── data/                   # Data output
├── requirements.txt        # Dependencies
└── README.md              # This file
```

## Tasks Completed

### ✅ Task 1: API Integration & JSON Generation
- **File**: `src/ef_jobs_scraper.py`
- **Status**: Complete and tested
- **Features**:
  - OOP architecture with `EFJobsScraper` class
  - Fetches jobs from careers.ef.com API
  - Processes and saves data to JSON
  - Clean error handling and logging

### ✅ Task 2: XPath Validation
- **File**: `docs/xpath_expressions.md`
- **Status**: Complete
- **Content**: XPath expressions for marketdino.pl website

### ✅ Task 3: SQL Queries
- **File**: `docs/sql_queries.md`
- **Status**: Complete
- **Content**: SQL queries for Job and Job_text tables

### ✅ Task 4: Regular Expressions
- **Files**: `tests/test_regex.py`, `docs/regex_patterns.md`
- **Status**: Complete and tested
- **Content**: Regex patterns for URLs, emails, bots, and parentheses

## Quick Start

### Installation
```bash
pip install -r requirements.txt
```

### Run Scraper
```bash
cd src
python ef_jobs_scraper.py
```

### Test Regex Patterns
```bash
cd tests
python test_regex.py
```

## Code Quality

- **Clean Architecture**: Organized into logical modules
- **Type Hints**: Full typing support for better code clarity
- **Error Handling**: Comprehensive exception management
- **Documentation**: Clear and concise documentation
- **Testing**: Included test files for validation

## Dependencies

- `requests` - HTTP library for API calls
- `typing-extensions` - Enhanced type hints
- `pathlib2` - Path manipulation utilities

## Output

The scraper generates `ef_jobs.json` in the `data/` folder containing processed job information from the EF careers API.
