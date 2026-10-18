"""
Declare your age as integer variable
Declare your height as a float variable
Declare a variable that store a complex number
Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
    Enter base: 20
    Enter height: 10
    The area of the triangle is 100
Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12
Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
Calculate the slope, x-intercept and y-intercept of y = 2x -2
Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
Compare the slopes in tasks 8 and 9.
Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
Find the length of 'python' and 'dragon' and make a falsy comparison statement.
"""

age = 22;
height = 170.00;
complex_number = 1 + 1j;

base = float(input('Enter base '));
height = float(input('Enter height '));
print('The area of the triangle is ', 0.5 * base * height);

side_a = float(input('Enter side a '));
side_b = float(input('Enter side b '));
side_c = float(input('Enter side c '));
print('The perimeter of the triangle is ', side_a+side_b+side_c);

lenght = float(input('Enter lenght '));
width = float(input('Enter width '));
print('The perimeter is ', lenght+width, ', The area is ', lenght*width);

r = float(input('Enter radius '));
pi = 3.14;
print('The area is ', pi*r*r, 'The circumference is ', 2*pi*r);

#y = 2x -2
x_intercept = (2+0) / 2;
y_intercept = (-2+0);
#point 1 = (1, 0) point 2 = (0, -2)
m8 = (-2 - 0) / (0 - 1);
print('y = 2x-2 intercepts x in ', x_intercept, 'intercepts y in ', y_intercept, ' and his slop is ', m8);

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
m9 = (10 - 2) / (6 - 2);
euclidian_distance = (2-2)**2 + (10-6)**2;
print('Slop between (2,2) and (6,10): ', m9, ', Euclidian distance: ', euclidian_distance);

print(m8 > m9);

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
(-3)**2 + 6*(-3) + 9 == 0;

print(len('dragon') > len('python'));

"""
Use and operator to check if 'on' is found in both 'python' and 'dragon'
I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
There is no 'on' in both dragon and python
Find the length of the text python and convert the value to float and convert it to string
Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
Check if type of '10' is equal to type of 10
Check if int('9.8') is equal to 10
Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120
Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
Enter number of years you have lived: 100
You have lived for 3153600000 seconds.
Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""
print('on' in 'python' and 'on' in 'dragon');
print('jargon' in 'I hope this course is not full of jargon');
print('on' not in 'python' and 'on' not in 'dragon');
str(float(len('python')));
8 % 2 == 0;
int(2.7) == (7 // 3);
type('10') == type(10);
int(9.8) == 10;

hours = input('Enter hours ');
rate_per_hour = input('Enter rate per hour ');
print('Your weekly earning is ', hours*rate_per_hour);

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input('Enter the number of years '));
seconds = (100 - years) * 365 * 24 * 60 * 60;
print(seconds);

"""
Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""
print('1', '1', '1', '1', '1');
print('2', '1', '2', '4', '8');
print('3', '1', '3', '9', '27');
print('4', '1', '4', '16', '64');
print('5', '1', '5', '25', '125');