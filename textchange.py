import os
import csv 
import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://quotes.toscrape.com/"

def fetch_page():
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except Exception as e:
        log(f"Unable to Connect: {e}")
        return None

def parse_data(html):
    soup = BeautifulSoup(html.content, 'html.parser')
    quotes = soup.find_all("div", class_="quote")  # FIXED
    return quotes

def clean_data(data):
    cleaned = []
    for item in data:  # FIXED: loop through list
        quote = item.find("span", class_="text").text.strip()
        author = item.find("small", class_="author").text.strip()
        cleaned.append([quote, author])  # consistent structure
    return cleaned

def load_old_data():
    try:
        with open("data/old.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            return list(reader)
    except FileNotFoundError:
        log("Old file not found")
        return None

def save_data(data):
    os.makedirs("data", exist_ok=True)
    try:
        with open("data/old.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Quote", "Author"])  # FIXED
            for row in data:  # FIXED
                writer.writerow(row)
    except Exception as e:
        log(f"Write failed: {e}")

def compare_data(old, new):
    return old == new

def log(message):
    os.makedirs("data", exist_ok=True)
    with open("data/logs.txt", 'a') as file:
        file.write(f"{datetime.now()} {message}\n")

def main():
    log("RUN STARTED")

    response = fetch_page()
    if not response:
        log("RUN TERMINATED")
        return

    parsed = parse_data(response)
    cleaned = clean_data(parsed)
    old = load_old_data()

    if old is None:
        log("FIRST RUN")
        save_data(cleaned)
    elif compare_data(old, cleaned):
        log("NO CHANGE")
    else:
        log("UPDATED")
        save_data(cleaned)

    log("RUN COMPLETED")

if __name__ == "__main__":
    main()