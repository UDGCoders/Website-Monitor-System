import os
import csv
import requests
from datetime import datetime   

# ===========================================
# variables for the connection to the site
# ===========================================

url="https://quotes.toscrape.com/"


# ===========================================
# connetcing and Fetching data 
# ===========================================

def fetch_data():
    try:
        response = requests.get(url)
        response.raise_for_status()
        log("Fetch Coompleted")
        return response.text

    except:
        print("Connection Failed")
        log("Connection Failed")
        return None

# ===========================================
# function for logging records
# 1. check the directory if exists then ignore the command and moves to new line otherwise create a new file
# ============================================

def log(message):
    # os.makedirs("records",exist_ok=True)
    print(f"{datetime.now()} : {message}")
    try:
        with open("logs.txt","a",newline='') as file:
            
            file.write(f"{datetime.now()} : {message} \n")
    except FileNotFoundError:
        print("File Not Found")
        # log("file not found")

# ===========================================
# reads all the files 
# ===========================================

def load_old_data():
    log("read mode for file")
    try:
        with open("files/old.html","r",newline='',encoding="utf-8") as file:
            return file.read()
            
    except FileNotFoundError:
        print("File not Found")
        log("File not found")

# =========================================================================
# Checks that file exists or not is exists then compare with new html file 
# if not exists then create a new file 
# =========================================================================

def save_data(content):
    os.makedirs("files",exist_ok=True)
   
    try:
        if os.path.exists("files/old.html"):
            with open("files/new_data.html","w",newline="",encoding="utf-8") as file:                  
                file.write(content)
        else:
            with open("files/old.html","w",newline="",encoding="utf-8") as file:
                file.write(content)
                
    except FileNotFoundError:
        print("File Not Found")
        log("File Not Found")



new_data = fetch_data()
old_data = load_old_data()