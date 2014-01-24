#! /usr/bin/env Python
"""
For now this just calls the three modules. Once I learn how to process command line arguments I'll augment this to handle those as well.
"""
__author__ = 'Nate Dickson'
#import sys
from cpuglow import CpuGlow
from memglow import MemGlow


def main():
    try:
        while True:
            cg = CpuGlow()
            cg.equalizer()
            mg = MemGlow()
            mg.one_pulse()
    except KeyboardInterrupt:
        CpuGlow.pg.all(0)

if __name__ == '__main__':
    main()
