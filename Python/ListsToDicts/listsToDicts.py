# Create a function that takes in two lists and creates a single dictionary. The first list contains keys and the second list contains the values. Assume the lists will be of equal length.

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

# def make_dict(list1, list2):
#   new_dict = {}
#   new = zip(name, favorite_animal)
#   print new_dict

#  make_dict(name, favorite_animal)
new_list = {}
new = zip(name, favorite_animal)
new_list.append(new)
print new_list