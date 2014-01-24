#!/usr/bin/env python
"""

this module makes it possible to make a specific pattern of LEDS
light up based on CPU usage. This module will only work correctly on a
Raspberry Pi with the PiGlow accessory board correctly installed and configured.

"""

from time import sleep
from pyglow import PyGlow
import psutil

pg = PyGlow()

trail = [128, 64, 32]


def snake(auto):
    """

      Makes the lights along the CPU arm light up sequentially. The amount of time between
      runs is reduced as the cpu utilization increases.

     """

    arm = [1, 2, 3, 4, 5, 6]
    try:
        while auto:
            cpu = psutil.cpu_percent()
            delay = 1 - cpu * 0.01
            for i in range(len(arm) + 3):
                head = i
                mid = i - 1
                tail = i - 2

                for i in range(len(arm)):
                    if i == head:
                        pg.led(arm[i], trail[0])
                    elif i == mid:
                        pg.led(arm[i], trail[1])
                    elif i == tail:
                        pg.led(arm[i], trail[2])
                    else:
                        pg.led(arm[i], 0)
                    sleep(0.01)
            sleep(delay)
    except KeyboardInterrupt:
        pg.all(0)


def equalizer(auto):
    """

      Lights from the center outward, illuminating more lights as the CPU usage increases.

    """
    leds = [6, 5, 4, 3, 2, 1]
    try:
        while True:
            level = 100 / len(leds)
            cpu = psutil.cpu_percent()
            brightness = 70

            for i in range(len(leds)):
                if (cpu >= level * i):
                    pg.led(leds[i], brightness)
                else:
                    pg.led(leds[i], 0)
            sleep(0.2)

    except KeyboardInterrupt:
        pg.all(0)


if __name__ == "__main__":
    #equalizer(auto=True)
    snake(auto=True)
