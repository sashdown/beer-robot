
import logging

import mock as mock



logging.basicConfig(level=logging.DEBUG)

from actions import wait_until_temperature_has_fallen_to


def test_wait_until_temperature_has_fallen_to():
    mock_temperature = mock.Mock()
    mock_temperature.return_value=1

    pump_mock = mock.Mock()
    wait_until_temperature_has_fallen_to(target_temperature=10,
                                         pump=pump_mock,
                                         read_delay=0,
                                         temperature_fn=mock_temperature)


    pump_mock.off.assert_called_once_with()