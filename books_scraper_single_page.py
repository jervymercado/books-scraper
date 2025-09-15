# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL for the first page of the site
url = "http://books.toscrape.com/"

# Send an HTTP GET request to the page
page = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")

# Find all book entries (each one is inside an <article> tag with class 'product_pod')
books = soup.find_all("article", class_="product_pod")

# Initialize an empty list to store extracted book data
data = []

# Loop through each book found on the page
for book in books:
    # Extract the book title (text inside the <a> tag under <h3>)
    title = book.find("h3").find("a").text

    # Extract the book price
    price = book.find("p", class_="price_color").text

    # Extract the book rating from the class name (e.g., 'One', 'Two', etc.)
    rating_tag = book.find("p", class_="star-rating")
    rating = rating_tag.get("class")[1]

    # Create a dictionary with the data and add it to the list
    book_data = {
        "Title": title,
        "Price": price,
        "Rating": rating
    }
    data.append(book_data)

# Convert the list of book data into a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file (without the index)
df.to_csv("books_page1.csv", index=False)
