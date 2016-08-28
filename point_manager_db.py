#!/usr/bin/env python
# -*- coding: utf-8 -*-

""":Mod: point_manager_db

:Synopsis:

:Author:
    servilla
  
:Created:
    8/27/16
"""

from datetime import datetime
from sqlalchemy import Table, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

import logging

logging.basicConfig(format='%(asctime)s %(levelname)s (%(name)s): %(message)s',
                    datefmt='%Y-%m-%d% H:%M:%S%z')
logging.getLogger('').setLevel(logging.WARN)
logger = logging.getLogger('point_manager_db')


class Sensor(Base):
    #Sensor DB ORM

    __tablename__ = 'sensor'

    index = Column(Integer, primary_key=True)
    sensor_id = Column(Integer, nullable=False)
    sensor_type = Column(Integer, nullable=False)
    sensor_serial_no = Column(String, nullable=False)
    sensor_battery = Column(Integer, nullable=False)
    sensor_battery_life = Column(DateTime, nullable=False)
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
    return cwd + '/sensor.sqlite'

def create_sqlite3_db():
    from sqlalchemy import create_engine
    sensor_db_path = get_sensor_db_cwd()
    engine = create_engine('sqlite:///' + sensor_db_path)
    Base.metadata.create_all(engine)


def main():

    create_sqlite3_db()

    return 0


if __name__ == "__main__":
    main()