import string
def remove_punctuation(input_string):
    return input_string.translate(str.maketrans('', '', string.punctuation))

print("Enter a string:")
input_string = input()
cleaned_string = remove_punctuation(input_string)
print("String after removing punctuation:")
print(cleaned_string)
