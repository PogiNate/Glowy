#!/usr/bin/env python
"""

We'll light up the second arm of the PiGlow based on memory usage.
Naturally this requires the PiGlow accessory to be properly installed and configured.

"""
__author__ = 'Nate Dickson'

from time import sleep
from pyglow import PyGlow
import psutil

pg = PyGlow()


def pulse():

    """

    This will pulse the lights up to the current memory usage for every
    check of the memory usage level.

    """

    arm = [7, 8, 9, 10, 11, 12]

    try:
        while True:
            used = psutil.phymem_usage()[3]
            brightness = 70
            speed = 300
            level = 100/len(arm)
            for i in range(len(arm)):
                if used >= level * i:
                    pg.pulse(arm[i], brightness, speed)
            sleep(0.2)
    except KeyboardInterrupt:
        pg.all(0)

if __name__ == "__main__":
    pulse()
