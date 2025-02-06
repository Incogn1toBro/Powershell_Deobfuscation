input_string = "X,X,X"

numbers_as_strings = input_string.split(',')

numbers = [int(number) for number in numbers_as_strings]

characters = [chr(number) for number in numbers]

normal_string = ''.join(characters)

print(normal_string)
