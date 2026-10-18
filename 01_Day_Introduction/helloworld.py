# Day 1 - 30DaysOfPython Challenge

print(3+4);
print(3-4);
print(3*4);
print(3%4);
print(3/4);
print(3**4);
print(3//4);

print("Giuseppe")
print("Guerrini")
print("Italy")

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland'])) #list
print(type("Giuseppe"))
print(type("Guerrini"))
print(type("Italy"))

"""
Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
Find an Euclidean distance between (2, 3) and (10, 8)
"""

print(type(1)); #integer
print(type(1.1));   #float
print(type(1 + 1j));    #complex
print(type("Uno")); #string
print(type(True));  #boolean
print(type(['Primo', 'Secondo', 1]));   #list
print(type((1, 3)));    #tuple
print(type({1, 3}));    #set
print(type({"1": "uno", "2": "due"}));  #dictionary

#Euclidian distance on 2D is calculated with d(p, q) = (q1-p1)^2 + (q2-p2)^2
d = (10-2)**2 + (8-3)**2;
print("Euclidian distance between p and q: ", d);