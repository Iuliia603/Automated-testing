
def user_name():
    user_input2 = input("What is your name?\n")
    return user_input2

name = user_name()
print("Nice to meet you, " + name + "!")

def user_hwu():
    user_input3 = input("How are you " + name + "?\n")
    return user_input3

response = user_hwu()
print("It is cool, " + name + "! " + "You said you are " + response + "!")