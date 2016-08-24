#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: point_manager_reader

:Synopsis:

:Author:
    servilla
  
:Created:
    8/23/16
"""

import logging

logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
                    datefmt='%Y-%m-%d% H:%M:%S%z')
logging.getLogger('').setLevel(logging.WARN)
logger = logging.getLogger('point_manager_reader')

import point_manager

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
        self.Point = self.sensor.Point

    def get_id(self):
        return self.id

    def get_type(self):
        return self.type

    def get_snid(self):
        return self.snid

    def get_batt(self):
        return self.batt

    def get_battlife(self):
        return self.battlife

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

    def get_Value(self):
        return self.Value


def main():

    xml = open('./data/pointManagerData.xml').read()
    pm = point_manager.CreateFromDocument(xml)
    print('Point Manager Attributes: {0}, {1}, {2}'.format(pm.id, pm.ts, pm.NoSensors))
    for sensor in pm.Sensor:
        s = Sensor(sensor)
        p = Point(s.get_Point())
        print('Sensor {0}'.format(s.get_id()))
        print('     Sensor Attributes: {0}, {1}, {2}, {3}, {4}'.format(s.get_id(), s.get_type(), s.get_snid(), s.get_batt(), s.get_battlife()))
        print('     Sensor Data: {0}, {1}, {2}'.format(s.get_Age(), s.get_Status(), s.get_Service()))
        print('     Point Attributes: {0}, {1}, {2}, {3}, {4}'.format(p.get_id(), p.get_type(), p.get_dtype(), p.get_ptid(), p.get_index()))
        print('     Point Data: {0}\n'.format(p.get_Value()))

    return 0


if __name__ == "__main__":
    main()

