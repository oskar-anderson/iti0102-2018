"""Check if given ID code is valid."""


def check_your_id(id_code: str):
    """
    Check if given ID code is valid and return the result.

    :param id_code: str
    :return: boolean
    """
    if id_code.isupper() or id_code.islower():
        return False
    elif int(id_code) in range(100000000000) and int(id_code) not in range(10000000000)\
            and check_gender_number(int(id_code[0])) is True and check_control_number(id_code) is True \
            and check_day_number(10 * int(id_code[1]) + int(id_code[2]),
                                 10 * int(id_code[3]) + int(id_code[4]),
                                 10 * int(id_code[5]) + int(id_code[6])):
        # Checking year number and born order is useless.
        # check_day_number also checks months and leap years
        return True
    else:
        return False


def check_gender_number(gender_number: int):
    """
    Check if given value is correct for gender number in ID code.

    :param gender_number: int
    :return: boolean
    """
    if gender_number == 0 or gender_number == 7 or gender_number == 8 or gender_number == 9:
        return False
    else:
        return True


def check_year_number_two_digits(year_number: int):
    """
    Check if given value is correct for year number in ID code.

    :param year_number: int
    :return: boolean
    """
    if year_number in range(100):
        return True
    else:
        return False


def check_month_number(month_number: int):
    """
    Check if given value is correct for month number in ID code.

    :param month_number: int
    :return: boolean
    """
    if month_number in range(13):
        return True
    else:
        return False


def check_day_number(year_number: int, month_number: int, day_number: int):
    """
    Check if given value is correct for day number in ID code.

    Also, consider leap year and which month has 30 or 31 days.

    :param year_number: int
    :param month_number: int
    :param day_number: int
    :return: boolean
    """
    if day_number <= 31\
        and month_number == 1\
        or day_number <= 31\
        and month_number == 3\
        or day_number <= 31\
        and month_number == 5\
        or day_number <= 31\
        and month_number == 7\
        or day_number <= 31\
        and month_number == 8\
        or day_number <= 31\
        and month_number == 10\
        or day_number <= 31\
            and month_number == 12:
        return True
    # Note to self: "or" condition does not take previous "and" conditions along.

    elif day_number <= 30\
        and month_number == 4\
        or day_number <= 30\
        and month_number == 6\
        or day_number <= 30\
        and month_number == 9\
        or day_number <= 30\
            and month_number == 11:
        return True

#    Same thing different style
#    elif day_number <= 30\
#    and month_number == 4:
#        return "true"
#    elif day_number <= 30\
#    and month_number == 6:
#        return "true"
#    elif day_number <= 30\
#    and month_number == 9:
#        return "true"
#    elif day_number <= 30\
#    and month_number == 11:
#        return "true"

    elif month_number == 2\
        and year_number % 400 == 0\
            and day_number <= 29:
        return True

    elif month_number == 2\
        and year_number % 100 == 0\
            and day_number <= 28:
        return True

    elif month_number == 2\
        and year_number % 4 == 0\
            and day_number <= 29:
        return True

    else:
        return False


def check_leap_year(year_number: int):
    """
    Check if given year is a leap year.

    :param year_number: int
    :return: boolean
    """
    if year_number % 400 == 0:
        return True

    elif year_number % 100 == 0:
        return False

    elif year_number % 4 == 0:
        return True
    else:
        return False


def check_born_order(born_order: int):
    """
    Check if given value is correct for born order number in ID code.

    :param born_order: int
    :return: boolean
    """
    if born_order in range(1000):
        return True
    else:
        return False


def check_control_number(id_code: str):
    """
    Check if given value is correct for control number in ID code.

    Use algorithm made for creating this number.

    :param id_code: string
    :return: boolean
    """
    if ((int(id_code[9]) * 1 + int(id_code[8]) * 9 + int(id_code[7]) * 8 + int(id_code[6]) * 7 + int(id_code[5]) * 6
         + int(id_code[4]) * 5 + int(id_code[3]) * 4 + int(id_code[2]) * 3 + int(id_code[1]) * 2
         + int(id_code[0]) * 1) % 11) == 10 and ((int(id_code[9]) * 3 + int(id_code[8]) * 2
                                                  + int(id_code[7]) * 1 + int(id_code[6]) * 9
                                                  + int(id_code[5]) * 8 + int(id_code[4]) * 7
                                                  + int(id_code[3]) * 6 + int(id_code[2]) * 5
                                                  + int(id_code[1]) * 4 + int(id_code[0]) * 3) % 11) == 10\
            and int(id_code[10]) == 0:
        return True
    elif ((int(id_code[9]) * 1 + int(id_code[8]) * 9 + int(id_code[7]) * 8 + int(id_code[6]) * 7 + int(id_code[5]) * 6
           + int(id_code[4]) * 5 + int(id_code[3]) * 4 + int(id_code[2]) * 3 + int(id_code[1]) * 2
           + int(id_code[0]) * 1) % 11) == 10 and ((int(id_code[9]) * 3 + int(id_code[8]) * 2
                                                    + int(id_code[7]) * 1 + int(id_code[6]) * 9
                                                    + int(id_code[5]) * 8 + int(id_code[4]) * 7
                                                    + int(id_code[3]) * 6 + int(id_code[2]) * 5
                                                    + int(id_code[1]) * 4 + int(id_code[0]) * 3) % 11)\
            == int(id_code[10]):
        return True
    elif ((int(id_code[9]) * 1 + int(id_code[8]) * 9 + int(id_code[7]) * 8 + int(id_code[6]) * 7 + int(id_code[5]) * 6
           + int(id_code[4]) * 5 + int(id_code[3]) * 4 + int(id_code[2]) * 3 + int(id_code[1]) * 2
           + int(id_code[0]) * 1) % 11) == 10 and int(id_code[10]) == 0:
        return True
    elif ((int(id_code[9]) * 1 + int(id_code[8]) * 9 + int(id_code[7]) * 8 + int(id_code[6]) * 7 + int(id_code[5]) * 6
           + int(id_code[4]) * 5 + int(id_code[3]) * 4 + int(id_code[2]) * 3 + int(id_code[1]) * 2
           + int(id_code[0]) * 1) % 11) == int(id_code[10]):
        return True
    else:
        return False


if __name__ == '__main__':
    print("Overall ID check:")
    print(check_your_id("4980827k244"))  # this is mine
    print(check_your_id("49808270244"))  # -> True
    personal_id = "39809200287"  # type your own id in command prompt
    print(check_your_id(personal_id))  # -> True
    print(check_your_id("12345678901"))  # -> False
    print("\nGender number:")
    for i in range(10):  # changed 9 to 10
        print(f"{i} {check_gender_number(i)}")
        # 0 -> False
        # 1...6 -> True
        # 7...8 -> False
    print("\nYear number:")
    print(check_year_number_two_digits(100))  # -> False
    print(check_year_number_two_digits(50))  # -> true
    print("\nMonth number:")
    print(check_month_number(2))  # -> True
    print(check_month_number(15))  # -> False
    print("\nDay number:")
    print(check_day_number(2005, 12, 25))  # -> True
    print(check_day_number(1910, 8, 32))  # -> False
    print(check_leap_year(1804))  # -> True
    print(check_leap_year(1800))  # -> False
    print("\nFebruary check:")
    print(check_day_number(1996, 2, 30))  # -> False (February cannot contain more than 29 days in any circumstances)
    print(check_day_number(2099, 2, 29))  # -> False (February contains 29 days only during leap year)
    print(check_day_number(2008, 2, 29))  # -> True
    print("\nMonth contains 30 or 31 days check:")
    print(check_day_number(1822, 4, 31))  # -> False (April contains max 30 days)
    print(check_day_number(2018, 10, 31))  # -> True
    print(check_day_number(1915, 9, 31))  # -> False (September contains max 30 days)
    print("\nBorn order number:")
    print(check_born_order(0))  # -> True
    print(check_born_order(850))  # -> True
    print("\nControl number:")
    print(check_control_number("49808270244"))  # -> True
    print(check_control_number("60109200187"))  # -> False, it must be 6


def get_data_from_id(id_code: str):
    """
    Get possible information about the person.

    Use given ID code and return a short message.
    Follow the template - This is a (gender) born on (DD.MM.YYYY).

    :param id_code: str
    :return: str
    """
    if check_control_number(id_code) is True:
        return "This is a " + get_gender(int(id_code[0])) + " born on " + str(10 * int(id_code[5]) + int(id_code[6])) +\
               "." + str(10 * int(id_code[3]) + int(id_code[4])) + "." + str(get_full_year(int(id_code[0]),
                                                                                           ((10 * int(id_code[1]))
                                                                                            + (int(id_code[2])))))
    else:
        return "Given invalid ID code!"


def get_gender(gender_number: int):
    """
    Define the gender according to the number from ID code.

    :param gender_number: int
    :return: str
    """
    if gender_number == 1:
        return "male"
    elif gender_number == 3:
        return "male"
    elif gender_number == 5:
        return "male"
    elif gender_number == 2:
        return "female"
    elif gender_number == 4:
        return "female"
    elif gender_number == 6:
        return "female"
    else:
        print("Given invalid ID code!")


def get_full_year(gender_number: int, year: int):
    """
    Define the 4-digit year when given person was born.

    Person gender and year numbers from ID code must help.
    Given year has only two last digits.

    :param gender_number: int
    :param year: int
    :return: int
    """
    if gender_number == 1:
        return 1800 + year
    elif gender_number == 2:
        return 1800 + year
    elif gender_number == 3:
        return 1900 + year
    elif gender_number == 4:
        return 1900 + year
    elif gender_number == 5:
        return 2000 + year
    elif gender_number == 6:
        return 2000 + year
    else:
        print("Given invalid ID code!")


if __name__ == '__main__':
    print("\nFull message:")
    print(get_data_from_id("49808270244"))  # -> "This is a female born on 27.08.1998"
    print(get_data_from_id("60109200187"))  # -> "Given invalid ID code!"
    print(get_full_year(1, 28))  # -> 1828
    print(get_full_year(4, 85))  # -> 1985
    print(get_full_year(5, 1))  # -> 2001
    print(get_gender(2))  # -> "female"
    print(get_gender(5))  # -> "male"
