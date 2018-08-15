
import logging
logging.basicConfig(level=logging.DEBUG)

from temperature import read_temp, init
from actions import message, raise_temperature_for, manual_action

init()

manual_action("Confirm Start")

message("Boiling for 1 minute")

exit(0)
raise_temperature_for(target_temperature=95, target_minutes=1)

message("Reached {}".format(read_temp()))