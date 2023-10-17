"""Plaque controllers"""

from Models.Plaque import Plaque
from utils.add_name_to_commemoration import fill_commemorant
from utils.extract_coords import extract_coordinates
from utils.original_record import get_original_record_url
from utils.regex_for_names import match_for_names


def plaques_in_english(data):
    """Returns a new list of all plaques reformatted and with english-language
    keys, sorted by increasing original_id"""
    new_plaques_list = []

    for plaque in data:
        coords = extract_coordinates(plaque)
        match = match_for_names(plaque)
        commemorant = fill_commemorant(match, plaque)

        if plaque["precision_adresse"] == "NULL":
            complementary_info = None

        else:
            complementary_info = plaque["precision_adresse"]

        street_address = (
            plaque["adresse_complete"][:-12] if plaque.get("adresse_complete") else None
        )
        city = (
            plaque["adresse_complete"][-5:] if plaque.get("adresse_complete") else None
        )
        record_url = get_original_record_url(int(plaque["identifiant"]))
        values = {
            "commemorates": commemorant,
            "street_address": street_address,
            "arrondissement": plaque["empty"],
            "city": city,
            "address_complement": complementary_info,
            "coordinates": coords,
            "original_id": plaque["identifiant"],
            "original_record": record_url,
        }
        new_plaque = Plaque(**values)
        new_plaques_list.append(new_plaque)
    sorted_list = sorted(new_plaques_list, key=lambda x: x.original_id)

    return sorted_list
