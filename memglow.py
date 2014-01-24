#!/usr/bin/env python
"""

We'll light up the second arm of the PiGlow based on memory usage.
Naturally this requires the PiGlow accessory to be properly installed and configured.

"""
__author__ = 'Nate Dickson'

from time import sleep
from pyglow import PyGlow
import psutil


class MemGlow:
    pg = PyGlow()

    def _one_pulse(self):
        """

        This will pulse the lights from the center to the edge
         based on memory usage.

        """

        arm = [12, 11, 10, 9, 8, 7]
        used = psutil.phymem_usage()[3]
        brightness = 70
        speed = 300
        level = 100 / len(arm)
        #print "Brightness: %d, speed: %d, level %f" %(brightness, speed, level)
        for i in range(len(arm)):
            if used >= level * i:
                self.pg.pulse(arm[i], brightness, speed)

    def pulse(self, auto):
        """

        If called with auto set to true this will run forever (or until a
        keyboard interrupt event). If called without a value it will run once.
        In either case this is basically a wrapper for one_pulse()

        @param auto:Boolean: If true it will run forever.
        """

        if auto:
            try:
                while auto:
                    self._one_pulse()
                    sleep(0.2)
            except KeyboardInterrupt:
                self.pg.all(0)
        else:
            self._one_pulse()


if __name__ == "__main__":
    mg = MemGlow()
    mg.pulse(True)
