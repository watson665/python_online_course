# Open functions/Exercises/add_nums.py in your editor and review the code.
# Now, run the file in Python. 

def add_3_and_6():
    total = 3 + 6
    print('3 + 6 = ', total)

def add_10_and_12():
    total = 10 + 12
    print('10 + 12 = ', total)

def main():
    add_3_and_6()
    add_10_and_12()

main()

# Replace the two crazy add…() functions with an add_nums() function that accepts two numbers, adds them together, and outputs the equation.
def add_nums(num1, num2):
    total = num1 + num2
    print("The total of ", num1, "+", num2, "=", total, sep="") 

add_nums(3,6)
add_nums(10,12)
