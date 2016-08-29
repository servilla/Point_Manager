#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: point_manager_reader

:Synopsis:

:Author:
    servilla
  
:Created:
    8/23/16
"""

import requests
import getopt
import sys
from datetime import date
from datetime import datetime

import point_manager
import point_manager_db

import logging

# Setup logging
logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S%z')
logging.getLogger('').setLevel(logging.WARN)
logger = logging.getLogger('point_manager_reader')


class Sensor(object):
    def __init__(self, sensor=None):
        self.sensor = sensor

        # Attributes
        self.id = self.sensor.id
        self.type = self.sensor.type
        self.snid = self.sensor.snid
        self.batt = self.sensor.batt
        self.battlife = self.sensor.battlife

        # Elements
        self.Age = self.sensor.Age
        self.Status = self.sensor.Status
        self.Service = self.sensor.Service
        self.Point = Point(self.sensor.Point)

    def get_id(self):
        return self.id

    def get_type(self):
        return self.type

    def get_snid(self):
        return self.snid

    def get_batt(self):
        return self.batt

    def get_battlife(self):
        d = self.battlife.split('/')
        battlife = date(int(d[2]) + 2000, int(d[0]), int(d[1]))
        return battlife

    def get_Age(self):
        return self.Age

    def get_Status(self):
        return self.Status

    def get_Service(self):
        return self.Service

    def get_Point(self):
        return self.Point


class Point(object):
    def __init__(self, point=None):
        self.point = point

        # Attributes
        self.id = self.point.id
        self.type = self.point.type
        self.dtype = self.point.dtype
        self.ptid = self.point.ptid
        self.index = self.point.index

        # Elements
        self.Value = self.point.Value

    def get_id(self):
        return self.id

    def get_type(self):
        return self.type

    def get_dtype(self):
        return self.dtype

    def get_ptid(self):
        return self.ptid

    def get_index(self):
        return self.index

    def get_Value_as_F(self):
        return self.Value

    def get_Value_as_C(self):
        return (self.Value - 32) * 5.0 / 9.0


def main(argv):
    usage = 'Usage: python ./point_manager_reader.py -h (help) | -f <filepath/filename> | -u <data URL>'

    if len(argv) == 0:
        logger.error(usage)
        sys.exit(1)

    try:
        opts, args = getopt.getopt(argv, 'hf:u:')
    except getopt.GetoptError as e:
        logger.error('Unrecognized command line flag: {0}'.format(e))
        sys.exit(1)

    fn = None
    url = None
    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit(0)
        elif opt == '-f':
            fn = arg
        elif opt == '-u':
            url = arg
        else:
            logger.error(usage)
            sys.exit(1)

    if fn and url:
        logger.error(usage)
        sys.exit(1)

    if fn:
        try:
            xml = open(fn).read()
        except IOError as e:
            logger.error('Data file read error: {0}'.format(e))
            sys.exit(1)
    else:
        try:
            r = requests.get(url=url)
            xml = r.text
        except requests.RequestException as e:
            logger.error('URL read error: {0}'.format(e))
            sys.exit(1)

    pm = point_manager.CreateFromDocument(xml)
    print('Point Manager Attributes: {0}, {1}, {2}'.format(pm.id, pm.ts,
                                                           pm.NoSensors))
    session = point_manager_db.connect_sensor_db()
    for sensor in pm.Sensor:
        s = Sensor(sensor)
        print('Sensor {0}'.format(s.get_id()))
        print('     Sensor Attributes: {0}, {1}, {2}, {3}, {4}'.format(
            s.get_id(), s.get_type(), s.get_snid(), s.get_batt(),
            s.get_battlife()))
        print('     Sensor Data: {0}, {1}, {2}'.format(s.get_Age(),
                                                       s.get_Status(),
                                                       s.get_Service()))

        p = s.get_Point()
        print(
            '     Point Attributes: {0}, {1}, {2}, {3}, {4}'.format(p.get_id(),
                                                                    p.get_type(),
                                                                    p.get_dtype(),
                                                                    p.get_ptid(),
                                                                    p.get_index()))
        print('     Point Data: {0}\n'.format(p.get_Value_as_C()))

        ts = pm.ts.split(' ')
        d = ts[0].split('/')
        t = ts[1].split(':')
        pm_ts = datetime(int(d[2]) + 2000, int(d[0]), int(d[1]), int(t[0]),
                         int(t[1]), int(t[2]))

        point_manager_db.add_sensor(pm_id=pm.id, pm_ts=pm_ts, s=s,
                                    session=session)

    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
