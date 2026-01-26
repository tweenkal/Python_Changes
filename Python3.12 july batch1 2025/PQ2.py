# Input text
text = "apple banana apple orange banana apple banana banana"

# Split the text into words
words = text.split()

# Create a dictionary to store word frequencies
word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Find the most frequent word
most_frequent_word = max(word_freq, key=word_freq.get)

# Display results
result = {
    "Word Frequencies": word_freq,
    "Most Frequent Word": most_frequent_word
}

print(result)
