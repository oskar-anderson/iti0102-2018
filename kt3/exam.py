"""KT3."""
import re


def duplicate_last(nums: list) -> list:
    """
    Return a list where the last element is doubled.

    In the case of empty list, return empty list.

    duplicate_last([1, 2, 3]) => [1, 2, 3, 3]
    duplicate_last([7]) => [7, 7]
    duplicate_last([]) => []
    """
    try:
        error_check = nums[0]
        print(error_check)
    except IndexError:
        return []
    else:
        new_nums_list = []
        for i in range(len(nums)):
            new_nums_list = nums[:]
        new_nums_list.append(nums[-1])
        return new_nums_list


def list_query(data: list, query_set: set) -> dict:
    """
    Return dict, where keys are elements from set and values are key counts in data.

    The set does not contain elements which cannot be used as key. Also, the set does not contain True/False.

    list_query(["a", "b", "b", "c"], {"a", "b"}) => {"a": 1, "b": 2}
    list_query(["a", "b", "b", "c"], {"a", "d"}) => {"a": 1, "d": 0}
    list_query(["a", "b", "b", "c"], set()) => {}
    list_query([], {"a", "b"}) => {"a": 1, "b": 2}  # mistake?!!
    list_query([1, True], {1}) => {1: 1}
    """
    counting_dict = {}
    for key in query_set:
        # print(key)
        # print(data.count(key))
        number_of_true_false = str(data).count("True") + (str(data).count("False"))
        counting_dict[key] = int(data.count(key)) - number_of_true_false
    return counting_dict


def sum_numbers(s):
    """
    Given a string, return the sum of the numbers appearing in the string, ignoring all other characters.

    A number is a series of 1 or more digit chars in a row.

    sum_numbers("abc123xyz") => 123
    sum_numbers("aa11b33") => 44
    sum_numbers("7 11") => 18
    """
    sum_of_list_items = 0
    list_of_numbers = []
    regex = r"([0-9]+)"
    for match in re.finditer(regex, s):
        list_of_numbers.append(match.group())
    print(list_of_numbers)
    for i in range(len(list_of_numbers)):
        sum_of_list_items += int(list_of_numbers[i])
    return sum_of_list_items


if __name__ == '__main__':
    # print(duplicate_last([1, 2, 3]))
    # print(duplicate_last([7]))
    # print(duplicate_last([]))

    # print(list_query(["a", "b", "b", "c"], {"a", "b"}))  # {"a": 1, "b": 2}
    # print(list_query(["a", "b", "b", "c"], {"a", "d"}))  # {"a": 1, "d": 0}
    # print(list_query(["a", "b", "b", "c"], set()))  # {}
    print(list_query([], {"a", "b"}))  # {"a": 1, "b": 2}
    print(list_query([1, True], {1}))  # {1: 1}

    # print(sum_numbers("abc123xyz"))  # 123
    # print(sum_numbers("aa11b33"))  # 44
    # print(sum_numbers("7 11"))  # 18
