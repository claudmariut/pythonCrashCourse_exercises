def get_city_country(city, country, population=''):
    """Return a neatly formatted city and its country."""
    if population:
        formatted_out = f"{city}, {country} - population {population}"
    else:
        formatted_out = f"{city}, {country}"
    return formatted_out.title()

