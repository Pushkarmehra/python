import folium
import requests
import time
from geopy.distance import geodesic
from twilio.rest import Client
from threading import Timer

# Twilio setup
account_sid = 'your_twilio_account_sid'
auth_token = 'your_twilio_auth_token'
twilio_client = Client(account_sid, auth_token)

# Google Maps API key
google_maps_api_key = 'your_google_maps_api_key'

# Crime data (latitude, longitude, crime weight)
crime_hotspots = [
    (28.7041, 77.1025, -10),  # Delhi center
    (28.6841, 77.1125, -8),   # Another hotspot
    # Add more crime hotspot locatin
]

# Function to fetch routes and travel times from Google Maps API
def get_routes_and_travel_time(origin, destination):
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&alternatives=true&key={google_maps_api_key}"
    response = requests.get(url)
    routes_data = response.json()
    return routes_data['routes']

# Function to calculate the safety score for a route
def calculate_route_safety(route):
    total_safety_score = 0
    for step in route['legs'][0]['steps']:
        step_start_location = (step['start_location']['lat'], step['start_location']['lng'])
        step_end_location = (step['end_location']['lat'], step['end_location']['lng'])

        # Calculate safety score based on proximity to crime hotspots
        for hotspot in crime_hotspots:
            hotspot_location = (hotspot[0], hotspot[1])
            distance_to_hotspot = geodesic(step_start_location, hotspot_location).km
            if distance_to_hotspot < 1:  # If route is within 1 km of a hotspot
                total_safety_score += hotspot[2]  # Add crime weight (negative score)

    return total_safety_score

# Choose the safest route
def choose_safest_route(routes):
    best_route = None
    best_safety_score = float('-inf')

    for route in routes:
        route_safety_score = calculate_route_safety(route)
        print(f"Route distance: {route['legs'][0]['distance']['text']} | Safety score: {route_safety_score}")

        if route_safety_score > best_safety_score:
            best_safety_score = route_safety_score
            best_route = route

    return best_route

# Send SOS alerts to emergency contacts using Twilio
def send_sos_alert(user_info, message):
    for contact in user_info['emergency_contacts']:
        # Send SMS
        twilio_client.messages.create(
            body=message,
            from_='+1234567890',  # Twilio number
            to=contact
        )

        # Call emergency contacts
        twilio_client.calls.create(
            url='http://demo.twilio.com/docs/voice.xml',
            to=contact,
            from_='+1234567890'
        )

# Function to track user in real time and monitor deviations from the safest route
def track_user_real_time(safest_route, user_info, max_delay):
    start_time = time.time()
    route_coordinates = [(step['start_location']['lat'], step['start_location']['lng']) for step in safest_route['legs'][0]['steps']]

    def check_user_location():
        current_location = get_current_user_location()  # Function to get user's real-time GPS coordinates

        # Calculate how far the user is from the safest route
        distance_to_route = min([geodesic(current_location, route_coord).km for route_coord in route_coordinates])

        # If user deviates from the route (more than 1 km), trigger an SOS alert
        if distance_to_route > 1:
            print("User deviated from the safest route!")
            send_sos_alert(user_info, "Alert: User has deviated from the safest route.")
        
        # If user is delayed
        elapsed_time = time.time() - start_time
        if elapsed_time > max_delay:
            print("User is delayed!")
            send_sos_alert(user_info, "Alert: User is delayed and may be in danger.")

        # Check every 5 minutes
        tracking_timer = Timer(300, check_user_location)
        tracking_timer.start()

    check_user_location()

# Function to display the safest route on a map
def display_safe_route(route):
    map_center = [route['legs'][0]['start_location']['lat'], route['legs'][0]['start_location']['lng']]
    safe_map = folium.Map(location=map_center, zoom_start=12)

    route_coordinates = [(step['start_location']['lat'], step['start_location']['lng']) for step in route['legs'][0]['steps']]
    folium.PolyLine(locations=route_coordinates, color="green", weight=5).add_to(safe_map)

    for hotspot in crime_hotspots:
        folium.CircleMarker(location=[hotspot[0], hotspot[1]], radius=5, color='red', fill=True).add_to(safe_map)

    safe_map.save("safe_route_map.html")
    print("Safe route map generated.")
    return safe_map

# Function to get the user's current GPS location (you will replace this with actual GPS fetching logic)
def get_current_user_location():
    return (28.7041, 77.1025)  # Example coordinates for Delhi