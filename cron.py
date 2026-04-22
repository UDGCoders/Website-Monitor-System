import os 
import datetime
import schedule
import time

print("Currtent time is", datetime.datetime.now())

def job():
    print("Running Current job",datetime.datetime.now())

schedule.every(2).seconds.do(job)
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopped by user")