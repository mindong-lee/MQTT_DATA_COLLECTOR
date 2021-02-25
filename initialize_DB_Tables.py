import psycopg2

# DB Table Schema
TableSchema="""
CREATE TABLE Waterflow_Data (
  SensorID text,
  Date text,
  Waterflow text
);
"""

#Connect or Create DB File
conn_string = "host='localhost' dbname ='db' user='postgres' password='udmt'"
conn = psycopg2.connect(conn_string)
cur = conn.cursor()

#Create Tables
cur.execute(TableSchema)
conn.commit()

#Close DB
cur.close()
conn.close()
