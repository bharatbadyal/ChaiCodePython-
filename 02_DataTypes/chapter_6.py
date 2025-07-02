# Strings : Immutable
from builtins import print
chai_type = "Ginger Chai"
customer_name= "Priya"

print(f"The order for {customer_name} : {chai_type} please!...")

chai_discription = "Aromatic and Bold"
print(f"The first letter is: {chai_discription[:8]}")
print(f"The last letter is: {chai_discription[12:]}")

# Encoding and decoding "Especially for the forign character very distinctive to normal code"

label = "Nothing Special ČÐǏÆ"
print(label)

encoded_label = label.encode("utf-8")
print(encoded_label)

decoded_label = encoded_label.decode("utf-8")
print(decoded_label)