"""Difference between loops and recursion."""


def recursive_sum(numbers: list) -> int:
    """
    Find out the sum of all the even numbers using recursion.
    :param numbers: list of randomly ordered numbers
    :return: sum of even numbers
    """
    if not numbers:
        return 0
    place_in_list = 0
    if numbers[place_in_list] % 2 == 0:
        return recursive_sum(numbers[1:]) + numbers[place_in_list]
    else:
        return recursive_sum(numbers[1:])


def loop_sum(numbers: list) -> int:
    """
    Find out the sum of all the even numbers using loops.

    :param numbers: list of randomly ordered numbers
    :return: sum of even numbers
    """
    sum_of_even_numbers = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            sum_of_even_numbers += numbers[i]
    return sum_of_even_numbers


def loop_reverse(s: str) -> str:
    """Reverse a string using a loop.

    :param s: string
    :return: reverse of s
    """
    reversed_string_list = []
    string_lenght = (len(s)) - 1
    for i in range(len(s)):
        reversed_string_list.append(s[string_lenght - i])
    new_string = "".join(reversed_string_list)
    return new_string


def recursive_reverse(s: str) -> str:
    """Reverse a string using recursion.

    :param s: string
    :return: reverse of s
    """
    if s == "":
        return ""
    string_lenght = len(s) - 1
    return s[string_lenght] + recursive_reverse(s[:string_lenght])


if __name__ == '__main__':
    print(recursive_sum([1, 3, 5, 7, 9]))
    print(recursive_sum([2, 4, 5, 8]))
    print(loop_sum([1, 3, 5, 7, 9]))
    print(loop_sum([2, 4, 5, 8]))
    print(recursive_reverse("abcdef"))
    print(loop_reverse("abcdef"))
