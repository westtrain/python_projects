cookbook = {
    'sandwich': {
        'ingredients': ["ham", "bread", "cheese", "tomatoes"],
        'meal': 'lunch',
        'prep_time': '10 minutes'
    },
    'cake': {
        'ingredients': ["ﬂour", "sugar", "eggs"],
        'meal': 'dessert',
        'prep_time': '60 minutes'
    },
    'salad': {
        'ingredients': ["avocado", "arugula", "tomatoes", "spinach"],
        'meal': 'lunch',
        'prep_time': '15 minutes'
    }
}


def print_recipe(name):
    print(f"Recipe for {name}")
    print(f"Ingredients list: {cookbook[name]['ingredients']}")
    print(f"To be eatan for {cookbook[name]['meal']}.")
    print(f"Takes {cookbook[name]['prep_time']} of cooking.")
    # for i in cookbook[name].values():
    #     print(i)


def delete_recipe(name):
    del cookbook[name]


def add_recipe(name, ingreds, meal_type, time):
    tmp = {
        name: {
            "ingredients": ingreds,
            "meal": meal_type,
            "prep_time": time
        }
    }
    cookbook.update(tmp)


def print_recipe_name():
    for i in cookbook.keys():
        print(f"Try to cooking \'{i}\' by yourslef right now")


while(True):
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a receipe")
    print("4: Print a cookbook")
    print("5: Quit")
    user_input = input()
    if user_input == '1':
        print()
        print("Please enter the new recipe's name:")
        name = input()
        print("Please enter the new recipe's ingredients:")
        ingreds = input()
        print("Please enter the new recipe's meal type:")
        meal_type = input()
        print("Please enter the new recipe's preparation time:")
        time = input()
        print()
        add_recipe(name, ingreds, meal_type, time)
        print()
    elif user_input == '2':
        print()
        print("Please enter the recipe's name to delete:")
        del_name = input()
        print()
        delete_recipe(del_name)
        print()
    elif user_input == '3':
        print()
        print("Please enter the recipe's name to print:")
        name = input()
        print()
        print_recipe(name)
        print()
    elif user_input == '4':
        print()
        print_recipe_name()
        print()
    elif user_input == '5':
        print()
        print("Cookbook closed.")
        break
    else:
        print()
        print("This option doesn't exist, pleaes type the corresponding number.")
        print("To exit, enter 5")
        print()
