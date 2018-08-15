from datetime import datetime
from time import sleep

start = datetime.now()

while ((datetime.now() -start).seconds < 3):
    sleep(1)
    print("Waiting")

print("Done")