# basic operation on numbers + - * / , // for removing decimal

from builtins import print
total_tea_bags = 7
serving = 4
bags_per_pot = total_tea_bags//serving  # // will remove .00 decimal from answer 
print(f"The total bags per tea Pot are: {bags_per_pot}")  

# to get the reminder we use % operator in python 
total_caramom_Pots = 10
pots_per_cup = 3
leftover_pots = total_caramom_Pots % pots_per_cup
print(f"The total no of leftover pots are: {leftover_pots}")

# Use of exponential ** 
base_flavour_strength = 2
scale_flavor = 3
powerfull_flavour = base_flavour_strength**scale_flavor
print(f"Scaled Flavour Strength : {powerfull_flavour}")

# For readability puspouse 
tea_leaves = 1_000_000_000
print(tea_leaves)