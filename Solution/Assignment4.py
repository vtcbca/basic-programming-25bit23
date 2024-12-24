input_string = input("Enter a string: ")
reversed_string = ""
index = len(input_string) - 1
while index >= 0:
    reversed_string += input_string[index]
    index -= 1
print("Reversed string:", reversed_string)
