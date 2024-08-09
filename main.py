def main():
    path = "books/frankenstein.txt"

    with open(path) as f:
        file_contents = f.read()

    sorted_word_frequency = sort_word_frequency(count_word_frequency(file_contents))
    print(f"--- Begin report of {path} ---")
    for word in sorted_word_frequency:
        print(f"The {word[0]} word was found {word[1]} times")
    print("--- End report ---")


def count_words(text):
    words = text.split()
    return len(words)

def count_word_frequency(text):
    words = text.lower()
    word_frequency = {}
    for word in words:
        if word.isalpha():
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1
    return word_frequency

def sort_word_frequency(word_frequency):
    return sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    main()