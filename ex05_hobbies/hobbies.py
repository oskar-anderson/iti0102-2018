"""Hobbies."""
import csv


def create_list_from_file(file):
    """
    Collect lines from given file into list.

    :param file: original file path
    :return: list of lines
    """
    file = open(file, "r")
    return file.readlines()


def create_dictionary(file):
    """
    Create dictionary about given peoples' hobbies as Name: [hobby_1, hobby_2].

    :param file: original file path
    :return: dict
    """
    if file:
        pass
    pre_dic_dict = {}
    # print(create_list_from_file(file))
    l_of_hobbies_for_current_person = []
    old_name = ""

    for lines in sorted(create_list_from_file("hobbies_database.txt")):
        number_of_characters_in_key = lines.find(":")
        name = (lines[0:number_of_characters_in_key])

        if old_name != name:
            l_of_hobbies_for_current_person = []
            old_name = name
        # empties list if person changes

        if lines.find("\n") != -1:
            hobby = (lines[number_of_characters_in_key + 1:lines.find("\n")])
        # all keys' values except last
        else:
            hobby = (lines[number_of_characters_in_key + 1:len(lines)])
        # key's value from line 100

        if hobby not in l_of_hobbies_for_current_person:
            pre_dic_dict.setdefault(name, []).append(hobby)
            l_of_hobbies_for_current_person.append(hobby)

    # tests:
    # print("jack's hobbies: " + str(pre_dic_dict.get("Jack")))
    # print("pre_dic_dict: " + str(pre_dic_dict))

    return pre_dic_dict


def find_person_with_most_hobbies(file):
    """
    Find the person (or people) who have more hobbies than others.

    :param file: original file path
    :return: list
    """
    if file:
        pass
    dic = create_dictionary("hobbies_database.txt")
    d_number_of_hobbies_for_person = {}
    for name in dic:
        number_of_hobbies = (len(dic[name]))
        d_number_of_hobbies_for_person.update({name: number_of_hobbies})
    print(d_number_of_hobbies_for_person)

    l_names_of_people_with_most_hobbies = []
    for name in d_number_of_hobbies_for_person:
        if d_number_of_hobbies_for_person[name] == max(d_number_of_hobbies_for_person.values()):
            # print(name, d_number_of_hobbies_for_person[name])
            l_names_of_people_with_most_hobbies.append(name)
    return l_names_of_people_with_most_hobbies


def find_person_with_least_hobbies(file):
    """
    Find the person (or people) who have less hobbies than others.

    :param file: original file path
    :return: list
    """
    if file:
        pass
    dic = create_dictionary("hobbies_database.txt")
    d_number_of_hobbies_for_person = {}
    for name in dic:
        number_of_hobbies = (len(dic[name]))
        d_number_of_hobbies_for_person.update({name: number_of_hobbies})
    print(d_number_of_hobbies_for_person)

    l_names_of_people_with_least_hobbies = []
    for name in d_number_of_hobbies_for_person:
        if d_number_of_hobbies_for_person[name] == min(d_number_of_hobbies_for_person.values()):
            # print(name, d_number_of_hobbies_for_person[name])
            l_names_of_people_with_least_hobbies.append(name)
    return l_names_of_people_with_least_hobbies


def find_most_popular_hobby(file):
    """
    Find the most popular hobby.

    :param file: original file path
    :return: list
    """
    pass


def find_least_popular_hobby(file):
    """
    Find the least popular hobby.

    :param file: original file path
    :return: list
    """
    pass


def write_corrected_database(file, file_to_write):
    """
    Write .csv file in a proper way. Use collected and structured data.

    :param file: original file path
    :param file_to_write: file to write result
    """
    with open(file_to_write, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        name = "Name"
        hobbies = "Hobbies"
        writer.writerow([name, hobbies])
        # your code goes here

# These examples are based on a given text file from the exercise.


if __name__ == '__main__':
    dic = create_dictionary("hobbies_database.txt")
    print(len(create_list_from_file("hobbies_database.txt")))  # -> 100
    print("Check presence of hobbies for chosen person:")
    print("shopping" in dic["Wendy"])  # -> True
    print("fitness" in dic["Sophie"])  # -> False
    print("gaming" in dic["Peter"])  # -> True
    print("Check if hobbies - person relation is correct:")
    print("Check if a person(people) with the biggest amount of hobbies is(are) correct:")
    print(find_person_with_most_hobbies("hobbies_database.txt"))  # -> ['Jack']
    print(len(dic["Jack"]))  # ->  12
    print(len(dic["Carmen"]))  # -> 10
    print("Check if a person(people) with the smallest amount of hobbies is(are) correct:")
    print(find_person_with_least_hobbies("hobbies_database.txt"))  # -> ['Molly']
    print(len(dic["Molly"]))  # -> 5
    print(len(dic["Sophie"]))  # -> 7
    print("Check if the most popular hobby(ies) is(are) correct")
    print(find_most_popular_hobby("hobbies_database.txt"))  # -> ['gaming', 'sport', 'football']
    print("Check if the least popular hobby(ies) is(are) correct")
    print(find_least_popular_hobby("hobbies_database.txt"))  # -> ['tennis', 'dance', 'puzzles', 'flowers']
    write_corrected_database("hobbies_database.txt", 'correct_hobbies_database.csv')
