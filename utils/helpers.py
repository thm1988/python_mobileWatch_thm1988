import subprocess
import os
import csv

# KEY_EVENT
from time import sleep

KEYCODE_WAKEUP = "224"
KEYCODE_SLEEP = "223"
KEYCODE_HOME = "3"


def set_root():

    cmd = "adb root"
    sleep(2)
    os.system(cmd)


def get_serial_number():

    cmd = ['adb', 'devices', '|', 'tail -n+2', '|', 'cut -sf 1']
    return subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT) \
        .stdout.read().decode()


def get_screen_brightness():

    set_root()
    cmd = ['adb', 'shell', 'cat', '/sys/class/leds/lcd-backlight/brightness']
    return subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT).stdout.read().decode()
