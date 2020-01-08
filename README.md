# Point_Manager
Python source to manage Point Manager data files.

###Installation###
1. Create a local virtual environment
	- conda create --name point --no-default-packages
2. conda activate point
3. conda install requests sqlalchemy
4. pip install pyxb==1.2.4 
5. git clone https://github.com/servilla/Point_Manager.git
6. cd Point_Manager
7. touch sensors.db
8. python3 ./point_manager_reader.py -f ./data/pointManagerData.xml
or
8. python3 ./point_manager_reader.py -u http://10.153.147.94/xmldata

###Usage###
`python ./point_manager_reader.py -h (help) | -f <filepath/filename> | -u <data URL>`
