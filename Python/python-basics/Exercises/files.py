# Open a new script. Save it as files.py in python-basics/Exercises.
# Write code to open python-basics/data/1880-boys.txt and read its contents into a variable called boys.
# Write code to open python-basics/data/1880-girls.txt and read its contents into a variable called girls.
# Write code to open a new file named 1880-all.txt in the python-basics/data folder and write the combined contents of the boys and girls variables into the file. Note that you can combine the two strings like this:
# boys + "\n" + girls
# That will place one newline between the content in boys and the content in girls.
# Save your file.
# Test your solution. When you run it, it should create the new file. Look in the data folder for the 1880-all.txt file. Does it exist? If so, open it up. Does it have a list of all the boys and girls names?

with open("Python/python-basics/data/1880-boys.txt") as f1:
    boys = f1.read()
    print(boys)

with open("Python/python-basics/data/1880-girls.txt") as f2:
    girls = f2.read()
    print(girls)

with open("Python/python-basics/data/1880-all.txt", "w") as f3:
    all = f3.write(boys + "\n" + girls)