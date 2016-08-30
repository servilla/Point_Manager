#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: point_manager_db

:Synopsis:

:Author:
    servilla
  
:Created:
    8/27/16
"""

from sqlalchemy import Column, Integer, Float, String, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta

Base = declarative_base()

import logging

logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
                    datefmt='%Y-%m-%d% H:%M:%S%z')
logging.getLogger('').setLevel(logging.WARN)
logger = logging.getLogger('point_manager_db')


class SensorRaw(Base):
    #Sensor DB ORM

    __tablename__ = 'sensors_raw'

    index = Column(Integer, primary_key=True, autoincrement=True)
    collection_timestamp = Column(DateTime, nullable=False)
    point_manager_id = Column(String, nullable=False)
    point_manager_ts = Column(String, nullable=False)
    sensor_id = Column(Integer, nullable=False)
    sensor_type = Column(Integer, nullable=False)
    sensor_serial_no = Column(String, nullable=False)
    sensor_battery = Column(Integer, nullable=False)
    sensor_battery_life = Column(String, nullable=False)
    sensor_age = Column(Integer, nullable=False)
    sensor_status = Column(Integer, nullable=False)
    sensor_service = Column(Integer, nullable=False)
    point_id = Column(Integer, nullable=False)
    point_type = Column(String, nullable=False)
    point_data_type = Column(Integer, nullable=False)
    point_serial_no = Column(String, nullable=False)
    point_index = Column(Integer, nullable=False)
    point_value = Column(Float, nullable=False)


class SensorCooked(Base):
    #Sensor DB ORM

    __tablename__ = 'sensors_cooked'

    index = Column(Integer, primary_key=True, autoincrement=True)
    collection_timestamp = Column(DateTime, nullable=False)
    point_manager_id = Column(String, nullable=False)
    sensor_timestamp = Column(DateTime, nullable=False)
    sensor_id = Column(Integer, nullable=False)
    sensor_type = Column(Integer, nullable=False)
    sensor_serial_no = Column(String, nullable=False)
    sensor_battery = Column(Integer, nullable=False)
    sensor_battery_life = Column(Date, nullable=False)
    sensor_age = Column(Integer, nullable=False)
    sensor_status = Column(Integer, nullable=False)
    sensor_service = Column(Integer, nullable=False)
    point_id = Column(Integer, nullable=False)
    point_type = Column(String, nullable=False)
    point_data_type = Column(Integer, nullable=False)
    point_serial_no = Column(String, nullable=False)
    point_index = Column(Integer, nullable=False)
    point_value = Column(Float, nullable=False)


def get_sensor_db_cwd():
    import os
    cwd = os.getcwd()
    return cwd + '/sensors.db'


def connect_sensor_db():
    from sqlalchemy import create_engine
    sensor_db_path = get_sensor_db_cwd()
    engine = create_engine('sqlite:///' + sensor_db_path)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


def add_sensor_raw(ts=None, pm_id=None, pm_ts=None, sensor=None, session=None):
    s = SensorRaw(
        collection_timestamp=ts,
        point_manager_id=pm_id,
        point_manager_ts=pm_ts,
        sensor_id=sensor.get_id(),
        sensor_type=sensor.get_type(),
        sensor_serial_no=sensor.get_snid(),
        sensor_battery=sensor.get_batt(),
        sensor_battery_life=sensor.get_battlife(),
        sensor_age=sensor.get_Age(),
        sensor_status=sensor.get_Status(),
        sensor_service=sensor.get_Service(),
        point_id=sensor.get_Point().get_id(),
        point_type=sensor.get_Point().get_type(),
        point_data_type=sensor.get_Point().get_dtype(),
        point_serial_no=sensor.get_Point().get_ptid(),
        point_index=sensor.get_Point().get_index(),
        point_value=sensor.get_Point().get_Value()
    )
    session.add(s)
    session.commit()


def add_sensor_cooked(ts=None, pm_id=None, sensor=None, session=None):
    s = SensorCooked(
        collection_timestamp=ts,
        point_manager_id=pm_id,
        sensor_timestamp=(ts - timedelta(seconds=sensor.get_Age())),
        sensor_id=sensor.get_id(),
        sensor_type=sensor.get_type(),
        sensor_serial_no=sensor.get_snid(),
        sensor_battery=sensor.get_batt(),
        sensor_battery_life=sensor.get_battlife(as_date=True),
        sensor_age=sensor.get_Age(),
        sensor_status=sensor.get_Status(),
        sensor_service=sensor.get_Service(),
        point_id=sensor.get_Point().get_id(),
        point_type=sensor.get_Point().get_type(),
        point_data_type=sensor.get_Point().get_dtype(),
        point_serial_no=sensor.get_Point().get_ptid(),
        point_index=sensor.get_Point().get_index(),
        point_value=sensor.get_Point().get_Value(as_celsius=True)
    )
    session.add(s)
    session.commit()


def main():

    connect_sensor_db()

    return 0


if __name__ == "__main__":
    main()