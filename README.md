# Point_Manager
Python source to manage Point Manager data files.

###Installation###
1. Create a local virtual environment
  - Python3: pyvenv venv
  - Python2: virtualenv venv
2. source ./venv/bin/activate
3. pip install --upgrade pip setuptools
4. pip install pyxb requests sqlalchemy
5. git clone https://github.com/servilla/Point_Manager.git
6. cd Point_Manager
7. touch sensors.db
8. python3 ./point_manager_reader.py -f ./data/pointManagerData.xml

###Usage###
`python ./point_manager_reader.py -h (help) | -f <filepath/filename> | -u <data URL>`
