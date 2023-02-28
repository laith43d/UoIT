import math

# All types in Python are objects
a = 2

# variables in Python has no limits, the memory is the limit!
b = 9901910191091091095465465411654654656546546546546546546546
c = 'A'
d = 3.232
pi = 3.14

print(type(a))
number: int = 2

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

print(True)
print('a' == 'A')
print(True)

# The difference between '=='  and 'is'
print(True)
print(2 == 2.0)
print(2 is not 2)
print(2 is 2.0)

_x = 2

# 0 = 'a' - Invalid syntax
# 9x = 2 - Invalid syntax
# $x = 2 - Invalid syntax

# list, set, dictionary, tuple

# tuple

tuple_a = (1, 2, 3)
print(type(tuple_a))

# list

list_a = [1, 2, 3]
print(type(list_a))

# set

set_a = {1, 2, 3}
print(type(set_a))

# dictionary

dictionary_a = {'x': 2, 'y': 5}
print(type(dictionary_a))

# unpacking
a, b, c = 1, 2, 3

# packing and unpacking
a, *b, c = [1, 2, 5, 6, 3, 4]

print(a)
print(b)
print(c)

a, b, *c = [1, 2, 3, 4, 5, 6]

print(a)
print(b)
print(c)

a, *b = [1, 2, 3, 4, 5, 6]

iterable_list = [1, 2, 3, 4, 5, 6]

print(iterable_list[1])

for i, v in enumerate(iterable_list):
    print(i, v)


def afunction(*args):
    print(sum(args))


afunction(1, 2, 3, 4, 5, 6, 7)

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

dictionary_type_one = {
    'x': 1,
    'y': 2
}


def bfunction(*args, **kwargs):
    print(args, kwargs)


def cfunction(arg1, arg2, arg3, arg4: int = 3):
    print(arg1, arg2, arg3)


cfunction(1, 2, 3, arg4=6)

bfunction(1, 2, 3, 4, a=1, b=5, c='x')

# string is a special type of collections
name = 'laythzuhair'

for i, v in enumerate(name):
    print(i, v)

print(name[0])

print(name)
print(name.capitalize())
print(name.upper())

# slicing [start:stop:step]

print(name[::-1])

print(name)
print(name[0])
print(name[1])
print(name[1:7:2])
print(name[:])
print(name[::2])

print(name[-1::-2])

print(name[::-1])

palindrome = 'abcdcba'

if palindrome == palindrome[::-1]:
    print("palindrome")

print(b[::-1])


