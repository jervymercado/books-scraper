# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Initialize an empty list to store book data from all pages
all_books = []

# Loop through the first 5 pages of the BooksToScrape website
for page_num in range(1, 6):
    # Construct the URL for each page
    url = f"http://books.toscrape.com/catalogue/page-{page_num}.html"

    # Send an HTTP GET request to the page
    page = requests.get(url)

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup (page.content, "html.parser")

    # Find all book entries on the page
    books = soup.find_all("article", class_="product_pod")

    # Loop through each book on the page
    for book in books:
        # Get the book title (text inside the <a> tag under <h3>)
        title = book.find("h3").find("a").text

        # Get the price of the book
        price = book.find("p", class_="price_color").text

        # Get the rating (as a class name like 'One', 'Two', etc.)
        rating_tag = book.find("p", class_="star-rating")
        rating = rating_tag.get("class")[1]

        # Create a dictionary with the scraped data
        book_data = {
            "Title": title,
            "Price": price,
            "Rating": rating
        }

        # Add the book data to the list
        all_books.append(book_data)

# Convert the list of book dictionaries into a DataFrame
df = pd.DataFrame(all_books)

# Save the DataFrame to a CSV file
df.to_csv("books_5pages.csv", index=False)


