import os
import csv
import requests
from bs4 import BeautifulSoup
from datetime import datetime   

# ===========================================
# variables for the connection to the site
# ===========================================
url="https://quotes.toscrape.com/"

# timestamp=datetime.now()

# ===========================================
# connetcing and Fetching data 
# ===========================================
def fetch_data():
    response=None
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("connection completed")
            log("Connection Completed")

            # data = response.json()
    except requests.exceptions.ConnectionError:
        print("Connection Failed")
        log("Connection Failed")

    return response

# ===========================================
# function for logging records
# 1. check the directory if exists then ignore the command and moves to new line otherwise create a new file
# ============================================
def log(message):
    # os.makedirs("records",exist_ok=True)
    print(f"{datetime.now()} : {message}")
    try:
        with open("file.csv","a",newline='') as file:
            writer = csv.writer(file)
            writer.writerow([f"{datetime.now()} : {message}"])
    except FileNotFoundError:
        print("File Not Found")
        # log("file not found")

# ===========================================
# reads all the files 
# ===========================================
def fetch_all():
    try:
        with open("file.csv","r",newline='') as file:
            reader= csv.reader(file)
            for line in reader:
                print(line)
        log("read mode for file")
    except FileNotFoundError:
        print("File not Found")
        log("File not found")

# 
# Checks that file exists or not is exists then compare with new html file 
# if not exists then create a new file 
# 
def save_data():
    os.makedirs("files",exist_ok=True)
    response=None
    response=fetch_data()
    if response != None:
        soup=BeautifulSoup(response.text,"html.parser")
        qoutes=soup.find_all("div",class_="quote")
        text=soup.find_all("span",class_="text")
        author=soup.find_all("small",class_="author")
        try:
            if os.path.exists("files/old_data.csv"):
                with open("files/new_data.csv","w",newline="",encoding="utf-8") as file:
                    writer=csv.writer(file)
                    writer.writerow(["Author", "Quote"]) # Header
                    for quote in qoutes:
                        q_text = quote.find("span", class_="text").text
                        q_author = quote.find("small", class_="author").text
                        writer.writerow([q_author, q_text])

            else:
                with open("files/old_data.csv",'w',newline="",encoding="utf-8")as file:
                    writer=csv.writer(file)
                    writer.writerow(["Author", "Quote"]) # Header
                    for quote in qoutes:
                        q_text = quote.find("span", class_="text").text
                        q_author = quote.find("small", class_="author").text
                        writer.writerow([q_author, q_text])
        except FileNotFoundError:
            print("File Not Found")
            log("File Not Found")

save_data()