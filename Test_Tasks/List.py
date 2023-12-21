my_list = [6, 12, 18, 24, 30]
print("Original list:", my_list)


def swap_numbers(my_list, index1, index2):
        my_list[index1], my_list[index2] = my_list[index2], my_list[index1]


swap_numbers(my_list, 1, 3)
print("After swapping numbers with indices 1 and 3:", my_list)