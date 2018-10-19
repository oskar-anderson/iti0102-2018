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
    regex = r"(\d+)([\D])(\d+)[ \n]* ([a-zA-Z]*)"
    dict1 = {}
    for match in re.finditer(regex, input_string):
        if int(match.group(1)) in range(24) and len(match.group(1)) in [1, 2] and int(match.group(3)) in range(60) \
                and len(match.group(3)) in [1, 2]:
            if int(match.group(1)) < 12 or int(match.group(1)) == 12 and int(match.group(3)) == 0:
                time = match.group(1).zfill(2) + ":" + match.group(3).zfill(2) + " AM"
            else:
                time = str(int(match.group(1)) - 12).zfill(2) + ":" + match.group(3).zfill(2) + " PM"
            string = match.group(4).lower()
            dict1.setdefault(time, [])
            if string not in dict1[time]:
                dict1.setdefault(time, []).append(string)
    if dict1 == {}:
        return no_items_found()
    proper_value_list = create_value_list(dict1)
    sorted_time_list = sort_time_list(dict1)
    max_value_lenght = find_max_lenght(proper_value_list)
    new_line = "\n"
    separator = (max_value_lenght + 13) * "-"   # 13 == 8 + 2 for time + 3 for "|"
    title_line = f"|" + (5 * " ") + "time | items" + ((max_value_lenght - 6) * " ") + "|"
    main_content = create_main_schedule_content(max_value_lenght, sorted_time_list, dict1)
    result = f"""{separator}\n{title_line}\n{separator}\n{new_line.join(main_content)}\n{separator}"""
    print(result)
    return result


def create_main_content_of_table(value_max_lenght, sorted_time_list, dict1):
    """Create main part of schedule."""
    string_list = []
    for time in sorted_time_list:
        string_list.append((f"""| {time} | {", ".join(dict1[time])}"""
                            f"""{(value_max_lenght - ((len(", ".join(dict1[time]))) + 1)) * " "}|"""))
    return string_list


def sort_time_list(dict1):
    """Create sorted time list from given dictionary."""
    time_am = []
    time_pm = []
    for time in sorted(dict1):
        if "AM" in time:
                time_am.append(time)
        elif "PM" in time:
                time_pm.append(time)
    list_of_sorted_times = time_am + time_pm
    return list_of_sorted_times


def create_value_list(dict1):
    """Put dictionary values into proper format for schedule."""
    old_value_list = list(dict1.values())
    value_list = []
    for i in range(len(old_value_list)):
        value_list.append(", ".join(old_value_list[i]))
    return value_list


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


def create_main_schedule_content(value_max_lenght, sorted_time_list, dict1):
    """Create main content of schedule."""
    main_schedule_content = []
    for time in sorted_time_list:
        main_schedule_content.append(f"""| {time} | {", ".join(dict1[time])}{(value_max_lenght -
        ((len(", ".join(dict1[time]))) + 1)) * " "}|""")
    return main_schedule_content


if __name__ == '__main__':
    print(create_schedule_string("11:00 teine tekst 11:0 jah ei 10:00 pikktekst "))
    create_schedule_file("schedule_input.txt", "schedule_output.txt")
