def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        print("Strings are not anagrams: different lengths.")
        return

    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    if sorted_str1 == sorted_str2:
        print("The strings are anagrams")
    else:
        print("The strings are not anagrams")


string_1 = input("Enter the first line: ")
string_2 = input("Enter the second line: ")
are_anagrams(string_1, string_2)

# "ruba" and "bura"