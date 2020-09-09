# Using arbitrary keyword arguments. **kwargs creates a dictionary.
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    for key, word in user_info.items():
        print(f"{key.title()} = {word.title()}")


build_profile("claudiu", "mariutanu", location="hot springs",
              field="computer science", status="unmarried")
