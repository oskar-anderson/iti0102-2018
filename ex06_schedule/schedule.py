"""Create schedule from the given file."""
import re


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    input_data = open(input_filename, "r").read()
    output_file = open(output_filename, "w")
    output_file.write(create_schedule_string(input_data))
    output_file.close()


def create_schedule_string(input_string: str) -> str:
    """Create schedule string from the given input string."""
    regex = r"\s+([\d]{1,2})[\D]([\d]{1,2})\s+([a-zA-Z]+)"
    dict1 = {}
    for match in re.finditer(regex, input_string):
        if int(match.group(1)) in range(24) and int(match.group(2)) in range(60):
            if int(match.group(1)) == 0:
                time = str(int(match.group(1)) + 12) + ":" + match.group(2).zfill(2) + " AM"
            elif int(match.group(1)) < 12:
                time = match.group(1).zfill(2) + ":" + match.group(2).zfill(2) + " AM"
            else:
                time = str(int(match.group(1)) - 12).zfill(2) + ":" + match.group(2).zfill(2) + " PM"
            string = match.group(3).lower()
            dict1.setdefault(time, [])
            if string not in dict1[time]:
                dict1.setdefault(time, []).append(string)
    if dict1 == {}:
        return no_items_found()
    # print("Dict1: " + str(dict1))

    dict2 = get_dict2(input_string)
    print(dict2)
    proper_value_list = create_value_list(dict1)
    sorted_time_list = sort_time_list(dict1)
    print("sorted_time_list: " + str(sorted_time_list))
    max_time_lenght = find_max_time_lenght(sorted_time_list)
    print("max_time_lenght: " + str(max_time_lenght))
    max_value_lenght = find_max_lenght(proper_value_list)
    new_line = "\n"
    separator = (max_time_lenght + max_value_lenght + 3) * "-"
    title_line = f"|" + ((max_time_lenght - 5) * " ") + "time | items" + ((max_value_lenght - 6) * " ") + "|"
    main_content = create_main_schedule_content(max_time_lenght, max_value_lenght, sorted_time_list, dict2)
    result = f"""{separator}\n{title_line}\n{separator}\n{new_line.join(main_content)}\n{separator}"""
    print(result)
    print("result type: " + str(type(result)))
    return result


def get_dict2(input_string):
    """Make a new list with no zfill for hours."""
    dict2 = {}
    regex = r"\s+([\d]{1,2})[\D]([\d]{1,2})\s+([a-zA-Z]+)"
    for match in re.finditer(regex, input_string):
        if int(match.group(1)) in range(24) and int(match.group(2)) in range(60):
            if int(match.group(1)) == 0:
                time = str(int(match.group(1)) + 12) + ":" + match.group(2).zfill(2) + " AM"
            elif int(match.group(1)) < 12:
                if (match.group(1)[0]) == "0":
                    # print("match.group with zero: " + str(match.group(1)))
                    remove_first_digit_zero = []
                    text1 = list(match.group(1))
                    text1[0] = ""
                    text2 = "".join(text1)
                    remove_first_digit_zero.append(text2)
                    # print("remove_first_digit_zero: " + str(remove_first_digit_zero))
                    time = str(remove_first_digit_zero).strip("[]'") + ":" + match.group(2).zfill(2) + " AM"
                    # print(time)
                else:
                    time = match.group(1) + ":" + match.group(2).zfill(2) + " AM"
            else:
                if (match.group(1)[0]) == "0":
                    # print("match.group with zero: " + str(match.group(1)))
                    remove_first_digit_zero = []
                    text1 = list(match.group(1))
                    text1[0] = ""
                    text2 = "".join(text1)
                    remove_first_digit_zero.append(text2)
                    # print("remove_first_digit_zero: " + str(remove_first_digit_zero))
                    time = str(remove_first_digit_zero).strip("[]'") + ":" + match.group(2).zfill(2) + " PM"
                    # print(time)
                else:
                    time = str(int(match.group(1)) - 12) + ":" + match.group(2).zfill(2) + " PM"
            string = match.group(3).lower()
            dict2.setdefault(time, [])
            if string not in dict2[time]:
                dict2.setdefault(time, []).append(string)
    return dict2


def sort_time_list(dict1):
    """Create sorted time list from given dictionary."""
    twelve_am = []
    time_am = []
    time_pm = []
    print(sorted(dict1))
    for time in sorted(dict1):
        if "12:" in time:
            twelve_am.append(time)
        elif "AM" in time:
            time_am.append(time)
        elif "PM" in time:
            time_pm.append(time)
    list_of_sorted_times = twelve_am + time_am + time_pm
    # print("list_of_sorted_times: " + str(list_of_sorted_times))
    remove_first_digit_zero = []
    for i in range(len(list_of_sorted_times)):
        # print((list_of_sorted_times[i])[0])
        if (list_of_sorted_times[i])[0] == "0":
            text1 = list(list_of_sorted_times[i])
            text1[0] = ""
            # print("text1: " + str(text1))
            text2 = "".join(text1)
            # print("text2: " + str(text2))
            remove_first_digit_zero.append(text2)
            # print("remove_first_digit_zero: " + str(remove_first_digit_zero))
        else:
            remove_first_digit_zero.append(list_of_sorted_times[i])
    # print(list_of_sorted_times)
    # print(remove_first_digit_zero)
    return remove_first_digit_zero


def create_value_list(dict1):
    """Put dictionary values into proper format for schedule."""
    old_value_list = list(dict1.values())
    value_list = []
    for i in range(len(old_value_list)):
        value_list.append(", ".join(old_value_list[i]))
    return value_list


def find_max_time_lenght(sorted_time_list):
    """Find lenght of longest time."""
    max_lenght = 0
    print("sorted_time_list: " + str(sorted_time_list))
    for time in sorted_time_list:
        current_lenght = len(time)
        if max_lenght < current_lenght:
            max_lenght = current_lenght
    max_lenght += 2
    if max_lenght < 6:
        max_lenght = 6
    return max_lenght


def find_max_lenght(list_of_values):
    """Find lenght of longest value."""
    max_lenght = 0
    for value in list_of_values:
        current_lenght = len(value)
        if max_lenght < current_lenght:
            max_lenght = current_lenght
    max_lenght += 2
    if max_lenght < 7:
        max_lenght = 7
    return max_lenght


def no_items_found():
    """print "No items found" if dict is empty."""
    separator_line = "------------------"
    title_line = f"|  time | items  |"
    main_content = f"| No items found |"
    return f"{separator_line}\n{title_line}\n{separator_line}\n{main_content}\n{separator_line}"


def create_main_schedule_content(time_max_lenght, value_max_lenght, sorted_time_list, dict2):
    """Create main content of schedule."""
    main_schedule_content = []
    for time in sorted_time_list:
        main_schedule_content.append(f"""|{(time_max_lenght - len(time) - 1) * " "}{time} | {", ".join(dict2[time])}{(
        value_max_lenght - ((len(", ".join(dict2[time]))) + 1)) * " "}|""")
    return main_schedule_content


if __name__ == '__main__':
    print(create_schedule_string("11:00 teine tekst 11:0 jah ei 10:00 pikktekst "))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
