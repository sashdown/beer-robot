import logging
from time import sleep

from temperature import read_temp
from tidy_pump import manage

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S')

from actions import message, wait_until_temperature_has_fallen_to, switch_off_boiler, create_pump

MAX_TEMPERATURE = 20
MIN_TEMPERATURE = 19.8

CYCLE_MINUTES = 10

with manage(create_pump()) as pump:
    message("Cooling initiated : target temp {}C".format(MAX_TEMPERATURE))

    try:
        while (True):
            switch_off_boiler()
            if (read_temp() > MAX_TEMPERATURE):
                message('Cooling.  temp {} : target {}'.format(read_temp(), MIN_TEMPERATURE))

                wait_until_temperature_has_fallen_to(MIN_TEMPERATURE, pump=pump)

                message(
                    "Target Temperature ( {}C ) reached.  Current temperature {}".format(MIN_TEMPERATURE, read_temp()))
            logging.debug('Waiting {} mins : temp {} C : max {}'.format(CYCLE_MINUTES, read_temp(), MAX_TEMPERATURE))
            sleep(CYCLE_MINUTES * 60)
    except Exception as e:
        message("Error received.  Exiting {}".format(e))
