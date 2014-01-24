#! /usr/bin/env Python
"""
For now this just calls the three modules. Once I learn how to process command line arguments I'll augment this to handle those as well.
"""
__author__ = 'Nate Dickson'
#import sys
from cpuglow import CpuGlow
from memglow import MemGlow
from ssdglow import SSDGlow
from time import sleep


def main():
    try:
        cg = CpuGlow()
        mg = MemGlow()
        sg = SSDGlow()
        while True:
            sg.equalizer()
            mg.one_pulse()
            cg.snake()
            #sleep(0.2)
    except KeyboardInterrupt:
        CpuGlow.pg.all(0)

if __name__ == '__main__':
    main()
