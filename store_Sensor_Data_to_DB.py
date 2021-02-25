#------------------------------------------
#--- Author: Pradeep Singh
#--- Date: 20th January 2017
#--- Version: 1.0
#--- Python Ver: 2.7
#--- Details At: https://iotbytes.wordpress.com/store-mqtt-data-from-sensors-into-sql-database/
#------------------------------------------

import json
import psycopg2

#===============================================================
# Database Manager Class

class DatabaseManager:
	def __init__(self):
		self.conn_string = "host='localhost' dbname ='db' user='postgres' password='udmt'"
		self.conn = psycopg2.connect(self.conn_string)
		self.cur = self.conn.cursor()
		print ("DB INIT SUCCESS")

	def add_del_update_db_record(self, sql_query, args):
		print("add start")
		self.cur.execute(sql_query, args)
		self.conn.commit()
		print("add end")
		return

	def __del__(self):
		self.cur.close()
		self.conn.close()

#===============================================================
# Functions to push Sensor Data into Database

# Function to save Waterflow to DB Table
def Waterflow_Data_Handler(Data):
	#Parse Data 
	SensorID,Data_and_Time,Waterflow=Data.split("/")
	print(SensorID,Data_and_Time,Waterflow)
	
	#Push into DB Table
	dbObj = DatabaseManager()
	dbObj.add_del_update_db_record("INSERT INTO waterflow_data (sensorid, date, waterflow) VALUES (%s,%s,%s)",(SensorID, Data_and_Time, Waterflow))
	del dbObj
	print ("Inserted waterflow Data into Database.")
	print ("")
