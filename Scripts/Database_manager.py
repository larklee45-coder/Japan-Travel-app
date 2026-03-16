import sqlite3
import json

conn = sqlite3.connect('../japan_database.sqlite')
cur = conn.cursor()

#Table1
cur.execute ('''
    CREATE TABLE IF NOT EXISTS Attractions (
             name TEXT PRIMARY KEY,
             rating REAL,
             description TEXT
    )''')

#Table 2
#cur.execute('''DROP TABLE IF EXISTS Location''')

cur.execute ('''
CREATE TABLE IF NOT EXISTS Location (
             name TEXT PRIMARY KEY,
             address TEXT,
             latitude REAL,
             longitude REAL,
             FOREIGN KEY (name) REFERENCES Attractions
             )''')

with open('data.json', 'r') as f:
    data = json.load(f)

dive = data.get ('results', []) #data["results"]

for item in dive:
    name = item.get('name').strip()
    rating = item.get('rating')
    desc = item.get('description')
    #print(f"Adding {name}")

    cur.execute ('''
    INSERT OR IGNORE INTO Attractions (name, rating, description) VALUES(?, ?, ?)''',(name, rating, desc))

with open ('detail.json') as f:
    data = json.load(f)

for item in data:
    name = item.get('name').strip()
    address = item.get('address')
    lat = item.get('lat')
    lng = item.get('lng')

    cur.execute('''
INSERT OR IGNORE INTO Location (name, address, latitude, longitude) VALUES(?, ?, ?, ?)''', (name, address, lat, lng))

cur.execute('''
CREATE TABLE IF NOT EXISTS Master AS
SELECT
Attractions.name,
Attractions.rating,
Attractions.description,
Location.address,
Location.latitude,
Location.longitude
FROM Attractions
LEFT JOIN Location ON Attractions.name = Location.name''')

cur.execute('''
SELECT name, description, latitude, longitude
            FROM Master
            WHERE latitude IS NOT NULL and longitude IS NOT NULL''')

conn.commit()
print("All Done")

# Close the connection when finished
conn.close()
