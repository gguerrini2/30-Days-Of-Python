#Day 2: 30 Days of python programming

"""
Exercises: Level 1
Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
Write a python comment saying 'Day 2: 30 Days of python programming'
Declare a first name variable and assign a value to it
Declare a last name variable and assign a value to it
Declare a full name variable and assign a value to it
Declare a country variable and assign a value to it
Declare a city variable and assign a value to it
Declare an age variable and assign a value to it
Declare a year variable and assign a value to it
Declare a variable is_married and assign a value to it
Declare a variable is_true and assign a value to it
Declare a variable is_light_on and assign a value to it
Declare multiple variable on one line
"""

name = "Giuseppe";
last_name = "Guerrini";
full_name = "Giuseppe Guerrini";
country = "Italy";
city = "Serramanna";
age = 22;
year = 2026;
is_married = False;
is_true = True;
is_light_on = True;
name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on = 'Giuseppe', 'Guerrini', 'Giuseppe Guerrini', 'Italy', 'Serramanna', 22, 2026, False, True, False;

"""
Exercises: Level 2
Check the data type of all your variables using type() built-in function
Using the len() built-in function, find the length of your first name
Compare the length of your first name and your last name
Declare 5 as num_one and 4 as num_two
Add num_one and num_two and assign the value to a variable total
Subtract num_two from num_one and assign the value to a variable diff
Multiply num_two and num_one and assign the value to a variable product
Divide num_one by num_two and assign the value to a variable division
Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
Calculate num_one to the power of num_two and assign the value to a variable exp
Find floor division of num_one by num_two and assign the value to a variable floor_division
The radius of a circle is 30 meters.
Calculate the area of a circle and assign the value to a variable name of area_of_circle
Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
Take radius as user input and calculate the area.
Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
"""

print(type(name));
print(type(last_name));
print(type(full_name));
print(type(country));
print(type(city));
print(type(age));
print(type(year));
print(type(is_married));
print(type(is_true));
print(type(is_light_on));

print(len(name));
print("Name lenght: ", len(name), ", Last name lenght: ", len(last_name));

num_one=5;
num_two=4;
total = num_one + num_two;
diff = num_one - num_two;
product = num_one * num_two;
division = num_one / num_two;
reamainder = num_one % num_two;
exp = num_one ** num_two;
floor_division = num_one // num_two;

r = 30;
area_of_circle = 3.14 * (r**2);
circum_of_circle = 3.14*r*2;
print(area_of_circle, circum_of_circle);

r= int(input("Insert the radius lenght"));
area_of_circle = 3.14 * (r**2);
circum_of_circle = 3.14*r*2;
print(area_of_circle, circum_of_circle);

#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
name = input("Insert your name ");
last_name = input("Insert your last name ");
country= input("Insert your country ");
age = input("Insert your age ");
print(name, last_name, country, age);

help('keywords');