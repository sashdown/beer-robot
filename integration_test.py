
import logging
logging.basicConfig(level=logging.DEBUG)

from temperature import read_temp, init
from actions import switch_off_boiler, switch_on_boiler, message, wait_until_temperature_has_risen_to

init()


message("Starting")

wait_until_temperature_has_risen_to(temperature=30, minutes=0)

switch_off_boiler()

print("Boiler off")