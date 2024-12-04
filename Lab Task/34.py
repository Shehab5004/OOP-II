def sort_words_alphabetically(sentence):
    words = sentence.split()
    words.sort()
    return words
print("Enter a sentence:")
sentence = input()
sorted_words = sort_words_alphabetically(sentence)
print("Words in alphabetical order:")
for word in sorted_words:
    print(word)
