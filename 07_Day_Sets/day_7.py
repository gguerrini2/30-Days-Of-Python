# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# Exercises: Level 1
# Find the length of the set it_companies
print(len(it_companies))
# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies);
# Insert multiple IT companies at once to the set it_companies
it_companies.update(['CISCO', 'Meta']);
print(it_companies)
# Remove one of the companies from the set it_companies
it_companies.remove('CISCO');
print(it_companies)
# What is the difference between remove and discard
# remove() raises errors, discard() doesn't

# Exercises: Level 2
# Join A and B
C = A.union(B);
print(C);
# Find A intersection B
int = A.intersection(B)
print(int)
# Is A subset of B
print('A is a subset of B: ', A.issubset(B));
# Are A and B disjoint sets
print('A and B are disjoint sets: ', A.isdisjoint(B));
# Join A with B and B with A
AjB = A.union(B)
BjA = B.union(A)
# What is the symmetric difference between A and B
sym = A.symmetric_difference(B)
print(sym)
# Delete the sets completely
del A

# Exercises: Level 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages = set(age)
print('List len', len(age), 'Set len', len(ages))
# Explain the difference between the following data types: string, list, tuple and set
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people';
print('Number of unique words: ', len(set(sentence)));