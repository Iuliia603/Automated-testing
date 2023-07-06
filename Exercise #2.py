def print_sum_avg_arg(*args):
    summary = sum(args)
    average = summary / len(args)

    print("Sum: ", summary)
    print("Average: ", average)

def request_numbers():
    numbers = []
    for num in range(3):
        user_input = input("Enter number " + str(num + 1) + ":\n")
        numbers.append(int(user_input))
    print_sum_avg_arg(*numbers)

request_numbers()