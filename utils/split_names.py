""" 
Utility function to separate name parts"""
import re


def match_for_names(item):
    """
    Takes a name in the format 'Juan Carlos CORDOVEZ-MANTILLA' and returns the
    name in two parts: first_name: Juan Carlos, last_name: Cordovez-Mantilla
    """
    pattern = r"(?=(?P<first_name>[A-Z][a-zÀ-ÿ-]+(?: [A-Z][a-zÀ-ÿ-]+)*)\s(?P<last_name>[A-Z]+)$)"
    # pattern = (
    #     r"(?=(?P<first_name>[A-Z][a-z]+(?:-[A-Z][a-z]+)*)\s(?P<last_name>[A-Z]+)$)"
    # )

    # pattern = r"(?=(?P<first_name>[A-Z][a-z]+(?:-[A-Z][a-z]+)*)\s(?P<last_name>[A-Z]+))"

    # pattern = r"(?=(?:[A-Z][a-z]+(?:-[A-Z][a-z]+)* [A-Z]+))"
    # pattern = r"([A-Z][a-z]+(?: [A-Z][a-z]+)*)\s([A-Z-]+)"

    match = re.search(pattern, item["commemore"])
    return match
    # name = {}
    # if match:
    #     name["first_name"] = match.group(1)
    #     name["last_name"] = match.group(2)

    # return name
