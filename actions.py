import logging
from datetime import date, datetime
from time import sleep

from temperature import read_temp

ENERGENIE_SOCKET_NUMBER = 2


def wait(minutes):
    sleep(minutes * 60)

def switch_on_boiler():
    from gpiozero import Energenie
    socket = Energenie(ENERGENIE_SOCKET_NUMBER)
    socket.on()

    logging.debug("Boiler On")

def switch_off_boiler():
    logging.debug("Boiler Off")
    from gpiozero import Energenie
    socket = Energenie(ENERGENIE_SOCKET_NUMBER)
    socket.off()

def wait_until_temperature_has_risen_to(temperature, minutes):
    switch_on_boiler()
    while (read_temp() < temperature):
        logging.debug("Waiting to rise to  {}. Current temp {}".format(temperature, read_temp()))
        sleep(10)
    switch_off_boiler()

    logging.debug("Target temperature reached")

def wait_until_temperature_has_fallen_to(target_temperature):
    while (read_temp() > target_temperature):
        logging.debug("Waiting to fall to {}. Current temp {}".format(target_temperature, read_temp()))
        sleep(10)
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
        text="{}:{}:{}> {}".format(now.hour, now.minute, now.second, action)
    )
    print(action)

def manual_action(action):
    print(action)
    message(action)

# Cool / Heat to target temperature and then keep at that temperature for specified minutes
def maintain(temperature, minutes):
    pass