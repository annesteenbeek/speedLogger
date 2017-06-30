#!/usr/bin/python
import cronus.beat as beat
import time
import datetime
import speedtest

class Logger(object):

    def __init__(self, storage):
        self.storage = storage
        self.set_interval(60)
        

    """
    Change the interval between tests in minutes
    """
    def set_interval(self, interval):
        interval = max(1, interval)  # make sure interval is > 1
        hz = 1/float(interval*60)    # convert interval to Hz
        beat.set_rate(hz)

    def do_speedtest(self):
        s = speedtest.Speedtest()
        s.get_best_server()
        s.download()
        s.upload()

        self.storage.add_test(s.results.dict())

    def run(self):
        while beat.true():
            self.do_speedtest()
            beat.sleep()


