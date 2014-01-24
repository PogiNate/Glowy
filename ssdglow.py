#!/usr/bin/env python
"""

Let's light up the third leg of the PiGlow with information on storage!

"""
__author__ = 'Nate Dickson'

from time import sleep
from pyglow import PyGlow
import psutil


class SSDGlow():
    """

    Methods to light up the third leg of the PiGlow with data on storage
    space used. This will probably be the least interesting one, no?

    """
    pg = PyGlow()
    arm = [18, 17, 16, 15, 14, 13]
    brightness = 70
    peak = 0

    def run(self, auto, pattern):
        try:
            while auto:
                if pattern == "eq":
                    self.equalizer()
                elif pattern == "snake":
                    self.snake()
                else:
                    self.snake() # I may add other patterns later, you don't know!
        except KeyboardInterrupt:
            self.pg.all(0)

    def equalizer(self):
        """
        Fancy Equalizer effect. Probably.

        """
        used = psutil.disk_usage("/")[3]
        speed = 100
        level = 100 / len(self.arm)
        #print "Used: %f, level: %f" %(used, level)
        for i in range(len(self.arm)):
            if used >= level * i:
                #self.pg.led(self.arm[i], self.brightness)
                if i > self.peak:
                    self.peak = i
            #else:
              #self.pg.led(self.arm[i],0)
            
        self.pg.pulse(self.arm[self.peak], self.brightness + 10, speed)


    def snake(self):
        """
        Same pulse snake effect as the others.

        """
        used = psutil.disk_usage("/")[3]
        speed = 300
        level = 100 / len(self.arm)

        for i in range(len(self.arm)):
            if used >= level * i:
                self.pg.pulse(self.arm[i], self.brightness, speed)


if __name__ == "__main__":
    sg = SSDGlow()
    sg.run(True, "eq")
