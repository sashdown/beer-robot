from temperature import read_temp, init
import time

init()

while True:
    print(read_temp())
    time.sleep(1)
