# list (mutable data type)
from builtins import print
ingrediants =["water", "milk","blackTea"]
ingrediants.append("sugar")
print(f"Ingreiants are : {ingrediants}")

removed_ingrediant = ingrediants.remove("water")
print(f"Ingrediant removed by using .remove method is: {removed_ingrediant}")
print(ingrediants)

spices_options = ["ginger", "Cardamom"]
chai_ingrediant =["Water", "Milk"]

# to add two lists
chai_ingrediant.extend(spices_options)
print(f"The chai: {chai_ingrediant}")
chai_ingrediant.insert(2,"black Tea")
print(f"chai:{chai_ingrediant}")

last_added = chai_ingrediant.pop()
print(chai_ingrediant)
print(last_added)

chai_ingrediant.reverse()
print(chai_ingrediant)

chai_ingrediant.sort()
print(chai_ingrediant)

sugar_levels=[1,2,3,4,5]
print(f"Maximum Sugar Level: {max(sugar_levels)}")
print(f"Minimum Sugar Level: {min(sugar_levels)}")

# bytearray and Operater Overloading in Python
base_liquid = ["Water","Milk"]
extra_flavour = ["Ginger"]

full_liquid_mix = base_liquid + extra_flavour
print(f"Liquid mix: {full_liquid_mix}")