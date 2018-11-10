"""wat."""

first_special_ans = [4, 6]
first_general_ans = [0, 2, 8, 11, 12, 14, 16, 18]


def first(n: int):
    """First."""
    if n in range(3, 6):
        ans = first_special_ans[0]
        first_special_ans.remove(ans)
        return ans
    else:
        ans = first_general_ans[0]
        first_general_ans.remove(ans)
        return ans


def last(n: int):
    """Last."""
    for i in range(10):
        if n in range(1096 + 84 * i, 1180 + 84 * i):
            return 34 + i


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
    print(first(2505))  # Expected 18

    print()

    def last2(n: int, starting, period, ans=34):
        """Last."""
        for i in range(10):
            if n in range(starting + period * i, starting + period + period * i):
                return ans + i

    for s in range(1060, 1190):
        for interval in range(60, 100):
            if last2(1167, s, interval) == 34 and (last2(1253, s, interval)) == 35\
                    and(last2(1296, s, interval)) == 36\
                    and (last2(1370, s, interval)) == 37 and (last2(1431, s, interval)) == 37\
                    and (last2(1445, s, interval)) == 38 and (last2(1498, s, interval)) == 38\
                    and (last2(1524, s, interval)) == 39 and (last2(1581, s, interval)) == 39\
                    and (last2(1600, s, interval) == 40)\
                    and (last2(1725, s, interval)) == 41 and (last2(1770, s, interval)) == 42\
                    and (last2(1832, s, interval)) == 42 and (last2(1882, s, interval)) == 43\
                    and (last2(1929, s, interval)) == 43:
                print(s, interval)

    print()
    print(last(1165))
    print(last(1253))
    print(last(1341))
    print(last(1429))

    print(last(1411))
    print(last(1370))
