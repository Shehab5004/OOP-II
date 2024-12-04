def list_to_string(input_list):
    return ' '.join(input_list)
print("Enter a list of words separated by spaces:")
input_string = input()
input_list = input_string.split()
result_string = list_to_string(input_list)
print("Converted string:")
print(result_string)
