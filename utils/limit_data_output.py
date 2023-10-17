"""Developer's tools for handling response data
"""


def limit_data_output(data_list):
    """
    Function is used by the developer of this api to inspect names
    using a smaller response output, by excluding some common values"""

    list_of_exlcludes = [
        "Liberation De Paris",
        "Eleves De Ces Ecoles Morts En Déportation Parce Que Nés Juifs",
        "Comite Parisien De La Liberation",
    ]
    response_data = []
    for plaque in data_list:
        commemoration_text = plaque.commemorates.other

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

    return response_data
