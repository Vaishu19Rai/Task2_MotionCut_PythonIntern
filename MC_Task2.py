def count_words(sentence):
    # Initialize count to 1 assuming at least one word is present
    count = 1
    for char in sentence:
        if char == ' ':
            count += 1
    return count
 
# Example usage
sentence = input("Enter a sentence or a sequence of string:")
print("Number of words:", count_words(sentence))
