#! /usr/bin/env Python
"""
For now this just calls the three modules. Once I learn how to process command line arguments I'll augment this to handle those as well.
"""
__author__ = 'Nate Dickson'
#import sys
#import getopt
import cpuglow
import memglow

def main():
    cpuglow.equalizer()
    memglow.pulse()

if __name__ == '__main__':
    main()
