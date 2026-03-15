# 🇯🇵 Japan Travel Explorer & Landmark Visualizer
**Capstone Project | Python for Everybody (PY4E) Specialization**

## 📌 Project Overview
This application is a full-cycle data pipeline built to assist in planning my upcoming trip to Japan in June 2026. The tool automates the retrieval of attraction data from the TripAdvisor API, stores it in a structured SQLite database, and generates an interactive geospatial visualization.

## 🚀 The "Why"
- **Personal Utility:** Solved a real-world need to visualize landmark proximity in Tokyo, Kyoto, and Osaka for itinerary optimization.
- **Self-Taught Milestone:** This project represents the culmination of my journey through the University of Michigan's PY4E specialization, demonstrating proficiency in Python, SQL, and API integration.

## 🛠️ Technical Stack
- **Language:** Python 3
- **Data Acquisition:** `urllib`, `json`, and `RapidAPI` (REST API integration)
- **Data Storage:** `sqlite3` (Relational database management and Master table joins)
- **Visualization:** `folium` (Geospatial mapping with Leaflet.js)
- **Environment:** `python-dotenv` (Secure API key management)

## 📂 Project Structure
- **`app.py`**: The main entry point. Reads processed coordinates from the SQL Master table and generates the interactive map.
- **`index.html`**: The final output. An interactive, browser-based map of Japan with custom markers.
- **`scripts/data_fetcher.py`**: A modular script that fetches attraction lists and deep details while respecting API rate limits.
- **`scripts/database_manager.py`**: Handles SQL schema creation, JSON parsing, and data insertion.
- **`japan_database.sqlite`**: The local relational database used for persistence.

## 💡 Key Features
- **Relational Data Modeling:** Uses a `Master` table to join attraction descriptions with geographic coordinates.
- **Rate-Limited Scraping:** Implements time delays to ensure stable communication with the RapidAPI server.
- **Interactive UI:** Features custom popups and tooltips for each landmark.

## ⚙️ How to Run
1. **Clone the Repo:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/japan-travel-app.git](https://github.com/YOUR_USERNAME/japan-travel-app.git)

2. bash pip install folium python-dotenv
3. bash python app.py
4. View Map: Open index.html in any web browser.
