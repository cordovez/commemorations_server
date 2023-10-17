from Models.Plaque import Commemoration


def fill_commemorant(name_match, plaque):
    """Function takes a regex match and split the name into two parts if a
    match exists, otherwise the information is saved in 'other'"""
    if name_match:
        first = name_match.group("first_name")
        last = name_match.group("last_name").capitalize()
        commemorant = Commemoration(first_name=first, last_name=last)

    else:
        entry_no_upper = plaque["commemore"].title()
        commemorant = Commemoration(other=entry_no_upper)

    return commemorant
