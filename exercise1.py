import typing
import collections
import types


def frequency_counter(word__list: typing.List) -> typing.Dict:
    """
    This function takes a list of words as input and returns a dictionary
    containing the frequency of each word in the list.

    Args:
        word__list (typing.List): A list of words.

    Returns:
        typing.Dict: A dictionary where the keys are the words from the input list,
                     and the values are the corresponding frequencies.
    """
    # Create a Counter object from the input list
    # Counter is a subclass of dict, so we can directly return it
    # return collections.Counter(word__list)
    # Create an empty dictionary to store the word frequencies
    word_dict = {}
    for word in word__list:
        word_dict[word] = word_dict.get(word, 0) + 1

    return word_dict


word_list = ['red', 'blue', 'red', 'green', 'green', 'red']
# Call the frequency_counter function with the word_list
# and print the resulting dictionary
print(frequency_counter(word_list))


def store_student_scores(score__list: typing.Tuple) -> typing.DefaultDict:
    student_scores_defaultdict = collections.defaultdict(list)
    for student, score in score__list:
        student_scores_defaultdict[student].append(score)

    return student_scores_defaultdict


score_list = [('Ivan', 5), ('Petro', 5), ('Petro', 4), ('Mykola', 3)]
# Call the store_student_scores function with the score_list
# and print the resulting defaultdict
print(store_student_scores(score_list))


def search_key(dictionary1: typing.Dict, dictionary2: typing.Dict, search_key: typing.Any) -> typing.Any:
    """
    This function searches for a given key in a dictionary and returns the corresponding value.
    If the key is not found, it returns the string 'Not found'.

    Args:
        dictionary (typing.Dict): The dictionary to search in.
        search_key (typing.Any): The key to search for.

    Returns:
        typing.any: The value corresponding to the search_key if found, otherwise 'Not found'.
    """
    combined_dict = collections.ChainMap(dictionary1, dictionary2)
    return combined_dict[search_key]


dictionary1 = {"a": 10, "b": 20}
dictionary2 = {"b": 50, "c": 80}
print(search_key(dictionary1, dictionary2, "b"))

original_dict = {"x": 1, "y": 2}
read_only_dict = types.MappingProxyType(original_dict)
try:
    read_only_dict["y"] = 5
except Exception as e:
    print (f"Erro is {e}")
