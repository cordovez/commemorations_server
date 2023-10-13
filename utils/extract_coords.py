from Models.Plaque import Coordinates


def extract_coordinates(item):
    coords = item["xy"]
    if coords:
        lon = coords["lon"]
        lat = coords["lat"]

        new_coordinates = Coordinates(lon=lon, lat=lat)
        return new_coordinates
