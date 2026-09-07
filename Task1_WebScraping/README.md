# Task 1: Web Scraping & Automated Dataset Generation

## Project Overview
An automated web scraping pipeline built to harvest e-commerce catalog information across 50 paginated index pages (1,000 distinct items) from `books.toscrape.com`. The script navigates dynamic pagination, parses hierarchical DOM nodes using `BeautifulSoup`, cleans messy character encodings, and structures the output into an analytical CSV dataset.

## Features & Schema Extracted
* **Title:** Full book title parsed from nested DOM attributes.
* **Price_GBP:** Numerical item price cleaned of currency symbols and encoding artifacts.
* **Star_Rating:** Transformed textual DOM classes (`One` through `Five`) into ordinal numerical integers (`1`–`5`).
* **In_Stock:** Boolean status confirming inventory availability.

## Technical Architecture
* **Language:** Python
* **Web Request Engine:** `requests` (with custom User-Agent headers and throttling intervals)
* **HTML Parsing:** `BeautifulSoup4` (`html.parser`)
* **Data Processing & Validation:** `pandas`

## Summary Metrics
* **Total Records:** 1,000 items
* **Pages Scraped:** 50/50 pages
* **Average Book Price:** ~£35.07
* **Output Format:** Clean structured CSV (`books_scraped_dataset.csv`)

## Execution
```bash
python scraper.py