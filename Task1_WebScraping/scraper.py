import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Mapping textual ratings to numeric integers
RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

def scrape_catalog(max_pages=50):
    records = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    print(f"Starting web scraper across {max_pages} pages...")

    for page in range(1, max_pages + 1):
        target_url = BASE_URL.format(page)
        response = requests.get(target_url, headers=headers)

        if response.status_code != 200:
            print(f"[Page {page}] Status {response.status_code}. Terminating pagination.")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        products = soup.find_all("article", class_="product_pod")

        for item in products:
            # 1. Title Extraction
            title = item.h3.a["title"].strip()

            # 2. Price Extraction & Numeric Cleaning
            raw_price = item.find("p", class_="price_color").text
            price = float(raw_price.replace("Â£", "").replace("£", "").strip())

            # 3. Star Rating Extraction
            rating_classes = item.find("p", class_="star-rating")["class"]
            rating_str = [c for c in rating_classes if c != "star-rating"][0]
            rating_num = RATING_MAP.get(rating_str, 0)

            # 4. Stock Availability Parsing
            raw_avail = item.find("p", class_="instock availability").text.strip()
            in_stock = "In stock" in raw_avail

            records.append({
                "Title": title,
                "Price_GBP": price,
                "Star_Rating": rating_num,
                "In_Stock": in_stock
            })

        print(f"--> Successfully extracted Page {page}/{max_pages} ({len(products)} items)")
        time.sleep(0.3)  # Respectful crawling delay

    df = pd.DataFrame(records)
    return df

def main():
    df = scrape_catalog(max_pages=50)

    # Validate output
    print("\nDataset Extraction Summary:")
    print(f"Total Rows Scraped: {len(df)}")
    print("\nFirst 5 Records:")
    print(df.head())

    print("\nDescriptive Price Statistics (£):")
    print(df["Price_GBP"].describe().round(2))

    # Export structured CSV
    output_filename = "books_scraped_dataset.csv"
    df.to_csv(output_filename, index=False)
    print(f"\n[Success] Dataset exported to '{output_filename}'.")

if __name__ == "__main__":
    main()