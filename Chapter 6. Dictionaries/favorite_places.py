favorite_places = {
    'mina': ['junto a mi', 'playa'],
    'clau': ['junto a ella', 'montana'],
    'pepito': ['cocina', 'cama'],
    }

del favorite_places['pepito']

for name, favorite_place in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are: ")
    for place in favorite_place:
        print(f'\t{place.title()}')
