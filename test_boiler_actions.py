
import logging
logging.basicConfig(level=logging.DEBUG)

from actions import raise_temperature_for

def test_raise_temperature_for():
    raise_temperature_for(target_temperature=100, minutes = 0)
