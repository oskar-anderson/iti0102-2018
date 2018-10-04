"""Test 3 (N10)."""


def middle_way(a, b):
    """
    Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

    middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
    middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
    middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]

    :param a: List of integers of length 3.
    :param b: List of integers of length 3.
    :return: List of integers of length 2.
    """
    return [a[1], b[1]]


def in1to10(n, outside_mode):
    """
    Return whether n follows the given rules.

    Given a number n, return True if n is in the range 1..10, inclusive.
    Unless outside_mode is True, in which case return True if the number is less or equal to 1,
    or greater or equal to 10.

    in1to10(5, False) → True
    in1to10(11, False) → False
    in1to10(11, True) → True

    :param n: Number to check.
    :param outside_mode: Whether we use outside mode.
    :return: Whether the number follows the given rules.
    """
    if n in range(1-11):
        return True
    elif outside_mode is True:
        return True
    else:
        return False


def non_start(first_string, second_string):
    """
    Given 2 strings, return their concatenation, except omit the first char of each.

    The strings will be at least length 1.

    non_start('Hello', 'There') → 'ellohere'
    non_start('java', 'code') → 'avaode'
    non_start('shotl', 'java') → 'hotlava'

    :param second_string: First string.
    :param first_string: Second string.
    :return: Concatenation of two string without first chars.
    """
    return first_string[1:] + second_string[1:]


def remove_nth_symbol(s, n):
    """
    Return a new string where n-th symbol is removed.

    If the n is outside of the string, return original string.
    If n is 1, the first symbol is removed etc.

    remove_nth_symbol("tere", 1) => "ere"
    remove_nth_symbol("tere", 3) => "tee"
    remove_nth_symbol("tere", 5) => "tere"

    :param s: Input string.
    :param n: Which element to remove.
    :return: String where n-th symbol is removed.
    """
    if n == 1:
        return s[n:]
    elif n - 1 < len(s):
        return s[0:n-1] + s[n:]
    else:
        return s


def word_numeration(words):
    """
    For a given list of string, add numeration for every string.

    The input list consists of strings. For every element in the input list,
    the output list adds a numeration after the string.
    The format is as follows: #N, where N starts from 1.
    String comparison should be case-insensitive.
    The case of symbols in string itself in output list should remain the same as in input list.

    The output list has the same amount of elements as the input list.
    For every element in the output list, "#N" is added, where N = 1, 2, 3, ...

    word_numeration(["tere", "tere", "tulemast"]) => ["tere#1", "tere#2", "tulemast#1"]
    word_numeration(["Tere", "tere", "tulemast"]) => ["Tere#1", "tere#2", "tulemast#1"]
    word_numeration(["Tere", "tere", "tulemast", "no", "tere", "TERE"]) => ["Tere#1", "tere#2", "tulemast#1", "no#1", "tere#3", "TERE#4"]

    :param words: A list of strings.
    :return: List of string with numeration.
    """
    runtime = len(words)
    while runtime != 0:
        words.append(words)
        runtime -= 1
    return words


if __name__ == '__main__':
    print(middle_way([1, 2, 3], [4, 5, 6]))
    print(non_start('Hello', 'There'))
    print(in1to10(5, False))
    print(remove_nth_symbol("tere", 1))
    print(word_numeration(["tere", "tere", "tulemast"]))
