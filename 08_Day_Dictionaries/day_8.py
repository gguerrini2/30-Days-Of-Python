# Create an empty dictionary called dog
dog = dict()
# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Bilbo';
dog['color'] = 'B/N'
dog['legs'] = 4
dog['age'] = 5
print(dog)
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'first_name':'Giuseppe', 'last_name':'Guerrini', 'gender':'male', 'age':22, 'marital status':False, 'skills':['Python', 'C', 'HTML'], 'country':'Italy', 'city':'Serramanna',  'address':'John Rambo Avenue'}
# Get the length of the student dictionary
print(len(student))
# Get the value of skills and check the data type, it should be a list
print(student['skills'])
# Modify the skills values by adding one or two skills
student['skills'].append('Java');
print(student['skills'])
# Get the dictionary keys as a list
print(student.keys())
# Get the dictionary values as a list
print(student.values())
# Change the dictionary to a list of tuples using items() method
st_lst = student.items()
print(st_lst)
# Delete one of the items in the dictionary
del student['skills']
print(student)
# Delete one of the dictionaries
del student