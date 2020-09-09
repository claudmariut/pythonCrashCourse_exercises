cities = {
    'zaragoza': {
        'country': 'spain',
        'population': '1 million',
        'fact': 'It has a nice river',
        },

    'hot springs': {
        'country': 'usa',
        'population': '37 thousand',
        'fact': 'Here is where I met my girlfriend'
        },

    'destin': {
        'country': 'usa',
        'population': '14 thousand',
        'fact': 'Here is where I went on summer vacation 2020',
        },
    }

for city, city_info in cities.items():
    print(f"\n{city.title()}:")
    print(f"\tThis city is in {city_info['country']}")
    print(f"\tThe population of this city is: {city_info['population']}")
    print(f"\tAn fact about this city is: {city_info['fact']}")
