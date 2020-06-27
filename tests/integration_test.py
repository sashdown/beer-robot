
import logging
logging.basicConfig(level=logging.DEBUG)

from temperature import read_temp, initialise_temperature_probe
from actions import message, raise_temperature_for, action

initialise_temperature_probe()

action("Confirm Start")

message("Boiling for 1 minute")

exit(0)
raise_temperature_for(target_temperature=95, target_minutes=1)

message("Reached {}".format(read_temp()))