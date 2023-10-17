""" 
Utility function to separate name parts
"""
import re


def match_for_names(item):
    """
    Takes a name in the format 'Juan Carlos CORDOVEZ-MANTILLA' and returns the
    name in two parts: first_name: Juan Carlos, last_name: Cordovez-Mantilla
    """
    pattern = r"(?=(?P<first_name>[A-Z][a-zÀ-ÿ-]+(?: [A-Z][a-zÀ-ÿ-]+)*)\s(?P<last_name>[A-Z]+)$)"

    match = re.search(pattern, item["commemore"])
    return match
