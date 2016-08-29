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

Base = declarative_base()

import logging

logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
                    datefmt='%Y-%m-%d% H:%M:%S%z')
logging.getLogger('').setLevel(logging.WARN)
logger = logging.getLogger('point_manager_db')


class Sensor(Base):
    #Sensor DB ORM

    __tablename__ = 'sensors'

    index = Column(Integer, primary_key=True, autoincrement=True)
    point_manager_id = Column(String, nullable=False)
    point_manager_timestamp = Column(DateTime, nullable=False)
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


def add_sensor(pm_id=None, pm_ts=None, s=None, session=None):
    sensor = Sensor(
        point_manager_id=pm_id,
        point_manager_timestamp=pm_ts,
        sensor_id=s.get_id(),
        sensor_type=s.get_type(),
        sensor_serial_no=s.get_snid(),
        sensor_battery=s.get_batt(),
        sensor_battery_life=s.get_battlife(),
        sensor_age=s.get_Age(),
        sensor_status=s.get_Status(),
        sensor_service=s.get_Service(),
        point_id=s.get_Point().get_id(),
        point_type=s.get_Point().get_type(),
        point_data_type=s.get_Point().get_dtype(),
        point_serial_no=s.get_Point().get_ptid(),
        point_index=s.get_Point().get_index(),
        point_value=s.get_Point().get_Value_as_F()
    )
    session.add(sensor)
    session.commit()


def main():

    connect_sensor_db()

    return 0


if __name__ == "__main__":
    main()