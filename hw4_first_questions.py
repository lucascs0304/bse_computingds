# 1)
# Create a function named
# "triple" that takes one
# parameter, x, and returns
# the value of x multiplied
# by three.
#

def triple(x):
    y = x*3
    return(y)

print(triple(12))

# 2)
# Create a function named "subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
#

def subtract(a,b):
    x = b - a
    return(x)

print(subtract(4,9))


# 3)
# Create a function called "dictionary_maker"
# that has one parameter: a list of 2-tuples.
# It should return the same data in the form
# of a dictionary, where the first element
# of every tuple is the key and the second
# element is the value.
#
# For example, if given: [('foo', 1), ('bar', 3)]
# it should return {'foo': 1, 'bar': 3}


def dictionary_maker(x):
    keys = []
    values = []
    for i in x:
        keys.append(i[0])
        values.append(i[1])
    x = dict(zip(keys, values))
    return(x)

z = [('lucas', 22), ('giovanna', 24)]
print(dictionary_maker(z))