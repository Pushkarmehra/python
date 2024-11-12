import folium
import requests
from geopy.distance import geodesic
from twilio.rest import Client
from threading import Timer
import time

# Twilio setup (replace with your actual Twilio credentials)
account_sid = 'your_twilio_account_sid'
auth_token = 'your_twilio_auth_token'
twilio_client = Client(account_sid, auth_token)

# Google Maps API key (replace with your actual API key)
google_maps_api_key = 'your_google_maps_api_key'

# Crime data
crime_hotspots = [
    (28.7041, 77.1025, -10),  # Example hotspot
]

def get_routes_and_travel_time(origin, destination):
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&alternatives=true&key={google_maps_api_key}"
    response = requests.get(url)
    
    # Debug: Print response status and content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.json()}")  # Print the response for debugging
    
    if response.status_code == 200:
        return response.json().get('routes', [])
    else:
        print("Error fetching routes")
        return []

def calculate_route_safety(route):
    total_safety_score = 0
    for step in route['legs'][0]['steps']:
        step_start_location = (step['start_location']['lat'], step['start_location']['lng'])
        step_end_location = (step['end_location']['lat'], step['end_location']['lng'])
        for hotspot in crime_hotspots:
            hotspot_location = (hotspot[0], hotspot[1])
            distance_to_hotspot = geodesic(step_start_location, hotspot_location).km
            if distance_to_hotspot < 1:
                total_safety_score += hotspot[2]
    return total_safety_score

def choose_safest_route(routes):
    best_route = None
    best_safety_score = float('-inf')
    
    if not routes:
        print("No routes found")
        return None
    
    for route in routes:
        route_safety_score = calculate_route_safety(route)
        print(f"Route distance: {route['legs'][0]['distance']['text']} | Safety score: {route_safety_score}")
        if route_safety_score > best_safety_score:
            best_safety_score = route_safety_score
            best_route = route
    return best_route

def display_safe_route(route):
    # Check if route is None
    if route is None:
        print("No route available to display.")
        return None

    # Check if 'legs' exists in the route and has valid data
    if 'legs' not in route or not route['legs']:
        print("Route does not contain valid 'legs' data.")
        return None
    
    map_center = [route['legs'][0]['start_location']['lat'], route['legs'][0]['start_location']['lng']]
    safe_map = folium.Map(location=map_center, zoom_start=12)
    
    route_coordinates = [(step['start_location']['lat'], step['start_location']['lng']) for step in route['legs'][0]['steps']]
    
    folium.PolyLine(locations=route_coordinates, color="green", weight=5).add_to(safe_map)
    
    for hotspot in crime_hotspots:
        folium.CircleMarker(location=[hotspot[0], hotspot[1]], radius=5, color='red', fill=True).add_to(safe_map)
    
    safe_map.save("safe_route_map.html")
    return safe_map

# Example usage
origin = "28.7041,77.1025"
destination = "28.6100,77.2300"

# Fetch routes
routes = get_routes_and_travel_time(origin, destination)

# Check if routes were found
if not routes:
    print("No routes were found from the API.")
else:
    # Choose the safest route
    safest_route = choose_safest_route(routes)
    
    # Display safest route if valid
    if safest_route:
        safe_route_map = display_safe_route(safest_route)
    else:
        print("No safe route found.")