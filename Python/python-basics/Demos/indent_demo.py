# def main():
#     print("I am part of the function.")
#     print("I am also part of the function.")
#     print("Hey, me too!")
# print("Sad not to be part of the function. I've been outdented.")

# main()

with open("my-file.txt", "w") as f:
    content = f.write("Hello Peeps!")
    print(content)

