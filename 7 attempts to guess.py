import random
num = random.randint(0,50)
print(num)
print("Guess the number from 1 to 50. You have 7 attempts!")

for attempt in range(7):
    user_input = int(input("Enter number: \n"))

    if user_input == num:
        print("You guessed correctly!")
        break
    elif user_input < num:
        print("The value is too low")
    else:
        print("The value is too high")

if user_input != num:
    print("Sorry, you didn't guess. The correct number was: " + str(num))