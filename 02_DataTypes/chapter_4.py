# Boolean

is_boiling = True 
stri_count = 5 
total_action = stri_count+ is_boiling  # upcasting simmilar to typecasting in JavaScript (just fancy namings)
print(f"Total actions: {total_action}")

# also can print the boolean representation using bool() funciton;
milk_present = 0
print(f"is there any milk? {bool(milk_present)}")

# Logical operations: and , or , not

water_hot = True  
tea_added = False
can_serve_tea = water_hot and tea_added
print(f"Can serve Tea? {can_serve_tea}")