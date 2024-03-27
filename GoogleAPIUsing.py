import googlemaps
import os

API_KEY = os.getenv('GOOGLEMAPS_API_KEY')

def search_places(query):
    gmaps = googlemaps.Client(key=API_KEY)
    places = gmaps.places(query)
    return places['results']

def get_place_details(place_id):
    gmaps = googlemaps.Client(key=API_KEY)
    place_details = gmaps.place(place_id, fields=['name', 'formatted_address', 'rating', 'reviews', 'opening_hours'], reviews_no_translations=True, reviews_sort='most_relevant')
    return place_details['result']