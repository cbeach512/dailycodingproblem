#!/usr/bin/env python3
"""Problem - Day 10
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""
import time

class Scheduler():
    def __init__(self, function, timing):
        self.fun = function
        self.t = timing

    def run(self):
        time.sleep(self.t)
        self.fun()

    def go(self):
        try:
            while True:
                time.sleep(self.t)
                self.fun()
        except KeyboardInterrupt:
            pass

def f():
    print('function called')

if __name__ == '__main__':
    timing1 = float(input('timing (in milliseconds): ')) / 1000
    sched1 = Scheduler(f, timing1)
    sched1.run()

    timing2 = float(input('timing (in milliseconds): ')) /1000
    sched2 = Scheduler(f, timing2)
    sched2.go()

