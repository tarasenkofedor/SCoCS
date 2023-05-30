import re
from constants import (SENTENCE_PATTERN,
                       NON_DECLARATIVE_SENTENCE_PATTERN,
                       WORD_PATTERN, NUMBER_PATTERN,
                       ONE_WORD_ABBREVIATIONS,
                       TWO_WORDS_ABBREVIATIONS)


def count_sentences(text: str) -> int:
    text = text.lower()
    amount = len(re.findall(SENTENCE_PATTERN, text))

    for abbreviation in ONE_WORD_ABBREVIATIONS:
        amount -= text.count(abbreviation)

    for abbreviation in TWO_WORDS_ABBREVIATIONS:
        amount -= text.count(abbreviation) * 2

    return amount


def count_non_declarative_sentences(text: str) -> int:
    return len(re.findall(NON_DECLARATIVE_SENTENCE_PATTERN, text))


def get_avg_sentence_len(text: str) -> float:
    nums = re.findall(NUMBER_PATTERN, text)
    words = [word for word in re.findall(WORD_PATTERN, text) if word not in nums]
    words_len = sum(len(word) for word in words)

    return round(words_len / count_sentences(text), 2) if count_sentences(text) != 0 else 0


def get_avg_word_len(text: str) -> float:
    words = re.findall(WORD_PATTERN, text)
    words_len_in_characters = sum(len(word) for word in words)
    return round(words_len_in_characters / len(words), 2) if len(words) != 0 else 0


def get_top_k_repeated_n_grams(text: str, k=10, n=4):
    words = re.findall(WORD_PATTERN, text.lower())
    dictionary = {}
    for i in range(len(words) - n + 1):
        n_gram = ' '.join([str(word) for word in words[i:i + n]])
        if n_gram not in dictionary:
            dictionary[n_gram] = 1
        else:
            dictionary[n_gram] += 1
    sorted_ngrams = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    return sorted_ngrams[0:k]
