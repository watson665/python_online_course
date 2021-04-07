def add_nums(num1, num2, num3=0, num4=0, num5=0):
    total = num1 + num2 + num3 + num4 + num5
    return total

def main():
    result = add_nums(1, 2)
    print(result)
    result = add_nums(result, 3)
    print(result)
    result = add_nums(result, 4)
    print(result)
    result = add_nums(result, 5)
    print(result)
    result = add_nums(result, 6)
    print(result)

#Only run main() if we are in this module so that it doesn't run in imported modules
if __name__ == '__main__':
    main()



