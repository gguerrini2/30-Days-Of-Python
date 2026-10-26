# Exercises: Level 1
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive.
# If below 18 give feedback to wait for the missing amount of years. Output:
"""
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.
"""

age = int(input("Enter your age "))
if age >= 18:
    print("You are old enough to drive")
else:
    print("You need ", 18 - age, "year to drive")

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
"""
# Enter your age: 30
# You are 5 years older than me.
"""
my_age = 22
your_age = int(input("Enter your age: "))
if your_age > my_age:
    if your_age == my_age + 1:
        print("You are 1 year older than me. ")
    else:
        print("You are ", your_age - my_age, "older than me.")
elif your_age < my_age:
    if your_age == my_age - 1:
        print("You are 1 year younger than me")
    else:
        print("You are ", my_age - your_age, "younger than me")
else:
    print("We have the same age")

# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
"""
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
"""
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print(a, "is greather than ", b)
elif a < b:
    print(a, "is smaller than", b)
else:
    print(a, "is equal than ", b)

# Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:
"""
# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F
# ```
"""
score = int(input("Enter your score "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
# Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn.
# December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = str(input("Enter the month")).capitalize()
if month == "September" or month == "October" or month == "November":
    print("Autumn")
elif month == "December" or month == "January" or month == "Febraury":
    print("Winter")
elif month == "March" or month == "April" or month == "May":
    print("Spring")
elif month == "June" or month == "July" or month == "August":
    print("Summer")
else:
    print("Not valid month")

# The following list contains some fruits:
fruits = ["banana", "orange", "mango", "lemon"]
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruit = input("Insert a fruit").lower()
if fruit not in fruits:
    fruits.append(fruit)
    print("New list: ", fruits)
else:
    print("That fruit already exist in the list ")


# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!
person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_married": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if(person["skills"] is not []):
    print(person["skills"][len(person["skills"]) // 2])
else:
    print('Skill issue') 
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if(person["skills"] is not []):
    if('Python' in person['skills']):
        print(True)
else:
    print(False) 
#If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
#if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if(person['skills'] == ['Javascript', 'React'] or person['skills'] == ['React', 'Javascript']):
    print('He \'s a front end developer')
elif(['Node', 'Python', 'MongoDB'] in person["skills"]):
    print('He \'s a backend developer ' )
elif(['React', 'Node', 'MongoDB'] in person["skills"]):
    print('He \'s a fullstack developer')
else: 
    print('unknown title')
    
#  * If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.
if(person["is_married"] == True and person["country"] == 'Finland'):
    print('Asabeneh Yetayeh lives in Finland. He is married.')