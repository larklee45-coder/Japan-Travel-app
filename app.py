import folium
import sqlite3

conn = sqlite3.connect('japan_database.sqlite')
cur = conn.cursor()

# 1. Fetch the data for the map
cur.execute('SELECT name, description, latitude, longitude FROM Master WHERE latitude IS NOT NULL')
rows = cur.fetchall()

# 2. Initialize a map centered on Japan
# Coordinates [36.2048, 138.2529] are the rough center of Japan
m = folium.Map(location=[36.2048, 138.2529], zoom_start=5, tiles='CartoDB positron')

# 3. Add markers for each attraction
for row in rows:
    name, desc, lat, lng = row
    
    # Create a popup with the name and description
    popup_text = f"<b>{name}</b><br>{desc}"
    
    folium.Marker(
        location=[lat, lng],
        popup=folium.Popup(popup_text, max_width=300),
        tooltip=name
    ).add_to(m)

# 4. Save the map
m.save('index.html')
conn.close()
print("Success! Open index.html to view your interactive Japan map.")
