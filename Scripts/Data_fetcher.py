import json
import urllib.request
import urllib.parse
import time
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("RAPIDAPI_KEY")

def fetch_attractions():
    url = "https://tripadvisor-scraper.p.rapidapi.com/attractions/list"
    params = {"query":"294232"}
    full_url = url + "?" + urllib.parse.urlencode(params)


    headers = {
        "X-RapidAPI-Key": key,
        "X-RapidAPI-Host": "tripadvisor-scraper.p.rapidapi.com"}

    request = urllib.request.Request(full_url, headers=headers)

    try:
        with urllib.request.urlopen(request) as response:
            raw_data = response.read().decode("utf-8")
            data = json.loads(raw_data)
            with open ("data.json", "w") as f:
                json.dump(data, f, indent=4)
                print("Data saved to data.json")

    except urllib.error.HTTPError as e:
    # This will help you see if the error is 401 (Unauthorized) or 404 (Not Found)
        print(f"HTTP error: {e.code} - {e.reason}")
        print(e.read().decode()) # Print the server's error message
    except Exception as e:
        print(f"Other error: {e}")

def fetch_search_results():
    """Step 1: Get the list of attraction IDs and save to data.json"""
    if not key: return
    
    print("Step 1: Fetching main attraction list...")
    url = "https://tripadvisor-scraper.p.rapidapi.com/attractions/search"
    # (Your specific search parameters from your first script go here)
    # ...
    # After fetching, save data.json
    print("data.json created.")

def get_details(id):
    """Helper function to fetch specific details for an ID"""
    url = "https://tripadvisor-scraper.p.rapidapi.com/attractions/detail"
    param = urllib.parse.urlencode({"query": id})
    full_url = f"{url}?{param}"
    headers = {
        "X-RapidAPI-Key": key,
        "X-RapidAPI-Host": "tripadvisor-scraper.p.rapidapi.com"
    }

    req = urllib.request.Request(full_url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode("utf-8"))
            item = data.get('data') if 'data' in data else data
            if isinstance(item, list) and len(item) > 0:
                item = item[0]

            return {
                "name": item.get('name'),
                "address": item.get('address') or item.get('address_obj', {}).get('address_string'),
                "lat": item.get('latitude') or item.get('coordinates', {}).get('latitude'),
                "lng": item.get('longitude') or item.get('coordinates', {}).get('longitude')
            }
    except Exception as e:
        print(f"Failed to fetch {id}: {e}")
        return None

def fetch_all_details():
    """Step 2: Read data.json and fetch deep details for each ID"""
    print("Step 2: Fetching deep details for markers...")
    file = "data.json"
    all_details = []

    if not os.path.exists(file):
        print(f"Error: {file} not found. Run Step 1 first.")
        return

    with open(file, 'r') as f:
        load_data = json.load(f)

    for items in load_data.get('results', []):
        id = items.get("tripadvisor_entity_id")
        if id:
            print(f"Scraping details for: {id}")
            result = get_details(id)
            if result:
                all_details.append(result)
            time.sleep(2) # Respecting Rate Limits

    with open("detail.json", "w") as f:
        json.dump(all_details, f, indent=4)
    print("detail.json created.")

if __name__ == "__main__":
    if not key:
        print("Error: RAPIDAPI_KEY not found.")
    else:
        # Toggle these based on what you need to run
        # fetch_search_results() 
        fetch_all_details()