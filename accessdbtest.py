# import pyodbc 


conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\szazyczny1\Documents\4ProblemSolvingAndSoftwareDesign\TermProject\FitnessExercisesDB.accdb;' 
    )
# cnxn = pyodbc.connect(conn_str)
# crsr = cnxn.cursor()
# for table_info in crsr.tables(tableType='TABLE'):
#     print(table_info.table_name)


import pyodbc

conn = pyodbc.connect(
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:C:\MIS3640GitHub\MIS3640-TermProject-AFSRSZ\FitnessExercisesDB.accdb;' 
    )
cursor = conn.cursor()
cursor.execute('select * from MuscleGroup')
   
for row in cursor.fetchall():
    print (row)

