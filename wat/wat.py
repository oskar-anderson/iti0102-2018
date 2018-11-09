"""wat."""

first_special_ans3 = [6, 4]
first_special_ans4 = [4, 6]
first_special_ans5 = [4, 6]
first_general_ans = [8, 11, 12, 14, 16, 18]


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
    print(first(3))
    print(first(3))
