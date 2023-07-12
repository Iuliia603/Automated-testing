# Exercise 2
dictionary = {'Jake': '$100K', 'Anand': '$120K'}
for name, salary in dictionary.items():
    print("{}: {}".format(name, salary))

# Exercise 3
my_tuple = (4, 30, 2017, 2, 27)
print("{3} {4} {2} {0} {1}".format(*my_tuple))

# Exercise 1
while True:
    user_input = input("Enter the text to convert to lowercase (to stop, type 'STOP'):\n")

    if user_input == "STOP":
        print("The program is over")
        break
    print(user_input.lower())