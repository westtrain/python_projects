from book import Book
from recipe import Recipe

des = "3 pounds mixed apples (such as Granny Smith, Gala and McIntosh) 2/3 cup granulated sugar 2 tablespoons fresh lemon juice 6 tablespoons unsalted butter 1 tablespoon all-purpose flour, plus more for dusting 3/4 teaspoon ground cinnamon 1/8 teaspoon salt 2 disks dough for Basic Crust  1 large egg, beaten"
pie = Recipe("Apple Pie", 1, 30, "a Apple, suger", des, "starter")
salad = Recipe("Salad", 2, 10, "freah vegis", "starter")
pizza = Recipe("Pizza", 4, 60, "cheese, dough, peperoni", "lunch")
stake = Recipe("Staek", 5, 120, "beef, butter", "lunch")
cake = Recipe("Chocolet Cake", 3, 50, "chocolet, suger, cream", "dessert")
to_print = str(pie)
print(to_print)
to_print = str(salad)
print(to_print)
to_print = str(pizza)
print(to_print)
to_print = str(stake)
print(to_print)
to_print = str(cake)
print(to_print)
