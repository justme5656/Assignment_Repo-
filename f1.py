num1 = float(input('Enter a number: '))
num2 = float(input('Enter another number: '))

print(num1, num2)

result = num1 + num2
int_result = int(result)
hex_r = hex(int_result)
print(result)
print(hex_r)
print(num1 - num2)

print(num1 * num2)

if num1 > num2:
    print(num1 / num2)
    print(num1 % num2)
else:
    print("Invalid num 1")