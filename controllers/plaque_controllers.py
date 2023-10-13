import json
import re

from Models.Plaque import Commemoration, Plaque
from utils.arr_and_city import extract_arrondissement_and_city
from utils.extract_coords import extract_coordinates
from utils.split_names import match_for_names


def plaques_in_english(data):
    new_plaques_list = []

    for plaque in data:
        coords = extract_coordinates(plaque)
        match = match_for_names(plaque)
        if match:
            first = match.group("first_name")
            last = match.group("last_name").capitalize()
            commemorant = Commemoration(first_name=first, last_name=last)
        else:
            entry_no_upper = plaque["commemore"].title()
            commemorant = Commemoration(other=entry_no_upper)

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

        values = {
            "commemorates": commemorant,
            "street_address": street_address,
            "arrondissement": plaque["empty"],
            "city": city,
            "address_complement": complementary_info,
            "coordinates": coords,
            "original_id": plaque["identifiant"],
        }
        new_plaque = Plaque(**values)
        new_plaques_list.append(new_plaque)
    sorted_list = sorted(new_plaques_list, key=lambda x: x.original_id)

    # return sorted_list

    # FOR DEVELOPER USE
    # Create a list of PlaqueResponseModel instances with only the "commemorates" field,
    # excluding some
    list_of_exlcludes = [
        "Liberation De Paris",
        "Eleves De Ces Ecoles Morts En Déportation Parce Que Nés Juifs",
        "Comite Parisien De La Liberation",
    ]
    response_data = []
    for plaque in sorted_list:
        commemoration_text = (
            plaque.commemorates.other
        )  # Assuming "other" contains the commemoration text

        if (
            commemoration_text not in list_of_exlcludes
            and plaque.commemorates.other is not None
        ):
            response_data.append(
                {
                    "id": plaque.original_id,
                    "commemorates": plaque.commemorates,
                }
            )
            # response_data = [
            #     {
            #         "id": plaque.original_id,
            #         "commemorates": plaque.commemorates.other,
            #     }
            #     for plaque in sorted_list
            # ]
    return response_data  # len =265
