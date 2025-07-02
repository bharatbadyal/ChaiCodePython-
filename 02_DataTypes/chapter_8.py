# list (mutable data type)
from builtins import print
ingrediants =["water", "milk","blackTea"]
ingrediants.append("sugar")
print(f"Ingreiants are : {ingrediants}")

removed_ingrediant = ingrediants.remove("water")
print(f"Ingrediant removed by using .remove method is: {removed_ingrediant}")
print(ingrediants)

spices_options = ["ginger, Cardamom"]
chai_ingrediant =["Water", "Milk"]

# to add two lists
chai_ingrediant.extend(spices_options)
print(f"The chai: {chai_ingrediant}")