"""Create schedule from the given file."""
import re


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    input_data = open(input_filename, "r").read()
    output_file = open(output_filename, "w")
    output_file.write(create_schedule_string(input_data))
    output_file.close()


def create_schedule_string(input_string: str) -> str:
    """Create schedule string_lower from the given input string_lower."""
    regex = r"\s([\d]{1,2})[\D]([\d]{1,2})\s+([a-zA-Z]+)"
    dict_time_and_str_w_zfill = {}
    for match in re.finditer(regex, input_string):
        if int(match.group(1)) in range(24) and int(match.group(2)) in range(60):
            if int(match.group(1)) == 0:
                time = str(int(match.group(1)) + 12) + ":" + match.group(2).zfill(2) + " AM"
            elif int(match.group(1)) < 12:
                time = match.group(1).zfill(2) + ":" + match.group(2).zfill(2) + " AM"
            else:
                time = str(int(match.group(1)) - 12).zfill(2) + ":" + match.group(2).zfill(2) + " PM"
            string_lower = match.group(3).lower()
            dict_time_and_str_w_zfill.setdefault(time, [])
            if string_lower not in dict_time_and_str_w_zfill[time]:
                dict_time_and_str_w_zfill.setdefault(time, []).append(string_lower)
    if dict_time_and_str_w_zfill == {}:
        return no_items_found()

    dict_time_and_str_wo_zfill = get_dict_time_and_str_wo_zfill(input_string)
    print(dict_time_and_str_wo_zfill)
    proper_value_list = create_value_list(dict_time_and_str_w_zfill)
    sorted_time_list = sort_time_list(dict_time_and_str_w_zfill)
    # print("sorted_time_list: " + str(sorted_time_list))
    max_time_lenght = find_max_time_lenght(sorted_time_list)
    print(f"max_time_lenght: {max_time_lenght}")
    max_value_lenght = find_max_lenght(proper_value_list)
    new_line = "\n"
    separator = (max_time_lenght + max_value_lenght + 3) * "-"
    title_line = f"|" + ((max_time_lenght - 5) * " ") + "time | items" + ((max_value_lenght - 6) * " ") + "|"
    main_content = create_main_schedule_content(max_time_lenght, max_value_lenght, sorted_time_list,
                                                dict_time_and_str_wo_zfill)
    result = f"{separator}\n{title_line}\n{separator}\n{new_line.join(main_content)}\n{separator}"
    print(result)
    # print("result type: " + str(type(result)))
    return result


def get_dict_time_and_str_wo_zfill(input_string):
    """Make a new dict with no zfill for hours."""
    dict_time_and_str_wo_zfill = {}
    regex = r"\s+([\d]{1,2})[\D]([\d]{1,2})\s+([a-zA-Z]+)"
    for match in re.finditer(regex, input_string):
        if int(match.group(1)) in range(24) and int(match.group(2)) in range(60):
            if int(match.group(1)) == 0:
                time = str(int(match.group(1)) + 12) + ":" + match.group(2).zfill(2) + " AM"
            elif int(match.group(1)) < 12:
                if (match.group(1)[0]) == "0":
                    # print("match.group with zero: " + str(match.group(1)))
                    remove_first_digit_zero = []
                    list_hour_digits = list(match.group(1))
                    list_hour_digits[0] = ""
                    remove_first_digit_zero.append("".join(list_hour_digits))
                    # print("remove_first_digit_zero: " + str(remove_first_digit_zero))
                    time = str(remove_first_digit_zero).strip("[]'") + ":" + match.group(2).zfill(2) + " AM"
                    # print(time)
                else:
                    time = match.group(1) + ":" + match.group(2).zfill(2) + " AM"
            else:
                if (match.group(1)[0]) == "0":
                    # print("match.group with zero: " + str(match.group(1)))
                    remove_first_digit_zero = []
                    list_hour_digits = list(match.group(1))
                    list_hour_digits[0] = ""
                    remove_first_digit_zero.append("".join(list_hour_digits))
                    # print("remove_first_digit_zero: " + str(remove_first_digit_zero))
                    time = str(remove_first_digit_zero).strip("[]'") + ":" + match.group(2).zfill(2) + " PM"
                    # print(time)
                else:
                    time = str(int(match.group(1)) - 12) + ":" + match.group(2).zfill(2) + " PM"
            string_lower = match.group(3).lower()
            dict_time_and_str_wo_zfill.setdefault(time, [])
            if string_lower not in dict_time_and_str_wo_zfill[time]:
                dict_time_and_str_wo_zfill.setdefault(time, []).append(string_lower)
    return dict_time_and_str_wo_zfill


def sort_time_list(dict_time_and_name_w_zfill):
    """Create sorted time list from given dictionary."""
    twelve_am = []
    time_am = []
    time_pm = []
    print(f"Sorted dict: {sorted(dict_time_and_name_w_zfill)}")
    for time in sorted(dict_time_and_name_w_zfill):
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
            listify_time = list(list_of_sorted_times[i])
            listify_time[0] = ""
            # print("listify_time: " + str(listify_time))
            remove_first_digit_zero.append("".join(listify_time))
            # print("remove_first_digit_zero: " + str(remove_first_digit_zero))
        else:
            remove_first_digit_zero.append(list_of_sorted_times[i])
    # print(list_of_sorted_times)
    # print(remove_first_digit_zero)
    return remove_first_digit_zero


def create_value_list(dict_time_and_name_w_zfill):
    """Put dictionary values into proper format for schedule."""
    old_value_list = list(dict_time_and_name_w_zfill.values())
    value_list = []
    for i in range(len(old_value_list)):
        value_list.append(", ".join(old_value_list[i]))
    return value_list


def find_max_time_lenght(sorted_time_list):
    """Find lenght of longest time."""
    max_time_lenght = 0
    print("sorted_time_list: " + str(sorted_time_list))
    for time in sorted_time_list:
        current_time_lenght = len(time)
        if max_time_lenght < current_time_lenght:
            max_time_lenght = current_time_lenght
    max_time_lenght += 2
    if max_time_lenght < 6:
        max_time_lenght = 6
    return max_time_lenght


def find_max_lenght(list_of_values):
    """Find lenght of longest value."""
    max_str_lenght = 0
    for value in list_of_values:
        current_str_lenght = len(value)
        if max_str_lenght < current_str_lenght:
            max_str_lenght = current_str_lenght
    max_str_lenght += 2
    if max_str_lenght < 7:
        max_str_lenght = 7
    return max_str_lenght


def no_items_found():
    """print "No items found" if dict is empty."""
    separator_line = "------------------"
    title_line = f"|  time | items  |"
    main_content = f"| No items found |"
    return f"{separator_line}\n{title_line}\n{separator_line}\n{main_content}\n{separator_line}"


def create_main_schedule_content(max_time_lenght, max_str_lenght, sorted_time_list, dict_time_and_name_wo_zfill):
    """Create main content of schedule."""
    main_schedule_content = []
    for time in sorted_time_list:
        main_schedule_content.append(f"""|{(max_time_lenght - len(time) - 1) * " "}{time} | {", ".join(dict_time_and_name_wo_zfill[time])}{(
        max_str_lenght - ((len(", ".join(dict_time_and_name_wo_zfill[time]))) + 1)) * " "}|""")
    return main_schedule_content


if __name__ == '__main__':
    print(create_schedule_string("11:00 teine tekst 11:0 jah ei 10:00 pikktekst "))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
