import os
import glob
import time


def initialise_temperature_probe():
  import RPi.GPIO as GPIO

  GPIO.setmode(GPIO.BCM)
  GPIO.setup(21, GPIO.OUT)
  GPIO.output(21, 1)
  os.system('modprobe w1-gpio')
  os.system('modprobe w1-therm')

def get_temperature_device_file():
    base_dir = '/sys/bus/w1/devices/'
    os.system('ls {} > /dev/null'.format(base_dir))   # Why does it need an ls - need to experiment with retry mech
    device_folder = glob.glob(base_dir + '28*')[0]
    return  device_folder + '/w1_slave'


def read_temp_raw():
    f = open(get_temperature_device_file(), 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos + 2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c


