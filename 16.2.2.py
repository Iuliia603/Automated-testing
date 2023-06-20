# an example to illustrate the scope of a variable inside a function
def my_func1():
	x = 10
	print("Value inside function:",x)

x = 20
my_func1()
print("Value outside function:",x)

# a game
x = 5
def my_func2(x, y):
	x = x + y

my_func2(x, 10)
print(x)
# my_func2() may be called with keyword arguments
my_func2(x=6, y=7)

# calling function with different order of keyword arguments
my_func2(y=7,x=6)


#calling function with both positional and keyword arguments
my_func2(6, y=7)


# an example of reading the value of the outside variable
x = "awesome"
def myfunc3():
	global x
	x = "fantastic"

myfunc3()
print("Python is " + x)

# function with default parameters
def print_cost(qty=6, item='bananas', price=3):
	output = str(qty) + " " + item + " cost " + str(price) + " dollars."
	print(output)

print_cost(4, 'apples')
print_cost(4)
print_cost()
print_cost(qty=5)

def shout_echo(word1, echo=1):
    echo_word= word1 * echo
    print(echo_word)
no_echo = shout_echo("Hey")
print(no_echo)
with_echo = shout_echo("Hey", echo=5)
print(with_echo)


