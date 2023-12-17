def word_frequency(sentence):
    cleaned_sentence = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in sentence)
    words = cleaned_sentence.split()
    return {word: words.count(word) for word in set(words)}

# Test the function
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)