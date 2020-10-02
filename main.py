import datetime
import os

import pygeohash
from custom_types import RecordType
from geopy.geocoders import Nominatim
from get_item import search_nearby

APP_USER_AGENT = "EnviroJusticeLeague"
METERS_PER_MILE = 1609.34

# Free for casual use, powered by Open Street Maps
# https://nominatim.org/
geolocator = Nominatim(user_agent=APP_USER_AGENT)


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def find(user_input, record_type):
    place = geolocator.geocode(user_input)
    geohash = pygeohash.encode(latitude=place.latitude, longitude=place.longitude)
    return [
        r
        for r in search_nearby(geohash, record_type)
        if r["distance_to_search"] / METERS_PER_MILE <= 25
    ]


def display_businesses(results):
    for r in results:
        mi_dist = r["distance_to_search"] / METERS_PER_MILE
        name = r["payload"]["name"]

        print(f"{name} - {mi_dist:.1f} mi away")
        print(f"    {r['payload']['description']}")
        print(f"    {r['payload']['website']}")
        print()


def display_events(results):
    for r in results:
        mi_dist = r["distance_to_search"] / METERS_PER_MILE
        start = datetime.datetime.fromtimestamp(r["payload"]["start_time"])
        start_str = start.strftime("%b %-d")
        name = r["payload"]["name"]

        print(f"{name}, {start_str}")
        print(f"    {r['payload']['description']}")
        print(f"    {mi_dist:.1f} mi away")
        print()


def main():
    print("Welcome to the Enviro-Justice League!")
    input("Press Enter to continue...")
    menu = {
        "Businesses": {"category_view": "(B)usiness"},
        "Events": {"category_view": "(E)vents"},
    }
    while True:
        clear()
        try:
            categories = ", ".join([m["category_view"] for m in menu.values()])
            record_type = input(f"Pick a category: {categories}: ")

            if record_type.lower() == "b":
                clear()
                print("Find businesses near you")
                print()

                user_input = input("Location: ")

                results = find(user_input, RecordType.business.value)
                if len(results):
                    print(f"Found {len(results)} businesses")
                    display_businesses(results)
                else:
                    print("We don't have any data on eco-friendly businesses near you")
                    print("Why not start one!")
            elif record_type.lower() == "e":
                clear()
                print("Find events near you")
                print()

                user_input = input("Location: ")

                results = find(user_input, RecordType.event.value)

                if len(results):
                    print(f"Found {len(results)} events")
                    display_events(results)
                else:
                    print("Couldn't find anything upcoming nearby")
                    print("Why not check out some virtual events!")
            elif record_type.lower() == "q":
                break
            else:
                clear()
                print(
                    "Opps that's not a valid category. Press Q to quit from main menu"
                )
            print()
            input("Press Enter to return to main menu...")
        except KeyboardInterrupt:
            break
    print("Goodbye!")


main()
