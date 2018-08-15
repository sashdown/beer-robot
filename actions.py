import logging
from datetime import date, datetime
from time import sleep

from temperature import read_temp

MONITOR_BOILER_SWITCHOFF_DELAY = 1

ENERGENIE_SOCKET_NUMBER = 2

from gpiozero import Energenie

socket = Energenie(ENERGENIE_SOCKET_NUMBER)

def wait(minutes):
    sleep(minutes * 60)

def switch_on_boiler():

    socket.on()

    logging.debug("Boiler On")

def switch_off_boiler():
    logging.debug("Boiler Off")
    socket.off()

def raise_temperature_for(target_temperature, target_minutes=0):

    raise_temperature(target_temperature)

    logging.debug("Holding at {} for {} minutes".format(target_temperature, target_minutes))
    start = datetime.now()
    while ((datetime.now() - start).seconds < target_minutes * 60):
        logging.debug("Waiting 30 seconds before re-reading temperature")
        sleep(30)
        logging.debug("Current temperature {}C".format(read_temp()))
        raise_temperature(target_temperature)
    logging.debug("Held at {} for {} seconds ".format(target_temperature, (datetime.now() - start).seconds))

def raise_temperature(target_temperature):

    while (read_temp() < target_temperature):
        switch_on_boiler()
        logging.debug("Boiler On.  Waiting {} secs to rise to  {}. Current temp {}".format(
            MONITOR_BOILER_SWITCHOFF_DELAY,
            target_temperature, read_temp()))
        sleep(MONITOR_BOILER_SWITCHOFF_DELAY)
    switch_off_boiler()
    logging.debug("Target temperature {} reached.  Now {}C".format( target_temperature, read_temp()))


def wait_until_temperature_has_fallen_to(target_temperature):
    while (read_temp() > target_temperature):
        switch_on_boiler()
        logging.debug("Waiting to fall to {}. Current temp {}".format(target_temperature, read_temp()))
        sleep(10)
    switch_off_boiler()
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
        text="{}> {}".format(now.strftime("%H:%M:%S") , action)
    )
    print(action)

def manual_action(action):
    message("ACTION REQUIRED: {}".format(action))
    input(action)
    message("COMPLETE: {}".format(action))

# Cool / Heat to target temperature and then keep at that temperature for specified minutes
def maintain(temperature, minutes):
    pass