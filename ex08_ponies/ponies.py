"""Ponies."""
import base64
import re
import operator


def write(input_file: str, kind: str):
    """Write."""
    pony_value_list = read(input_file)
    print(f"Pony value list:    {pony_value_list}")
    filtered_by_location = filter_by_location(pony_value_list)
    print(f"Filter by location: {filtered_by_location}")
    double_filtered_value_list = filter_by_kind(filtered_by_location, kind)
    print(f"Filter by kind:     {double_filtered_value_list}")
    evaluated_ponies = evaluate_ponies(double_filtered_value_list)
    print(f"Evaluate ponies:    {evaluated_ponies}")
    sorted_by_name = sort_by_name(evaluated_ponies)
    print(f"Sort by name:       {sorted_by_name}")
    unformatted_table_content = sort_by_points(sorted_by_name)
    print(f"Sort by points:     {unformatted_table_content}")

    output_filename = f"result_for_{kind}.txt"
    print(f"output filename: {output_filename}")
    output_file = open(output_filename, "w")
    separator = ("-" * 128)
    title_line = ("PLACE" + " " * 5 + "POINTS" + " " * 4 + "NAME" + " " * 16 + "KIND" + " " * 16 + "COAT COLOR"
                  + " " * 10 + "MANE COLOR" + " " * 10 + "EYE COLOR" + " " * 11 + "LOCATION")
    new_line = "\n"
    formatted_table = []
    for i in range(len(unformatted_table_content)):
        formatted_table.append(format_line(unformatted_table_content[i], i))
    table_contents = f"{title_line}\n{separator}\n{new_line.join(formatted_table)}"
    output_file.write(table_contents)
    output_file.close()


def format_line(pony: dict, place: int) -> str:
    """Format main table content."""
    main_content = (f"""{str(place + 1)}{
    str(" " * (10 - len(str(place + 1))))}{
    str(pony.get("points"))}{
    " " * (10 - len(str(pony.get("points"))))}{
    pony.get("name")}{
    " " * (20 - len(str(pony.get("name"))))}{
    pony.get("kind")}{
    " " * (20 - len(str(pony.get("kind"))))}{
    pony.get("coat color")}{
    " " * (20 - len(str(pony.get("coat color"))))}{
    pony.get("mane color")}{
    " " * (20 - len(str(pony.get("mane color"))))}{
    pony.get("eye color")}{
    " " * (20 - len(str(pony.get("eye color"))))}{
    pony.get("location")}""")
    return main_content


def read(read_file: str) -> list:
    """Read file and return list of decoded dictionaries."""
    try:
        read_file = open(read_file, "r")
    except FileNotFoundError:
        raise SystemExit("File not found!")
#    print(read_file.readline())    # print messes files up, why?
    read_file = read_file.readlines()
    read_file = [line.strip() for line in read_file]    # removes whitespace
#    return extract_information(decode(read_file[2]))   # 0 and 1 are title line and separator
    pony_value_list = []
    for i in range(2, len(read_file)):
        decoded_line = decode(read_file[i])
        attribute_dict = extract_information(decoded_line)
        pony_value_list.append(attribute_dict)
    return pony_value_list


def decode(line: str) -> str:
    """Decode string in base64."""
    # "gICA" is separator.
    line = base64.b64decode(line)
    line = line.decode("utf-8")
    return line


def extract_information(line: str) -> dict:
    """Make a pony attribute dict out of decoded string."""
    l_pony_attribute_values = []
    regex = r"([a-zA-Z]+ ?[a-zA-Z]+ ?[a-zA-Z]+)"
    for match in re.finditer(regex, str(line)):
        # print(match.group())
        l_pony_attribute_values.append(match.group())
    # print(l_pony_attribute_values)
    l_pony_dict_keys = ["name", "kind", "coat color", "mane color", "eye color", "location"]
    dict_pony_attributes = {}
    for i in range(len(l_pony_attribute_values)):
        dict_pony_attributes.setdefault(l_pony_dict_keys[i], l_pony_attribute_values[i])
    # print(dict_pony_attributes)
    return dict_pony_attributes


def filter_by_location(ponies: list) -> list:
    """Remove ponies with location value "None"."""
    filtered_ponies_by_loc = []
    for i in range(2, (len(ponies))):
        if ponies[i].get("location") == "None":
            pass
        else:
            filtered_ponies_by_loc.append(ponies[i])
    return filtered_ponies_by_loc

#    number_of_del_dicts = 0
#    for i in range(2, (len(ponies))):
#        i -= number_of_del_dicts        # otherwise skips list item after deletion
#        if len(ponies) == i:             # does not seem to be necessary with previos line
#            break

#        print(f"i: {i}")
#        print(f"Len: {len(ponies)}")

#        if ponies[i].get("location") == "None":
#            del ponies[i]
#            # print("deleted")
#            number_of_del_dicts += 1
#    return ponies


def filter_by_kind(ponies: list, kind: str) -> list:
    """Filter all ponies leaving the ones with matching kinds."""
    filtered_ponies_by_kind = []        # uses append instead of del like in filter_by_location
    for i in range(2, (len(ponies))):
        if ponies[i].get("kind") == kind:
            filtered_ponies_by_kind.append(ponies[i])
    return filtered_ponies_by_kind


def get_points_for_color(color: str):
    """Get points according to specific pony color."""
    color_list = ['magenta', 'pink', 'purple', 'orange', 'red', 'yellow', 'cyan', 'blue', 'brown', 'green']
    try:
        number = 10 - color_list.index(color)
    except ValueError:
        return None
    if number < 5:
        return None
    return number


def add_points(pony: dict) -> dict:
    """Add points from function get_points_for_color to pony attribute dictionary."""
    evaluation_locations = {
        'coat_color': ['Town Hall', 'Theater', 'School of Friendship'],
        'mane_color': ['Schoolhouse', 'Crusaders Clubhouse', 'Golden Oak Library'],
        'eye_color': ['Train station', 'Castle of Friendship', 'Retirement Village']
    }
    if pony.get("location") in evaluation_locations.get("coat_color"):
        points = get_points_for_color(pony.get("coat color"))
    elif pony.get("location") in evaluation_locations.get("mane_color"):
        points = get_points_for_color(pony.get("mane color"))
    elif pony.get("location") in evaluation_locations.get("eye_color"):
        points = get_points_for_color(pony.get("eye color"))
    else:
        print("Wrong location: " + pony.get("location"))
        points = None
    pony.update({"points": points})
    return pony


def evaluate_ponies(ponies: list) -> list:
    """Add points for all ponies into list dictionaries."""
    pony_attribute_list_with_points = []
    for i in range(len(ponies)):
        pony_attribute_list_with_points.append(add_points(ponies[i]))
    return pony_attribute_list_with_points


def sort_by_name(ponies: list) -> list:
    """Sort pony list by name."""
    sorted_pony_list_by_name = sorted(ponies, key=operator.itemgetter('name'))
#    sorted_pony_list_by_name.append(ponies.sort(key=operator.itemgetter("name")))
    return sorted_pony_list_by_name


def sort_by_points(ponies: list) -> list:
    """Sort pony list by decreasing points."""
    ponies_with_points = []
    for i in range(len(ponies)):
        if ponies[i].get("points") is not None:
            ponies_with_points.append(ponies[i])
    sorted_pony_list_by_points = sorted(ponies_with_points, key=operator.itemgetter('points'), reverse=True)
    return sorted_pony_list_by_points


if __name__ == '__main__':
    print(decode('TWF1ZCBQb21tZWwgICAgICAgICBVbmljb3JuICAgICAgICAgICAgIHBpbmsgICAgICAgICAgICAgICAgZ3JlZW4gICAgICAgICA'
                 + 'gICAgICBjeWFuICAgICAgICAgICAgICAgIENhc3RsZSBvZiBGcmllbmRzaGlw'))
    print(write("näidis_sisendfail.txt", "Alicorn"))
