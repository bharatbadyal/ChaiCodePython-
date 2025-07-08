essential_spices = {"cardamom","ginger","cinnamon"}
optional_spices ={"cloves","ginger","black pepper"}

all_spices = essential_spices|optional_spices   
print(f"All spices available: {all_spices}")

common_spices =essential_spices & optional_spices
print(f"Common_spices: {common_spices}")

only_in_essential = essential_spices-optional_spices
print(only_in_essential)

print("cloves" in optional_spices)