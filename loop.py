xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
print("Each number on a new line:")
for number in xs:
    print(number)

print("A number and its square:")
for number in xs:
    square = number ** 2
    print(number, square)



total = 0
for number in xs:
    total += number
print("Total:", total)

product = 1
for number in xs:
    product *= number
print("Product:", product)

