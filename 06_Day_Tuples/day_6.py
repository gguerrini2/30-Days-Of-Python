# Exercises: Level 1
# Create an empty tuple
tpl = ()
# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Gabriele',)
sisters = ('Bruna',)
# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters
print(siblings)
# How many siblings do you have?
print('I have ', len(siblings), 'siblings. ')
# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ('Gianfranco', 'Lucia',)
family_members = siblings + parents
print('My family members: ', family_members)
# Exercises: Level 2
# Unpack siblings and parents from family_members
gabriele = family_members[0]
print(gabriele)
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal = ('parrot', 'dog', 'cat', 'monkey', 'donkey', 'raccoon')
product = ('pasta', 'bread', 'pie', 'bottle')
food_stuff_tp = fruits+vegetables+animal+product
# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_item = food_stuff_tp[len(food_stuff_tp) // 2]
# Slice out the first three items and the last three items from food_stuff_lt list
border_items = food_stuff_tp[:4] + food_stuff_tp[-3:]
# Delete the food_stuff_tp tuple completely
del food_stuff_tp
# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
print('Estonia' in nordic_countries)
# Check if 'Iceland' is a nordic country
print('Iceland' in nordic_countries)