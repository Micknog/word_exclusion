# In this code, we want to analyse words in a given/ selected language
# Neste código, queremos analisar palavras em um dado (ou selecionado) idioma.

from itertools import combinations    # function to make the combinatory analysis

# Local dos arquivos com os verbetes de um dado idioma
from typing import List

location_eng = 'C:\\Users\\micha\\Desktop\\word_lists\\words.txt'


def twenty_or_more(i=0, letter_amount=20) -> object:
    """
    Detect a word with 'X' (letter_amount) or more letters, returns the word and position.

    :rtype: object
    :param i : counter, type: int
    :param letter_amount : amount of letters to filter, type: int
    """

    language_file = open(location_eng, 'r')
    for lines in language_file:
        line = lines.strip()
        if len(line) >= letter_amount:
            i += 1
            return f'The word {line} is in the position {i}'
        else:
            continue


def have_letter(letter: str, j: int = 0, k: int = 0) -> (str, str, float):
    """
    Check and count the amount of words without `letter` (one or more letters).

    :param letter: letter to be excluded, type: str
    :param k: position counter, type: int
    :param j: relative position counter, type: int
    :returns: j, type: str, letter, type: str, and percent (proportion of j relative to all words)
    :rtype: object
    """
    language_file = open(location_eng, 'r')
    for no_letter_line in language_file:
        if all(x in no_letter_line for x in letter):
            # print(f' This word {no_e_line} don\'t contain "{letter}", position {j}')
            j += 1
            k += 1
        else:
            k += 1
    percent = (j / k) * 100
    print(f'{round(percent, ndigits= 2)}% of the total {k} have "{letter}"')
    return j, letter, percent


def avoids(word: str, forbidden: str) -> bool:
    """
    Check if a word doesn't contain a forbidden string

    :param word: word to check, type: str
    :param forbidden: letters to avoid, type: str
    :return: analysis result
    :rtype: bool
    """
    language_file = open(location_eng, 'r')
    for line_avoid in language_file:
        if str(word).strip() == str(line_avoid).strip():
            if forbidden not in line_avoid:
                return True


def word_loss_analysis(string: str, size: int, y: object = '', minimum_value: int = 0, minimum_letter: str = '',
                       minimum_percent: float = 0, maximum_value: int = 0, maximum_letter: str = '',
                       maximum_percent: float = 0) -> str:
    """
    Analise the amount of words lost for a combination of letters in a given string. The amount of items is passed in
    the `size` parameter.

    :param string: string to be analysed
    :type string: str
    :param size: amount of items to combine
    :type size: int
    :param y: place holder for preliminary results
    :type y: str
    :param minimum_value: minimum amount of words lost,
    :type minimum_value: int
    :param minimum_letter: string to lose the minimum amount of words
    :type minimum_letter: str
    :param minimum_percent: percentage of the minimum loss relative to total
    :type minimum_percent :float
    :param maximum_value: maximum amount of words lost
    :type maximum_value int
    :param maximum_letter: string to lose the maximum amount of words
    :type maximum_letter: str
    :param maximum_percent: percentage of the maximum loss relative to total,
    :type maximum_percent: float
    :returns: Minimum and maximum values in the screen
    :rtype: str
    """
    string_to_list: list[str] = []   # Auxiliary variable to convert the strings into lists
    unique_combinations = []   # Auxiliary variable to hold the list of unique combinations
    unique_formatted = []    # Auxiliary variable to convert the lists of unique combinations into strings

    for element in string:
        string_to_list.append(element)

    combs = combinations(string_to_list, size)

    for i in list(combs):
        unique_combinations.append(list(i))

    for element in unique_combinations:
        unique_formatted.append(''.join(element))

    minimum_value = 200_000_000_000_000
    maximum_value = 0
    for unique_element in unique_formatted:
        y: str = have_letter(letter=unique_element)
        if y[0] < minimum_value:
            minimum_value = y[0]
            minimum_letter = y[1]
            minimum_percent = y[2]
        if y[0] > maximum_value:
            maximum_value = y[0]
            maximum_letter = y[1]
            maximum_percent = y[2]

    result1 = (maximum_value, maximum_letter, maximum_percent)
    result2 = (minimum_value, minimum_letter, minimum_percent)

    print(f'Maximum loss: {result1[0]} | {round(result1[2], ndigits=3)}%, letter: {result1[1]}\n'
          f'Minimum loss: {result2[0]} | {round(result2[2], ndigits=3)}%, letter: {result2[1]}')

    return f'_*'


# have_letter('a')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
word_loss_analysis(alphabet, 2)
