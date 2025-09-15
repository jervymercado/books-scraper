# Books Scraper

This project contains two Python scripts for scraping book data from the website [BooksToScrape.com](http://books.toscrape.com/).  
It demonstrates web scraping using `requests` and `BeautifulSoup` libraries, and saving the extracted data to CSV files using `pandas`.

---

## Project Structure

- `books_scraper_single_page.py`  
  Scrapes book information (title, price, and rating) from the **first page** of BooksToScrape.com and saves it to `books_page1.csv`.

- `books_scraper_multi_page.py`  
  Scrapes book information from the **first 5 pages** of the site, combining the results into a single CSV file named `books_5pages.csv`.

---

## Features

- Extracts **Title**, **Price**, and **Rating** of each book.
- Handles multiple pages by looping through URLs.
- Saves the scraped data in CSV format, ready for analysis or use in other projects.
- Uses clean, readable Python code with comments to aid understanding.

---

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `pandas` library

You can install the required libraries with:

```bash
pip install requests beautifulsoup4 pandas
