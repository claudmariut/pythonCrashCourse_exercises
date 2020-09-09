# 1
def make_sandwich(*ingredients):
    """Display a summarize with the order"""
    print("\nMaking a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")


make_sandwich('tuna', 'cheese', 'tomatoes')
make_sandwich('chicken', 'provolone', 'lettuce')
make_sandwich('veggie patties', 'cheddar', 'guacamole')


# 2
def make_car(message, manufacturer, model, **kwargs):
    """Build a dictionary with the car information"""
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    for key, value in kwargs.items():
        print(f"{key.title()} = {value}")


make_car('subaru', 'outback', color='blue', tow_package=True)
