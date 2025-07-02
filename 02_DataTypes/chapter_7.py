# Tuples 
from builtins import print
masala_spices = ("cardamom","cloves","cinnamon")
(spice1,spice2,spice3)=masala_spices
print(f"The spices we have : {spice1},{spice2},{spice3}")
print(f"Is cinnamon in masala Spices? {'cinnamon' in masala_spices}")  # membership testing 
# swaping the variables done by the help of tuple behind the scene
# swapping of varibles in python

ginger_ratio, cardamom_ratio = 2,1
print(f"Ginger = {ginger_ratio}, Cardamom = {cardamom_ratio}")

ginger_ratio,cardamom_ratio = cardamom_ratio,ginger_ratio
print(f"Ginger = {ginger_ratio}, Cardamom = {cardamom_ratio}")
