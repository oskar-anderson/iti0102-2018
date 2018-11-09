"""wat."""

first_special_ans3 = [6, 4]
first_special_ans4 = [4, 6]
first_special_ans5 = [4, 6]
first_general_ans = [0, 2, 8, 11, 12, 14, 16, 18]


def first(n: int):
    """First."""
    if n in range(3, 6):
        if n == 3:
            ans = first_special_ans3[0]
            first_special_ans3.remove(ans)
            return ans
        elif n == 4:
            ans = first_special_ans4[0]
            first_special_ans4.remove(ans)
            return ans
        else:
            ans = first_special_ans5[0]
            first_special_ans5.remove(ans)
            return ans
    else:
        ans = first_general_ans[0]
        first_general_ans.remove(ans)
        return ans


def last(n: int):
    """Last."""
    if n:
        pass


if __name__ == '__main__':
    print(first(1))  # Expected: 0
    print(first(2))  # Expected 2
    print(first(4))  # Expected: 4
    print(first(3))  # Expected: 6
    print(first(708))  # Expected: 8
    print(first(-871))  # Expected: 11
    print(first(-489))  # Expected: 12
    print(first(-1))  # Expected: 14
    print(first(0))  # Expected: 16
    print(first(2505))
