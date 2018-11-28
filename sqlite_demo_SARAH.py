import sqlite3

conn = sqlite3.connect('data.sqlite')

cur = conn.cursor()
cur.execute("select * from Abs;")

results = cur.fetchall()
print(results)


cur.close()
conn.close()





# import random
# import sqlite3
# db = sqlite3.connect('data.sqlite')






# for row in db.execute('select AbsExercise from Abs'):
#     print(row[0])

# def select_ab_exercise():
#     for row in db.execute('select AbsExercise from Abs'):
#     print(row)

# print("{}".format(random.choice(players)))



# for row in db.execute('select * from MuscleGroup'):
#     print(row)

# for row in db.execute('select * from Back'):
#     print(row)

# for row in db.execute('select * from Abs'):
#     print(row)

# for row in db.execute('select * from Duration'):
#     print(row)

# for row in db.execute('select * from Chest'):
#     print(row)

# for row in db.execute('select * from Legs'):
#     print(row)

# for row in db.execute('select * from Arms'):
#     print(row)

# for row in db.execute('select * from Stretch'):
#     print(row)

# for row in db.execute('select * from CoreBody'):
#     print(row)
