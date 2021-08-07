import logging
from datetime import datetime
from time import sleep

from temperature import read_temp

MONITOR_BOILER_SWITCHOFF_DELAY = 20

# the sockets should be passed in at object creation time.
# but refactoring without a test is uncomfortable


# is there a missing TemperatureController class?
# with public methods to raise and lower the temperature
# private methods to switch on and off pump and boiler


ENERGENIE_BOILER_SOCKET_NUMBER = 2
ENERGENIE_PUMP_SOCKET_NUMBER = 2


def wait(minutes):
    sleep(minutes * 60)


def switch_on_boiler():
    from gpiozero import Energenie
    boiler_socket = Energenie(ENERGENIE_BOILER_SOCKET_NUMBER)
    boiler_socket.on()

    logging.debug("Boiler On")


def switch_on_pump():
    from gpiozero import Energenie
    pump_socket = Energenie(ENERGENIE_PUMP_SOCKET_NUMBER)
    pump_socket.on()

    logging.debug("Pump On")


def switch_off_boiler():
    from gpiozero import Energenie
    boiler_socket = Energenie(ENERGENIE_BOILER_SOCKET_NUMBER)
    boiler_socket.off()

    logging.debug("Boiler Off")


def switch_off_pump():
    pump_socket = create_pump()
    pump_socket.on()
    logging.debug("Pump Off")
    pump_socket.off()


def create_pump():
    from gpiozero import Energenie
    pump_socket = Energenie(ENERGENIE_PUMP_SOCKET_NUMBER)
    return pump_socket


def boil_for(minutes=60):

    start = datetime.now()
    while (datetime.now() - start).seconds < minutes * 60:
        switch_on_boiler()
        sleep(60)
    switch_off_boiler()


def raise_temperature_for(target_temperature, target_minutes=0):
    raise_temperature(target_temperature)

    logging.debug("Holding at {} for {} minutes".format(target_temperature, target_minutes))

    start = datetime.now()
    while (datetime.now() - start).seconds < target_minutes * 60:
        logging.debug("Waiting 30 seconds before re-reading temperature")
        sleep(30)
        logging.debug("Current temperature {}C".format(read_temp()))
        raise_temperature(target_temperature)

    logging.debug("Held at {} for {} seconds ".format(target_temperature, (datetime.now() - start).seconds))


def raise_temperature(target_temperature):
    while read_temp() < target_temperature:
        switch_on_boiler()
        logging.debug("Boiler On.  Waiting {} secs to rise to  {}. Current temp {}".format(
            MONITOR_BOILER_SWITCHOFF_DELAY,
            target_temperature, read_temp()))
        sleep(MONITOR_BOILER_SWITCHOFF_DELAY)
    switch_off_boiler()

    logging.debug("Target temperature {} reached.  Now {}C".format(target_temperature, read_temp()))


def wait_until_temperature_has_fallen_to(target_temperature,
                                         pump=None,
                                         read_delay=30,
                                         temperature_fn=read_temp):
    previous_temperature = temperature_fn()
    static_temperature_count = 0

    while previous_temperature > target_temperature:
        if (pump):
            pump.on()
        logging.debug("Waiting for measured temperature to fall to {}C. Current temp {}C".format(target_temperature,
                                                                                                 previous_temperature))
        sleep(read_delay)

        current_temperature = temperature_fn()

        if current_temperature < previous_temperature:
            static_temperature_count = 0
        else:
            static_temperature_count += 1

        if pump and static_temperature_count > 5:
            pump.off()
            raise RuntimeError("Temperature failed to drop after 5 iterations.  Current temperature {}C".format(
                current_temperature
            ))

        previous_temperature = current_temperature

    if pump:
        pump.off()
    logging.debug("Target temperature reached")


def message(action):
    from slackclient import SlackClient
    import os

    slack_token = os.environ["SLACK_API_TOKEN"]
    sc = SlackClient(slack_token)

    now = datetime.now()
    sc.api_call(
        "chat.postMessage",
        channel="updates",
        text="{}> {}".format(now.strftime("%H:%M:%S"), action)
    )
    print(action)


def action(action):
    message("ACTION REQUIRED: {}".format(action))
    input(action)
    message("COMPLETE: {}".format(action))