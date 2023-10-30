"""Original record URL
    """


def get_original_record_url(original_id):
    """Function creates url string that points to original record

    Args:
        original_id (int): "identifiant" in the original record

    Returns:
        str: url
    """
    base_url = "https://opendata.paris.fr/"
    api_url = (
        "/api/explore/v2.1/catalog/datasets/plaques_commemoratives_1939-1945/records"
    )
    params = f"?where=identifiant%20%3D{original_id}&limit=1"
    original_record = base_url + api_url + params

    return original_record
