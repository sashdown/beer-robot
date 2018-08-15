import logging
from time import sleep

from temperature import read_temp

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S')

from actions import message, wait_until_temperature_has_fallen_to, switch_off_boiler

MAX_TEMPERATURE = 21
MIN_TEMPERATURE = 20

CYCLE_MINUTES = 10

while (True):
    switch_off_boiler()
    if (read_temp() > MAX_TEMPERATURE):
        message('Cooling.  temp {} : target {}'.format(read_temp(), MIN_TEMPERATURE))

        wait_until_temperature_has_fallen_to(MIN_TEMPERATURE)

    logging.debug('Waiting {} mins : temp {} C : max {}'.format(CYCLE_MINUTES, read_temp(), MAX_TEMPERATURE))
    sleep(CYCLE_MINUTES * 60)
