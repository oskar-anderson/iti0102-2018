"""Ponies."""
import base64
import re


def write(input_file: str, kind: str):
    """Write"""
    for i in range(len(read(input_file))):
        step1 = extract_information(decode(read(input_file)[i]))
        print(step1)
    output_file = open(output_filename, "w")


def read(read_file: str):
    """Read file and return list of decoded dictionaries."""
    try:
        read_file = open(read_file, "r")
    except FileNotFoundError:
        print("File not found")
#    print(read_file.readline())    # print messes files up
    read_file = read_file.readlines()
    read_file = [line.strip() for line in read_file]    # removes whitespace
#    return extract_information(decode(read_file[2]))   # 0 and 1 are title line and separator
    pony_value_list = []
    for i in range(2, len(read_file)):
        pony_value_list.append(extract_information(decode(read_file[i])))
    print(f"pony value list: {pony_value_list}")
    return pony_value_list
#     todo add exception for file not found


def decode(line: str):
    """Decodes string in base64."""
    # "gICA" is separator.
    line = base64.b64decode(line)
    # print(f"decoded line: {line}")
    return line


def extract_information(line: str):
    """Make a pony attribute dict out of decoded string."""
    l_pony_attribute_values = []
    regex = r"([a-zA-Z]+ ?[a-zA-Z]+ ?[a-zA-Z]+)"
    for match in re.finditer(regex, str(line)):
        # print(match.group())
        l_pony_attribute_values.append(match.group())
    # print(l_pony_attribute_values)
    l_pony_dict_keys = ["name", "kind", "coat colour", "mane colour", "eye colour", "location"]
    dict_pony_attributes = {}
    for i in range(len(l_pony_attribute_values)):
        dict_pony_attributes.setdefault(l_pony_dict_keys[i], l_pony_attribute_values[i])
    # print(dict_pony_attributes)
    return dict_pony_attributes


def filter_by_location(ponies: list):
    """Remove ponies with location value "None"."""
    number_of_del_dicts = 0
    for i in range(2, (len(ponies))):
        i -= number_of_del_dicts        # otherwise skips list item after deletion
#        if len(ponies) == i:             # does not seem to be necessary with previos line
#            break
        # print(f"i: {i}")
        # print(f"Len: {len(ponies)}")
#        if ponies[i].get("name") == "Pinkie Fritter":   # second last, this and previous ponies loc is None
#            print("Peachy Fritter")
#        if ponies[i].get("name") == "Lotus Pie":    # last
#            print("Lotus Pie")
        if ponies[i].get("location") == "None":
            del ponies[i]
            # print("deleted")
            number_of_del_dicts += 1
    # print(ponies)
    return ponies


def filter_by_kind(ponies: list, kind: str):
    """Filter all ponies leaving the ones with matching kinds."""
    filtered_ponies = []        # uses append instead of del like in filter_by_location
    for i in range(2, (len(ponies))):
        if ponies[i].get("kind") == kind:
            filtered_ponies.append(ponies[i])
    return filtered_ponies


if __name__ == '__main__':
    # print(read("näidis_sisendfail.txt"))
    print(filter_by_location(read("näidis_sisendfail.txt")))
    print(filter_by_kind(read("näidis_sisendfail.txt"), "Alicorn"))
#    print(decode(
# 'TWF1ZCBQb21tZWwgICAgICAgICBVbmljb3JuICAgICAgICAgICAgIHBpbmsgICAgICAgICAgICAgICAgZ3JlZW4gICAgICAgICAgICAgICBjeWFuICAgICAgICAgICAgICAgIENhc3RsZSBvZiBGcmllbmRzaGlw'))
#    print(extract_information(decode(
# "TWF1ZCBQb21tZWwgICAgICAgICBVbmljb3JuICAgICAgICAgICAgIHBpbmsgICAgICAgICAgICAgICAgZ3JlZW4gICAgICAgICAgICAgICBjeWFuICAgICAgICAgICAgICAgIENhc3RsZSBvZiBGcmllbmRzaGlw")))
