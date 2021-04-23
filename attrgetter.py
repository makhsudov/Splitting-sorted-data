from operator import attrgetter

class Object(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __repr__(self):
		template = '{0.name} {0.age}'
		return template.format (self)

# Function to return age 
def byAge_key(object): 
    return object.age

# Arrays to be sorted 
name = ['Adam', 'Bob', 'Mark']
age = [34, 41, 21]


i = 0
elements = []
# Assigning elements of class Object: name and age 
for el in name:
	people = Object(name [i], age [i])
	elements.append (people)
	i += 1

# Sort items by byAge_key function, which returns object.age 
sorting = sorted (elements, key = byAge_key, reverse = False)


newName = []
newAge = []
i = 0
# Separating sorted data into different arrays in sort order 
for z in name:
	attName = attrgetter ('name') # Returning text by key 'name' from class
	attAge = attrgetter ('age')

	sortedName = attName (sorting[i]) # Executing attName 
	sortedAge = attAge (sorting [i])

	newName.append (sortedName) 
	newAge.append ( sortedAge )

	i += 1