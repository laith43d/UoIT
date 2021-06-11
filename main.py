from module import print_name

if __name__ == "__main__":
    print("Im am executing the main.py script")
    print("The file imported name is:")
    print_name()
    print()
    print("The file being executed name is:")
    print(__name__)

# int operations

# imaginary operations

# reverse text operations and iterators


# kwlist
# from keyword import kwlist
#
# print(len(kwlist))
# print(kwlist)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in my_list:
    if i % 2 ==0:
        print(i * 2)

for i, v in enumerate(my_list):
    print(i, v)

# [var for var in range(10)]
your_list = [i * 2 for i in my_list]

odd_numbers = [i*2 for i in my_list if i % 2 == 0]

print([i for i in range(10) if i % 2 == 0])

print({i: v for i, v in enumerate(my_list)})

# print({i for i in range(10)})

print((i for i in range(10)))

'''
1. List comprehension
2. Loops (Collections)
3. Dictionary
4. Generator expressions
5. Functions
'''

'''
5. Project

'''