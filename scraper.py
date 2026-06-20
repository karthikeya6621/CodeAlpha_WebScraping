import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_books():
    url = "https://books.toscrape.com/"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    books = []

    for book in soup.find_all("article", class_="product_pod"):
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.p["class"][1]

        books.append({
            "Title": title,
            "Price": price,
            "Rating": rating
        })

    df = pd.DataFrame(books)

    # Save to Excel
    df.to_excel("books_data.xlsx", index=False)

    print("Data saved successfully to books_data.xlsx")