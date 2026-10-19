#1 Declare an empty list
lst = [];
# Declare a list with more than 5 items
lst = [1, 2, 3, 4, 5, 6, 7]
# Find the length of your list
print(len(lst));
# Get the first item, the middle item and the last item of the list
print(lst[0], lst[int(len(lst)/2)], lst[-1])
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Giuseppe', 22, 170, False, 'Via Carducci'];
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'];
# Print the list using print()
print(it_companies);
# Print the number of companies in the list
print(len(it_companies))
# Print the first, middle and last company
print(it_companies[0], it_companies[int(len(it_companies)/2)], it_companies[-1])
# Print the list after modifying one of the companies
it_companies[0] = 'Baseball AI'
print(it_companies)
# Add an IT company to it_companies
it_companies.append('Jiji AI')
# Insert an IT company in the middle of the companies list
it_companies.insert(4, 'Rino AI')
print(it_companies)
# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[2] = it_companies[2].upper();
print(it_companies);
# Join the it_companies with a string '#;  '
it_companies = it_companies + ['#; ']
print(it_companies)
# Check if a certain company exists in the it_companies list.
print('Baseball AI' in it_companies)
# Sort the list using sort() method
it_companies.sort()
print(it_companies);
# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)
# Slice out the first 3 companies from the list
first_3 = it_companies[:4]
print(first_3)
# Slice out the last 3 companies from the list
last_3 = it_companies[-3:]
print(last_3)
# Slice out the middle IT company or companies from the list
middle_2 = it_companies[4:6]
print(middle_2)
# Remove the first IT company from the list
it_companies.pop(0);
print(it_companies)
# Remove the middle IT company or companies from the list
it_companies.pop(4)
it_companies.pop(5)
print(it_companies)
# Remove the last IT company from the list
it_companies.pop()
print(it_companies)
# Remove all IT companies from the list
it_companies.clear()
print(it_companies)
# Destroy the IT companies list
del it_companies;
# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
join = front_end + back_end
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = join.copy();

# Exercises: Level 2
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort()
print('Minimum age: ', ages[0], 'Maximum age: ', ages[-1]);
# Add the min age and the max age again to the list
ages.insert(0, ages[0])
ages.insert(-1, ages[-1]);
# Find the median age (one middle item or two middle items divided by two)
print((ages[6] + ages[7])/2)
# Find the average age (sum of all items divided by their number )
print(sum(ages)/len(ages))
# Find the range of the ages (max minus min)
print('Range of ages: ', ages[-1] - ages[0])
# Compare the value of (min - average) and (max - average), use abs() method
min, avg, max = ages[0], sum(ages)/len(ages), ages[-1]
print('Min - average: ', abs(min -  avg), 'Max - average: ', abs(max - avg)) 
# Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];
print(countries)
print(len(countries))
print(countries[len(countries) // 2 - (len(countries) % 2 + 1) % 2 : len(countries) // 2 + 1])
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_half = countries[:len(countries) // (2 - (len(countries) % 2 + 1) % 2) + 1];
print(first_half,'\n', len(first_half));
second_half = countries[len(countries) // 2 + 1:];
print(second_half,'\n', len(second_half));
print(first_half + second_half == countries);
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
country1, country2, country3, *scandic = countries[countries.index('China')], countries[countries.index('Russia')], countries[countries.index('United States')], countries[countries.index('Finland')], countries[countries.index('Sweden')], countries[countries.index('Norway')], countries[countries.index('Denmark')];
print('First three countries: ', country1,',', country2, ',', country3, ', Scandic ones: ', scandic) 