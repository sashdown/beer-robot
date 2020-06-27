"""
Cycle socket on and off to verify it is working
"""
from time import sleep

from temperature import initialise_temperature_probe
import initialise_logging

initialise_temperature_probe()
from actions import switch_on_boiler, switch_off_boiler

while True:

    switch_on_boiler()
    sleep(1)
    switch_off_boiler()