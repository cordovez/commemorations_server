"""
Extract arrondissement and city
"""
import re


def extract_arrondissement_and_city(item):
    """
    Function extracts arrondissement and city from original address string"""
    pattern = r"(\d{5})\sParis"

    match = re.search(pattern, item)
    details = {}
    if match:
        details["arrondissement"] = match.group(1)
        details["city"] = match.group(2)
        return details
    else:
        return None
