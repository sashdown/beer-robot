import logging

import mock as mock
from pytest import fixture

logging.basicConfig(level=logging.DEBUG)

from actions import wait_until_temperature_has_fallen_to


@fixture
def pump():
    return mock.Mock()


@fixture
def temperature():
    mock_temperature = mock.Mock()
    mock_temperature.side_effect = [11, 9]
    return mock_temperature


def test_pump_remains_off_below_target_temp(temperature):
    pump_mock = mock.Mock()
    wait_until_temperature_has_fallen_to(target_temperature=20,
                                         pump=pump_mock,
                                         read_delay=0,
                                         temperature_fn=temperature)

    pump_mock.off.assert_called_once()


def test_pump_switches_on_above_target_temp(pump, temperature):
    wait_until_temperature_has_fallen_to(target_temperature=10,
                                         pump=pump,
                                         read_delay=0,
                                         temperature_fn=temperature)

    pump.off.assert_called_once()
    pump.on.assert_called_once()


def test_pump_switches_off_after_failing_to_reduce_temp_after_6_attempts(pump, temperature):
    temperature.return_value = 11
    temperature.side_effect=None

    try:
        wait_until_temperature_has_fallen_to(target_temperature=10,
                                         pump=pump,
                                         read_delay=0,
                                         temperature_fn=temperature)

        assert(False)

    except RuntimeError as e:
        pass