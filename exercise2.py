import typing
import collections
import types

def return_keys_from_nested_dictionaries(dictionary: typing.Dict) -> typing.List:
    """
    Returns a list of keys from a nested dictionary.

    Args:
        dictionary (typing.Dict): The input dictionary.

    Returns:
        typing.List: A list of keys from the input dictionary.

    Raises:
        TypeError: If the input is not a dictionary.
    """
    if not isinstance(dictionary, dict):
        raise TypeError("Input must be a dictionary")

    keys_list = []
    for value in dictionary.values():
        
        if isinstance(value, dict):
            keys_list.extend(value.keys())
            
    return keys_list

nested_dict = {
    "outer1": {"inner1": 1, "inner2": 2},
    "outer2": {"inner3": 3, "inner4": 4}
}
print(return_keys_from_nested_dictionaries(nested_dict))