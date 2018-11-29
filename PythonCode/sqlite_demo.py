import sqlite3
db = sqlite3.connect('data.sqlite')

for row in db.execute('select * from MuscleGroup'):
    print(row)

for row in db.execute('select * from Back'):
    print(row)

for row in db.execute('select * from Abs'):
    print(row)

for row in db.execute('select * from Duration'):
    print(row)

for row in db.execute('select * from Chest'):
    print(row)

for row in db.execute('select * from Legs'):
    print(row)

for row in db.execute('select * from Arms'):
    print(row)

for row in db.execute('select * from Stretch'):
    print(row)

for row in db.execute('select * from CoreBody'):
    print(row)
