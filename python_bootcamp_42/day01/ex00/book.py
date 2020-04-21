
# cookbook = {
#         name: [last_update, creation_date,
#         {recipe_type : [cooking_lvl, cooking_time, ingredients, descriptions] }]
# }

cookbook = {
    'Apple Pie': [12-10-2020, 12-09-2020, {'dessert': [2, 60, ['apple'], "descriptions"]}]
}


class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = recipes_list

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        pass

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        for key in cookbook.keys():
            if key is recipe_type:

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        pass
