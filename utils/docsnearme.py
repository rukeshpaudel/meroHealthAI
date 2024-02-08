import gradio as gr
import googlemaps
from geopy.geocoders import Nominatim
import os
# Initialize Google Maps API client
gmaps = googlemaps.Client(key="AIzaSyB0gKa0rMc_OqxK0KvtDRDbghy8IRssjlY")

# Function to find nearest doctors
def find_nearest_doctors(location):
    # Convert address to coordinates
    geolocator = Nominatim(user_agent="geoapiExercises")
    loc = geolocator.geocode(location)
    latitude = loc.latitude
    longitude = loc.longitude

    # Find nearby doctors (you might need to adjust the radius)
    places = gmaps.places_nearby(location=(latitude, longitude), radius=1000, type='doctor')

    # Extract doctors' locations
    doctors_locations = [(place['name'], place['geometry']['location']['lat'], place['geometry']['location']['lng']) for place in places['results']]

    return doctors_locations

# Create Gradio interface
def nearest_doctors(location):
    doctors_locations = find_nearest_doctors(location)
    
    # Generate HTML for Google Maps display
    map_html = f"<iframe width='600' height='500' src='https://maps.google.com/maps?q={location}&output=embed'></iframe>"

    # Add markers for doctors on the map
    for doctor in doctors_locations:
        map_html += f"<p>{doctor[0]}</p><iframe width='600' height='500' src='https://www.google.com/maps/embed/v1/place?q={doctor[1]},{doctor[2]}&key=YOUR_API_KEY'></iframe>"

    return map_html

# Create Gradio interface
iface = gr.Interface(fn=nearest_doctors, 
                      inputs="text", 
                      outputs="html",
                      title="Find Nearest Doctors",
                      description="Enter your location to find nearest doctors.")
iface.launch(share=True)
