"""method to merge two dictionaries using the dict() constructor 
with the union operator (|)"""


def merge(dict1, dict2):
    """create a new dictionary by merging the items of the two dictionaries using the union operator (|)"""
    merged_dict = dict(dict1.items() | dict2.items())
    # return the merged dictionary
    return merged_dict
