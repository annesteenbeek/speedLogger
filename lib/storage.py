#!/usr/bin/python
import sqlite3
import logging
from collections import OrderedDict

class Storage(object):

    def __init__(self):
        self.filename = 'storage.sqlite'
        self.table_name = 'speedtests'
        self.fields = OrderedDict([('date_time', 'TEXT PRIMARY KEY'),
                       ('ping', 'REAL'),
                       ('down', 'REAL'),
                       ('up', 'REAL'),
                       ('server_id','INTEGER')])
        self.conn = sqlite3.connect(self.filename)
        self.c = self.conn.cursor()

        self.setup_db()

    def setup_db(self):
        cols = ""
        for cname, dtype in self.fields.iteritems():
            cols += '{cn} {dt}, '.format(cn=cname,dt=dtype)

        print cols

        self.c.execute('CREATE TABLE IF NOT EXISTS {tn} ({cs})'\
                .format(tn=self.table_name,cs='1st_column INTEGER PRIMARY KEY'))

        self.conn.commit()


    def add_test(self, result_dict):
        try:
            ping = result_dict['ping']
            down = result_dict['download']
            up = result_dict['upload']
            sid = results_dict['server']['id']

            self.c.execute("INSERT INTO {tn} VALUES (DATE('now'),{p},{d},{u},{sid})"\
                .format(tn=self.table_name,p=ping,d=down,u=up,sid=server_id))
            self.conn.commit()

        except KeyError:
            logging.error('Results are missing data')


#    def get_tests(self, end_date, start_date=today):
#        pass



