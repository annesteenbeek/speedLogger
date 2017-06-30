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
            if cols != "":
                cols += ","
            cols += '{cn} {dt}'.format(cn=cname,dt=dtype)

        sql = "CREATE TABLE IF NOT EXISTS {tn} ({cs})"\
                .format(tn=self.table_name,cs=cols)

        self.c.execute(sql)
        self.conn.commit()


    def add_test(self, result_dict):
        try:
            ping = result_dict['ping']
            down = result_dict['download']
            up = result_dict['upload']
            server_id = result_dict['server']['id']

            logging.info("Speedtest result: D{:.2f}MB U{:.2f}MB P{:.2f}ms"\
                    .format(down/1024/1024, up/1024/1024, ping))

            self.c.execute("INSERT INTO {tn} VALUES (CURRENT_TIMESTAMP,{p},{d},{u},{sid})"\
                .format(tn=self.table_name,p=ping,d=down,u=up,sid=server_id))
            self.conn.commit()

        except KeyError:
            logging.error('Results are missing data')
        except sqlite3.IntegrityError:
            logging.error('Date time already exists, not adding data')


#    def get_tests(self, end_date, start_date=today):
#        pass



