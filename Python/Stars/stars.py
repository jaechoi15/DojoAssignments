# Part I
# Create a function called draw_stars() that takes a list of numbers and prints out *.

x = [4, 6, 1, 3, 5, 7, 25]
stars = "*"

def draw_stars(arr):
    for i in range (0, len(arr)): 
        print stars * x[i]

draw_stars(x)

# Part II
# Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. When a string is passed, instead of displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part.

y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
stars = "*"

def draw_stars2(arr):
    for i in range (0, len(arr)):
        selection_type = type(y[i])
        if selection_type is int:
            print stars * y[i]
        else:
            lowercase = y[i].lower()
            print lowercase[:1] * len(y[i])

draw_stars2(y)