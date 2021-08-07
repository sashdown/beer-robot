1)Connect to Pi

hostname raspberrypi
user: pi
password: pi

2)
cd workspace
. venv/bin/activate
sudo python scripts/monitor_temperature.py # (will fail but seems to initialise something)
export PYTHONPATH=.
python scripts/monitor_temperature.py

On pi,
cd workspace/venv
first activate venv (. venv/bin/activate)
then run sudo workspace/monitor_temperature.py

ip address 192.168.0.33


login pi/pi

export PYTHONPATH=~/workspace
python scripts/monitor_temperature.py - failed with error below
sudo python scripts/monitor_temperature.py - failed because su didn't inherit venv
 ls /sys/bus/w1/devices

python scripts/monitor_temperature.py -- worked

Got following error, but then  worked ok, no sudo required.
  File "/home/pi/workspace/temperature.py", line 18, in get_temperature_device_file
    device_folder = glob.glob(base_dir + '28*')[0]
IndexError: list index out of range
