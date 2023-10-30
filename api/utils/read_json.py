""" Function to read data saved as JSON"""
import json


def read_json_data():
    """Reads plaques data from a JSON file"""
    with open("Data/plaques.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        return data
