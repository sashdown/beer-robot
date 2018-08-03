
import logging
logging.basicConfig(level=logging.DEBUG)

from actions import wait_until_temperature_has_risen_to

def test_wait_until_temperature_has_risen_to():
    wait_until_temperature_has_risen_to(temperature=100, minutes = 0)
