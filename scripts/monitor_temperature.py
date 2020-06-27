from temperature import read_temp, initialise_temperature_probe
import time

initialise_temperature_probe()

while True:
    print(read_temp())
    time.sleep(1)
