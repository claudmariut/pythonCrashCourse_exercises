# Modifying a list ina function. Using functions.
def print_models(unprinted_designs_list, completed_models_list):
    """Simulate printing each design, until none are left. Move each design to
    completed_models after printing"""
    while unprinted_designs_list:
        current_design = unprinted_designs_list.pop()
        print(f"Printing model: {current_design}")
        completed_models_list.append(current_design)


def show_completed_models(completed_models_list):
    """Show all models that were printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models_list:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Once the first function is executed, it modifies the the lists.
# Notice that we have passed a copy of the original list.
print_models(unprinted_designs[:], completed_models)
# If we only execute the second function, then the list is empty.
show_completed_models(completed_models)
print(unprinted_designs)






