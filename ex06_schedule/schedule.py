"""Create schedule from the given file."""
import re


def create_schedule_file(input_filename: str, output_filename: str) -> None:
    """Create schedule file from the given input file."""
    input_data = open(input_filename, "r").read()
    output_file = open(output_filename, "w")
    output_file.write(create_schedule_string(input_data))
    output_file.close()


def create_schedule_string(input_string: str) -> str:
    """Create time string pair dictionary and schedule string from the given input lowerized string."""
    regex = r"\s+([\d]{1,2})[\D]([\d]{1,2})\s+([a-zA-Z]+)"
    dict_time_and_str = {}
    for match in re.finditer(regex, input_string):
        if int(match.group(1)) in range(24) and int(match.group(2)) in range(60):
            if int(match.group(1)) == 0:
                time = str(int(match.group(1)) + 12) + ":" + match.group(2).zfill(2) + " AM"
            elif int(match.group(1)) == 12:
                time = str(int(match.group(1))) + ":" + match.group(2).zfill(2) + " PM"
            elif int(match.group(1)) < 12:
                if (match.group(1)[0]) == "0":
                    remove_first_digit_zero = []
                    list_hour_digits = list(match.group(1))
                    list_hour_digits[0] = ""
                    remove_first_digit_zero.append("".join(list_hour_digits))
                    time = str(remove_first_digit_zero).strip("[]'") + ":" + match.group(2).zfill(2) + " AM"
                else:
                    time = match.group(1) + ":" + match.group(2).zfill(2) + " AM"
            else:
                if (match.group(1)[0]) == "0":
                    remove_first_digit_zero = []
                    list_hour_digits = list(match.group(1))
                    list_hour_digits[0] = ""
                    remove_first_digit_zero.append("".join(list_hour_digits))
                    time = str(remove_first_digit_zero).strip("[]'") + ":" + match.group(2).zfill(2) + " PM"
                else:
                    time = str(int(match.group(1)) - 12) + ":" + match.group(2).zfill(2) + " PM"
            string_lower = match.group(3).lower()
            dict_time_and_str.setdefault(time, [])
            if string_lower not in dict_time_and_str[time]:
                dict_time_and_str.setdefault(time, []).append(string_lower)
    if dict_time_and_str == {}:
        return no_items_found()

    proper_value_list = create_value_list(dict_time_and_str)
    sorted_time_list = sort_time_list(dict_time_and_str)
    # print("sorted_time_list: " + str(sorted_time_list))
    max_time_lenght = find_max_time_lenght(sorted_time_list)
    max_value_lenght = find_max_lenght(proper_value_list)
    new_line = "\n"
    separator = (max_time_lenght + max_value_lenght + 3) * "-"
    title_line = f"|" + ((max_time_lenght - 5) * " ") + "time | items" + ((max_value_lenght - 6) * " ") + "|"
    main_content = create_main_schedule_content(max_time_lenght, max_value_lenght, sorted_time_list,
                                                dict_time_and_str)
    result = f"{separator}\n{title_line}\n{separator}\n{new_line.join(main_content)}\n{separator}"
    print(result)
    # print("result type: " + str(type(result)))
    return result


def sort_time_list(dict_time_and_name):
    """Create sorted time list from given dictionary."""
    twelve_am = []
    time_am = []
    ten_and_eleven_am = []
    twelve_pm = []
    time_pm = []
    ten_and_eleven_pm = []
    # print(f"Sorted dict: {sorted(dict_time_and_name)}")
    for time in sorted(dict_time_and_name):
        if "12:" in time and "AM" in time:
            twelve_am.append(time)
        elif "10:" in time and "AM" in time or "11:" in time and "AM" in time:
            ten_and_eleven_am.append(time)
        elif "AM" in time:
            time_am.append(time)
        elif "12:" in time and "PM" in time:
            twelve_pm.append(time)
        elif "10:" in time and "PM" in time or "11:" in time and "PM" in time:
            ten_and_eleven_pm.append(time)
        elif "PM" in time:
            time_pm.append(time)
    list_of_sorted_times = twelve_am + time_am + ten_and_eleven_am + twelve_pm + time_pm + ten_and_eleven_pm
    return list_of_sorted_times


def create_value_list(dict_time_and_name):
    """Put dictionary values into proper format for schedule."""
    old_value_list = list(dict_time_and_name.values())
    value_list = []
    for i in range(len(old_value_list)):
        value_list.append(", ".join(old_value_list[i]))
    print(f"Value list: {value_list}")
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


def create_main_schedule_content(max_time_lenght, max_str_lenght, sorted_time_list, dict_time_and_name):
    """Create main content of schedule."""
    main_schedule_content = []
    for time in sorted_time_list:
        main_schedule_content.append(f"""|{(max_time_lenght - len(time) - 1) * " "}{time} | {", ".join(dict_time_and_name[time])}{(
        max_str_lenght - ((len(", ".join(dict_time_and_name[time]))) + 1)) * " "}|""")
    return main_schedule_content


if __name__ == '__main__':
    print(create_schedule_string("11:00 teine tekst 11:0 jah ei 10:00 pikktekst "))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
