def count_words_recursive(words, index=0, freq_dict=None):
    """Recursively count word frequencies in a list."""
    if freq_dict is None:
        freq_dict = {}

    if index == len(words):
        return freq_dict

    word = words[index]
    freq_dict[word] = freq_dict.get(word, 0) + 1

    return count_words_recursive(words, index + 1, freq_dict)


def word_frequency_analysis(text):
    """Return word frequencies and the most frequent word in a text."""
    words = text.split()
    freq_dict = count_words_recursive(words)
    most_frequent = max(freq_dict, key=freq_dict.get) if freq_dict else None

    return {
        "Word Frequencies": freq_dict,
        "Most Frequent Word": most_frequent
    }


# ------------------ Example Usage ------------------
text_input = "apple banana apple orange banana apple banana banana"
result = word_frequency_analysis(text_input)
print(result)
