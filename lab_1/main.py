"""
Lab 1
A concordance extraction
"""
# fyjvhmb,nkljkhjgn

import re

#text = open("data.txt", "r")
#c = text.read()


def tokenize(text: str) -> list:
    """
    Splits sentences into tokens, converts the tokens into lowercase, removes punctuation
    :param text: the initial text
    :return: a list of lowercased tokens without punctuation
    e.g. text = 'The weather is sunny, the man is happy.'
    --> ['the', 'weather', 'is', 'sunny', 'the', 'man', 'is', 'happy']
    """

    if isinstance(text, str):
        text = text.lower()
        tokens = re.sub('[\'\",.!0-9+=\!@#$%^&*()-_]+', '', text).split()
        print(tokens[:10])
        return tokens
    else:
        return []


#tokenize(c)
#tokens = tokenize(c)


def remove_stop_words(tokens: list, stop_words: list) -> list:
    """
    Removes stop words
    :param tokens: a list of tokens
    :param stop_words: a list of stop words
    :return: a list of tokens without stop words
    e.g. tokens = ['the', 'weather', 'is', 'sunny', 'the', 'man', 'is', 'happy']
    stop_words = ['the', 'is']
    --> ['weather', 'sunny', 'man', 'happy']
    """

    listt = []
    if isinstance(stop_words, list) and isinstance(tokens, list):
        for token in tokens:
            if token not in stop_words:
                listt.append(token)
        return listt

    elif isinstance(tokens, list) and not isinstance(stop_words, list):
        return tokens

    else:
        return []


def calculate_frequencies(tokens: list) -> dict:
    """
    Calculates frequencies of given tokens
    :param tokens: a list of tokens without stop words
    :return: a dictionary with frequencies
    e.g. tokens = ['weather', 'sunny', 'man', 'happy']
    --> {'weather': 1, 'sunny': 1, 'man': 1, 'happy': 1}
    """
    freq_dict = {}
    if isinstance(tokens, list):
        for word in tokens:
            if not isinstance(word, str):
                freq_dict = {}

            elif word in freq_dict:
                freq_dict[word] += 1

            else:
                freq_dict[word] = 1

        return freq_dict
    else:
        return {}


def get_top_n_words(freq_dict: dict, top_n: int) -> list:
    """
    Returns the most common words
    :param freq_dict: a dictionary with frequencies
    :param top_n: a number of the most common words to return
    :return: a list of the most common words
    e.g. tokens = ['weather', 'sunny', 'man', 'happy', 'and', 'dog', 'happy']
    top_n = 1
    --> ['happy']
    """
    tokens = []
    if isinstance(freq_dict, dict):
        sorted_dict = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
        # print(sorted_dict)
        for i in sorted_dict:
            tokens.append(i[0])
    return tokens[:top_n]

#tokens = ['the', 'weather', 'is', 'sunny', 'the', 'man', 'is', 'happy',
                    #'the', 'dog', 'is', 'happy', 'but', 'the', 'cat', 'is', 'sad']
def get_concordance(tokens: list, word: str, left_context_size: int, right_context_size: int) -> list:
    """
    Gets a concordance of a word
    A concordance is a listing of each occurrence of a word in a text,
    presented with the words surrounding it
    :param tokens: a list of tokens
    :param word: a word-base for a concordance
    :param left_context_size: the number of words in the left context
    :param right_context_size: the number of words in the right context
    :return: a concordance
    e.g. tokens = ['the', 'weather', 'is', 'sunny', 'the', 'man', 'is', 'happy',
                    'the', 'dog', 'is', 'happy', 'but', 'the', 'cat', 'is', 'sad']
    word = 'happy'
    left_context_size = 2
    right_context_size = 3
    --> [['man', 'is', 'happy', 'the', 'dog', 'is'], ['dog', 'is', 'happy', 'but', 'the', 'cat']]
    """
    # bad_inputs = ['string', (), None, 9, 9.34, True, [None], []]
    concordance = []

    if (not isinstance(tokens, list) or not isinstance(left_context_size, int) or
            not isinstance(right_context_size, int) or not isinstance(word, str)
            or isinstance(right_context_size, bool) or isinstance(left_context_size, bool)):
        return []

    else:
        for index, token in enumerate(tokens):
            if isinstance(token, str) and token == word:

                len_left = len(tokens[index - left_context_size:index])
                len_right = len(tokens[index: index + right_context_size + 1])
                left_word = tokens[index - left_context_size:index]
                right_word = tokens[index: index + right_context_size + 1]

                if ((left_context_size >= 1) and (left_context_size <= len_left)
                        and (right_context_size >= 1) and (right_context_size <= len_right)):
                    context = left_word + right_word
                    concordance.append(context)

                elif ((left_context_size >= 1) and
                      (left_context_size <= len_left) and (right_context_size < 1)):
                    context = left_word
                    concordance.append(context)

                elif (left_context_size < 1) and (right_context_size >= 1):
                    context = right_word
                    concordance.append(context)

                elif ((left_context_size > len_left) and (right_context_size >= 1)
                      and (right_context_size <= len_right)):
                    context = tokens[0:index] + right_word
                    concordance.append(context)

                elif (left_context_size > len_left) and (right_context_size < 1):
                    context = tokens[0:index + 1]
                    concordance.append(context)
        print(concordance)
        return concordance


#get_concordance(tokens, 'happy', 2, 3)
#content = get_concordance(tokens, 'happy', 2, 3)

def get_adjacent_words(tokens: list, word: str, left_n: int, right_n: int) -> list:
    """
    Gets adjacent words from the left and right context
    :param tokens: a list of tokens
    :param word: a word-base for the search
    :param left_n: the distance between a word and an adjacent one in the left context
    :param right_n: the distance between a word and an adjacent one in the right context
    :return: a list of adjacent words
    e.g. tokens = ['the', 'weather', 'is', 'sunny', 'the', 'man', 'is', 'happy',
                    'the', 'dog', 'is', 'happy', 'but', 'the', 'cat', 'is', 'sad']
    word = 'happy'
    left_n = 2
    right_n = 3
    --> [['man', 'is'], ['dog, 'cat']]
    """
    adj_w = []
    if (not isinstance(tokens, list) and not isinstance(word, str)
            and not isinstance(left_n, int) and not isinstance(right_n, int)
            and (right_n < 1) and (left_n < 1)):
        return []
    else:
        concordance = get_concordance(tokens, word, left_n, right_n)
        # print(concordance)
        for cont in concordance:
            if (left_n < 1) and (right_n >= 1):
                adj_w.append([cont[-1]])

            elif (right_n < 1) and (left_n >= 1):
                adj_w.append([cont[0]])

            elif (right_n >= 1) and (left_n >= 1):
                adj_w.append([cont[0], cont[-1]])

        return adj_w


# get_adjacent_words(['the', 'weather', 'is', 'sunny', 'the', 'man', 'sunny', 'ygh'] , 'sunny', 0, 1)


def read_from_file(path_to_file: str) -> str:
    """
    Opens the file and reads its content
    :return: the initial text in string format
    """
    with open(path_to_file, 'r', encoding='utf-8') as fs:
        data = fs.read()

    return data


def write_to_file(path_to_file: str, content: list):
    """
    Writes the result in a file
    """
    with open(path_to_file, "w") as f:
        for item in content:
            value = ' '.join(item)
            value += '\n'
            f.write(value)
#write_to_file('report.txt', content)


def sort_concordance(tokens: list, word: str, left_context_size: int, right_context_size: int, left_sort: bool) -> list:
    """
    Gets a concordance of a word and sorts it by either left or right context
    :param tokens: a list of tokens
    :param word: a word-base for a concordance
    :param left_context_size: the number of words in the left context
    :param right_context_size: the number of words in the right context
    :param left_sort: if True, sort by the left context, False – by the right context
    :return: a concordance
    e.g. tokens = ['the', 'weather', 'is', 'sunny', 'the', 'man', 'is', 'happy',
                    'the', 'dog', 'is', 'happy', 'but', 'the', 'cat', 'is', 'sad']
    word = 'happy'
    left_context_size = 2
    right_context_size = 3
    left_sort = True
    --> [['dog', 'is', 'happy', 'but', 'the', 'cat'], ['man', 'is', 'happy', 'the', 'dog', 'is']]
    """
    pass
