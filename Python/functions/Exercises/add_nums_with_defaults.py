# Open functions/Exercises/add_nums_with_defaults.py in your editor.
# Notice the add_nums() function takes five arguments, adds them together, and outputs the sum.

def add_nums(num1, num2, num3, num4, num5):
    total = num1 + num2 + num3 + num4 + num5
    print(num1, '+', num2, '+', num3, '+', num4, '+', num5, ' = ', total)

def main():
    add_nums(1, 2, 0, 0, 0)
    add_nums(1, 2, 3, 4, 5)
    add_nums(11, 12, 13, 14, 0)
    add_nums(101, 201, 301, 0, 0)

main()

# Modify add_nums() so that it can accept all of the following calls:
# add_nums(1, 2)
# add_nums(1, 2, 3, 4, 5)
# add_nums(11, 12, 13, 14)
# add_nums(101, 201, 301)
# For now, it’s okay for the function to print out 0s for values not passed in, like this:
# 1 + 2 + 0 + 0 + 0  =  3
# 1 + 2 + 3 + 4 + 5  =  15
# 11 + 12 + 13 + 14 + 0  =  50
# 101 + 201 + 301 + 0 + 0  =  603

print("==================")

def add_nums_modified(num1=0, num2=0, num3=0, num4=0, num5=0):
    total = num1 + num2 + num3 + num4 + num5
    print(num1, '+', num2, '+', num3, '+', num4, '+', num5, ' = ', total)

add_nums_modified(1,2)
add_nums_modified(1,2,3,4,5)
add_nums_modified(11,12,13,14)
add_nums_modified(101,201,301)