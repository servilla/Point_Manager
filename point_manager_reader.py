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

    def get_battlife(self, as_date=False):
        battlife = self.battlife
        if as_date:
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

    def get_Value(self, as_celsius=False):
        value = self.Value
        if as_celsius:
            value = (self.Value - 32) * 5.0 / 9.0
        return value


def main(argv):
    usage = 'Usage: python ./point_manager_reader.py -h (help) | ' +\
            '-f <filepath/filename> | -u <data URL>'

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

    now = datetime.now()
    pm = point_manager.CreateFromDocument(xml)
    print('Point Manager Attributes: {0}, {1}, {2}'.format(pm.id, pm.ts,
                                                           pm.NoSensors))
    session = point_manager_db.connect_sensor_db()
    for sensor in pm.Sensor:
        s = Sensor(sensor)
        print('Sensor {0}'.format(s.get_id()))
        print('     Sensor Attributes: {0}, {1}, {2}, {3}, {4}'.format(
            s.get_id(), s.get_type(), s.get_snid(), s.get_batt(),
            s.get_battlife(as_date=True)))
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
        print('     Point Data: {0}\n'.format(p.get_Value(as_celsius=True)))
        if s.get_snid()=='00000000D81C05D4': 
#             if p.get_Value(as_celsius=True) > -75.00:
#                print('1-DGR: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
#             else:
                print('1-DGR: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000EC1905D4': 
#             if p.get_Value(as_celsius=True) > -60.00:
#                print('2-DGR: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
#             else:
                print('2-DGR-BK: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000681E05D4': 
             if p.get_Value(as_celsius=True) > -75.00:
                print('3-DGR: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
             else:
                print('3-DGR: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='000000002C1D05D4': 
             if p.get_Value(as_celsius=True) > -75.00:
                print('4-DGR: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
             else:
                print('4-DGR: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000981B05D4': 
             if p.get_Value(as_celsius=True) > -75.00:
                print('5-DGR: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
             else:
                print('5-DGR: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000741F05D4': 
             if p.get_Value(as_celsius=True) > -75.00:
                print('18-DGR: {0:.2f} {1} is in maintenance'.format(p.get_Value(as_celsius=True),s.get_Age()))
             else:
                print('18-DGR: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000341905D4': 
#             if p.get_Value(as_celsius=True) > -75.00:
#                print('7-DGR: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
#             else:
                print('7-DGR: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000481E05D4': 
             if p.get_Value(as_celsius=True) > -75.00:
                print('8-DGR: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
             else:
                print('8-DGR: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000082005D4': 
             if p.get_Value(as_celsius=True) > -75.00:
                print('9-DGR: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
             else:
                print('9-DGR: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000802005D4': 
             if p.get_Value(as_celsius=True) > -75.00:
                print('10-DGR: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
             else:
                print('10-DGR: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='000000001C1D05D4': 
             if p.get_Value(as_celsius=True) > -75.00:
                print('11-DGR: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
             else:
                print('11-DGR: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000641E05D4': 
             if p.get_Value(as_celsius=True) > -75.00:
                print('12-DGR: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
             else:
                print('12-DGR: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000541E05D4': 
             if p.get_Value(as_celsius=True) > -75.00:
                print('13-DGR: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
             else:
                print('13-DGR: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000601E05D4': 
             if p.get_Value(as_celsius=True) > -65.00:
                print('14-DGR: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
             else:
                print('14-DGR: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='000000001C1905D4': 
             if p.get_Value(as_celsius=True) > -75.00:
                print('15-DGR: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
             else:
                print('15-DGR: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000B01B05D4': 
             if p.get_Value(as_celsius=True) > -75.00:
                print('16-DGR: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
             else:
                print('16-DGR: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000E81B05D4': 
             if p.get_Value(as_celsius=True) > -75.00:
                print('17-DGR: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
             else:
                print('17-DGR: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='000000000C1905D4': 
#             if p.get_Value(as_celsius=True) > -15.00:
#                print('1-DP MSB: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
#             else:
                print('1-DP: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000E81C05D4': 
#             if p.get_Value(as_celsius=True) > -75.00:
#                print('2-DP MSB: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
#             else:
                print('2-DP: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000D41C05D4': 
#             if p.get_Value(as_celsius=True) > -75.00:
#                print('1-IPM MSB: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
#             else:
                print('1-IPM: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='000000000C1E05D4': 
#             if p.get_Value(as_celsius=True) > -10.00:
#                print('2-IPM: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
#             else:
                print('2-IPM: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000B01D05D4': 
#             if p.get_Value(as_celsius=True) > -10.00:
#                print('3-IPM: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
#             else:
                print('3-IPM: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000241905D4': 
             if p.get_Value(as_celsius=True) > -10.00:
                print('4-IPM: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
             else:
                print('4-IPM: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000E41C05D4': 
             if p.get_Value(as_celsius=True) > -10.00:
                print('5-IPM: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
             else:
                print('5-IPM: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000E01C05D4': 
             if p.get_Value(as_celsius=True) > -10.00:
                print('6-IPM: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
             else:
                print('6-IPM: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000F41C05D4': 
#             if p.get_Value(as_celsius=True) > -75.00:
#                print('7-IPM: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
#             else:
                print('7-IPM: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000A01B05D4': 
             if p.get_Value(as_celsius=True) > -10.00:
                print('8-IPM: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
             else:
                print('8-IPM: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000CC1C05D4': 
#             if p.get_Value(as_celsius=True) > -75.00:
#                print('BURN MSB: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
#             else:
                print('BURN MSB: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='000000006C1F05D4': 
             if p.get_Value(as_celsius=True) > -10.00:
                print('DOCK MSB: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
             else:
                print('DOCK MSB: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000581E05D4': 
#             if p.get_Value(as_celsius=True) > -10.00:
#                print('1-FISH: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
#             else:
                print('1-FISH: {0:.2f}  {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000F81805D4': 
             if p.get_Value(as_celsius=True) > -10.00:
                print('2-FISH: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
             else:
                print('2-FISH: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000DC1B05D4': 
             if p.get_Value(as_celsius=True) > -60.00:
                print('3-FISH: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
             else:
                print('3-FISH: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000CF5105D4': 
#             if p.get_Value(as_celsius=True) > -70.00:
#                print('4-FISH: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
#             else:
                print('4-FISH: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='000000000C1D05D4': 
             if p.get_Value(as_celsius=True) > -10.00:
                print('1-PARA: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
             else:
                print('1-PARA: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='000000007C1D05D4': 
 #            if p.get_Value(as_celsius=True) > -10.00:
#                print('2-PARA: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
#             else:
                print('2-PARA: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        if s.get_snid()=='00000000441E05D4': 
             if p.get_Value(as_celsius=True) > -10.00:
                print('AWET MSB: {0:.2f} {1} is in alarm'.format(p.get_Value(as_celsius=True),s.get_Age()))
             else:
                print('AWET MSB: {0:.2f} {1}'.format(p.get_Value(as_celsius=True),s.get_Age()))
        point_manager_db.add_sensor_raw(ts=now, pm_id=pm.id, pm_ts=pm.ts,
                                        sensor=s, session=session)
        point_manager_db.add_sensor_cooked(ts=now, pm_id=pm.id, sensor=s,
                                           session=session)

    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
