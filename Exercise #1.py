
def print_sum_avg(numbers):
    summary = sum(numbers)
    average = summary / len(numbers)

    print("Sum: ", summary)
    print("Average: ", average)

def request_numbers():
    numbers = []

    for num in range(3):
        user_input = input("Enter number " + str(num + 1) + ":\n")
        numbers.append(int(user_input))
    print_sum_avg(numbers)

request_numbers()