#Team Haribo Gummy Bears - Claire Liu & Bo Hui Lu
#SoftDev1 pd6
#K #16: No Trouble
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
command = "CREATE TABLE students(name TEXT,age INTEGER,userid INTEGER)"
c.execute(command)
with open('peeps.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        command="INSERT INTO students(name, age, userid) VALUES ('"
        command+= row['name'] + "'," + row['age'] + "," + row['id']
        command+= ");" 
        c.execute(command)   

#==========================================================

db.commit() #save changes
db.close() #close database
