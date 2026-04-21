import os
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
        log("Fetch Completed")
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
    try:
        with open("data/old.html","r",encoding="utf-8") as file:
            log("read mode for file")
            return file.read()
            
    except FileNotFoundError:
        print("File not Found")
        log("File not found")
        return None 

# =========================================================================
# Checks that file exists or not is exists then compare with new html file 
# if not exists then create a new file 
# =========================================================================

def save_data(content):
    os.makedirs("data",exist_ok=True)
   
    try:
        with open("data/old.html","w",encoding="utf-8") as file:                  
            file.write(content)
            log("data written in file")
            print("data written in file")
                
    except FileNotFoundError:
        print("File Not Found")
        log("File Not Found")


def main():
    log("Run Started")

    new_data = fetch_data()
    old_data = load_old_data()
    if new_data == None:
        log("Cannot Run")
    elif old_data==None:
        log("First Run")
        save_data(new_data)
    elif old_data == new_data:
        log("no change")
    else:
        log("Updated")
        save_data(new_data)
    log("Run Completed")

main()
