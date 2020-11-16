# pair programming 11
# Yingchen Liu, Erik Adames, Haipeng Lin
import sqlite3
db = sqlite3.connect('test_db.sqlite') # Create a connection to the database
cursor = db.cursor() # https://www.python.org/dev/peps/pep-0249/#cursor-objects
cursor.execute("DROP TABLE IF EXISTS candidates") # Convenient in case you want to start over

cursor.execute('''CREATE TABLE candidates (
               id INTEGER PRIMARY KEY NOT NULL, 
               first_name TEXT, 
               last_name TEXT, 
               middle_init TEXT, 
               party TEXT NOT NULL)''')

db.commit()

# add a single value
with open("candidates.txt",'r') as candidates:
    r = candidates.readline()
    r = candidates.readline()


    while r:
        items = r.split('|')

        cursor.execute('''INSERT INTO candidates
                    (id, first_name, last_name, middle_init, party)
                     VALUES (?, ?, ?, ?, ?)''', 
                    (items[0], items[1], items[2], items[3], items[4].replace('\n', '')))

        db.commit()
        r = candidates.readline()

cursor.execute("SELECT * FROM candidates")
all_rows = cursor.fetchall()
print(all_rows)