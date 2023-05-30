import statistic_util


def main():
    text = input('Enter text: ')
    print('Amount of sentences: ' + str(statistic_util.count_sentences(text)))
    print('Amount of non-declarative sentences: ' + str(statistic_util.count_non_declarative_sentences(text)))
    print('Average word length: ' + str(statistic_util.get_avg_word_len(text)))
    print('Average sentence length: ' + str(statistic_util.get_avg_sentence_len(text)))
    print('Top k repeated anagrams: ' + str(statistic_util.get_top_k_repeated_n_grams(text)))


if __name__ == "__main__":
    main()
