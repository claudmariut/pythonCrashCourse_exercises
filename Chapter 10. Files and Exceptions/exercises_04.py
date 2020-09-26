import json


def get_new():
    """Gets favorite number from input"""
    favorite_num = input("What is your favorite number? ")
    return favorite_num


def return_favorite():
    """Return favorite number from file or new"""
    filename = "text_files/favorite_num.json"
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        favorite_number = get_new()
        return favorite_number
    else:
        return favorite_number


def print_number():
    print(f"Your favorite number is {return_favorite()}!")


print_number()



