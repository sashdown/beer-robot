
import logging

import mock as mock
from pytest import fixture

logging.basicConfig(level=logging.DEBUG)

from actions import wait_until_temperature_has_fallen_to

@fixture
def pump():
    return mock.Mock()

def test_pump_remains_off_below_target_temp():
    mock_temperature = mock.Mock()
    mock_temperature.return_value=1

    pump_mock = mock.Mock()
    wait_until_temperature_has_fallen_to(target_temperature=10,
                                         pump=pump_mock,
                                         read_delay=0,
                                         temperature_fn=mock_temperature)


    pump_mock.off.assert_called_once_with()


def test_pump_switches_on_above_target_temp(pump):
    mock_temperature = mock.Mock()
    mock_temperature.side_effect=[11,11,9,9]

    wait_until_temperature_has_fallen_to(target_temperature=10,
                                         pump=pump,
                                         read_delay=0,
                                         temperature_fn=mock_temperature)


    pump.off.assert_called_once_with()
    pump.on.assert_called_once_with()