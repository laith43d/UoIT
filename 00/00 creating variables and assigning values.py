import math


# All types in Python are objects
a = 2

# variables in Python has no limits, the memory is the limit!
b = 9901910191091091095465465411654654656546546546546546546546
c = 'A'
d = 3.232
pi = 3.14

print(type(a))

# This is the real deal
print(a.__add__(5))

# This is syntactic sugar!
print(a + 5)


# Python deals with complex numbers natively
comp1 = 2 + 3j
comp2 = 5 - 4j

print(comp1 + comp2)
print(comp1 - comp2)
print(comp1 * comp2)
print(comp1 / comp2)

# standard library is very rich, you don't need to define PI, it is already predefined for you!
print(math.pi)

q = True
y = False
x = None

print(type(True))
print(type(False))
print(type(None))
print(type(2))
print(type(2.1))
print(type('a'))

# The difference between '=='  and 'is'
print(2 == 2)
print(2 == 2.0)
print(2 is 2)
print(2 is 2.0)

_x = 2

# 0 = 'a' - Invalid syntax
# 9x = 2 - Invalid syntax
# $x = 2 - Invalid syntax

a, b, c = 1, 2, 3

# packing and unpacking
a, *b, c = [1, 2, 3, 4]

print(b)

a, b, *c = [1, 2, 3, 4]

print(a)
print(b)
print(c)


def afunction(*args):
    print(args)
    for arg in args:
        print(arg)


afunction(1, 2, 3, 4)

# collections
# tuple, list, set, dictionary

a = (1, 2, 3)
print(type(a))
b = [1, 2, 3, 4]
print(type(b))
c = {1, 2, 3, 4}
print(type(c))
d = {'x': 1,
     'y': 2,
     'z': 3,
     }
print(type(d))


def bfunction(*args, **kwargs):
    print(args, kwargs)


bfunction(1, 2, 3, a=1, b=5)

# string is a special type of collections
name = 'layth'
print(name)
print(name.capitalize())
print(name.upper())
print(name[::-1])

print(name)
print(name[0])
print(name[1])
print(name[0:2])
print(name[:])
print(name[::2])
print(name[::-1])

print(b[::-1])
