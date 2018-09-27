"""Adding."""


def get_max_element(int_list):
    """
    Return the maximum element in the list.

    If the list is empty return None.
    :param int_list: List of integers
    :return: largest int
    """
    if len(int_list) == 0:
        return None
    best = int_list[0]
    for element in int_list:
        if best < element:
            best = element
    return best


def get_min_element(int_list):
    """
    Return the minimum element in list.

    If the list is empty return None.
    :param int_list: List of integers
    :return: Smallest int
    """
    if len(int_list) == 0:
        return None
    worst = int_list[0]
    for element in int_list:
        if worst > element:
            worst = element
    return worst


def sort_list(int_list):
    """
    Sort the list in descending order.

    :param int_list: List of integers
    :return: Sorted list of integers
    """
    new_list = []
    list2 = list(int_list)
    element_count = len(list2)
    for _ in range(element_count):
        max_element = get_max_element(list2)
        list2.remove(max_element)
        new_list.append(max_element)
    return new_list


def add_list_elements(int_list):
    """
    Create a new sorted list of the sums of minimum and maximum elements.

    Add together the minimum and maximum element of int_list and add that sum to a new list
    Repeat the process until all elements in the list are used, ignore the median number
    if the list contains uneven amount of elements.
    Sort the new list in descending order.
    This function must use get_min_element(), get_max_element() and sort_list() functions.
    :param int_list: List of integers
    :return: Integer list of sums sorted in descending order.
    """
    new_list = []
    list2 = list(int_list)
    for i in range(len(int_list) // 2):
        min_element = get_min_element(list2)
        max_element = get_max_element(list2)
        sum_element = min_element + max_element
        list2.remove(min_element)
        list2.remove(max_element)
        new_list.append(sum_element)
    return sort_list(new_list)


if __name__ == '__main__':
    print(add_list_elements([0, 0, 0, 0, 0, 0, 1, 2, 5, 6]))  # -> [6, 5, 2, 1, 0]
    print(add_list_elements([-1, -2, -5, -50, -14]))  # -> [-16, -51]
    print(add_list_elements([1]))  # -> []
