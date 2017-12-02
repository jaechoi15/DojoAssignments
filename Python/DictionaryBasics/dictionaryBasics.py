# Create a dictionary containing some information about yourself. The keys should include name, age, country of birth, favorite language.

# My name is Anna
# My age is 101
# My country of birth is The United States
# My favorite language is Python

my_dictionary = {"name": "Jae", "age": "28", "country of birth": "South Korea", "favorite language": "Python"}

def readDictionary():
    for val in my_dictionary.itervalues():
        print val

readDictionary()

# print my_dictionary.get("name")