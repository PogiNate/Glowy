#!/usr/bin/env python
"""

this module makes it possible to make a specific pattern of LEDS
light up based on CPU usage. This module will only work correctly on a
Raspberry Pi with the PiGlow accessory board correctly installed and configured.

"""

from time import sleep
from pyglow import PyGlow
import psutil


class CpuGlow:
    pg = PyGlow()

    def run(self, auto, pattern):
        """
        Lets you run one of the light patterns defined in this class.
        You can run them once, or forever. It's really up to you.
        @param auto: boolean Run forever or only once.
        @param pattern: one of the patterns in this class
        @return: nothing
        """
        if auto:
            try:
                while auto:
                    if pattern == "snake":
                        self.snake()
                    elif pattern == "equalizer":
                        self.equalizer()
                        sleep(0.2)
            except KeyboardInterrupt:
                self.pg.all(0)

    def snake(self):
        """
        Makes the lights along the arm blink faster, and they only
        blink up to the level of the cpu usage.

        This one might need refactored again.

        """

        arm = [1, 2, 3, 4, 5, 6]
        cpu = psutil.cpu_percent()
        brightness = 70
        assert isinstance(cpu, float)
        speed = 300 + (2 * int(cpu))
        level = 100 / len(arm)

        for i in range(len(arm)):
            if cpu >= level * i:
                self.pg.pulse(arm[i], brightness, speed)

    def equalizer(self):
        """

          Lights from the center outward, illuminating more lights as the CPU usage increases.

        @rtype :nil
        """
        arm = [6, 5, 4, 3, 2, 1]
        level = 100 / len(arm)
        cpu = psutil.cpu_percent()
        brightness = 70

        for i in range(len(arm)):
            if cpu >= level * i:
                self.pg.led([i], brightness)
            else:
                self.pg.led([i], 0)


if __name__ == "__main__":
    cg = CpuGlow()
    cg.run(True, "snake")
