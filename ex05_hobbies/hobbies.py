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
    main_dict = {}
    # print(create_list_from_file(file))
    l_of_hobbies_for_current_person = []
    old_name = ""

    for lines in sorted(create_list_from_file(file)):
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
            main_dict.setdefault(name, []).append(hobby)
            l_of_hobbies_for_current_person.append(hobby)

    # tests:
    # print("jack's hobbies: " + str(main_dict.get("Jack")))
    # print("main_dict: " + str(main_dict))

    return main_dict


def find_person_with_most_or_least_hobbies(file, most_or_least):
    """
    Find the person (or people) who have more hobbies than others.

    :param file: original file path
    :param most_or_least: determines if to find the person(s) with most or least amount of hobbies
    :return: list
    """
    main_dict = create_dictionary(file)
    d_number_of_hobbies_for_person = {}
    for name in main_dict:
        number_of_hobbies = (len(main_dict[name]))
        d_number_of_hobbies_for_person.update({name: number_of_hobbies})
    print(d_number_of_hobbies_for_person)

    l_names_of_people_with_most_or_least_hobbies = []
    for name in d_number_of_hobbies_for_person:
        if most_or_least == "most":
            if d_number_of_hobbies_for_person[name] == max(d_number_of_hobbies_for_person.values()):
                # print(name, d_number_of_hobbies_for_person[name])
                l_names_of_people_with_most_or_least_hobbies.append(name)
        elif most_or_least == "least":
            if d_number_of_hobbies_for_person[name] == min(d_number_of_hobbies_for_person.values()):
                # print(name, d_number_of_hobbies_for_person[name])
                l_names_of_people_with_most_or_least_hobbies.append(name)
        else:
            return False
    return l_names_of_people_with_most_or_least_hobbies


def find_person_with_most_hobbies(file):
    """
    Find the person (or people) who have more hobbies than others.

    :param file: original file path
    :return: list
    """
    return find_person_with_most_or_least_hobbies(file, "most")


def find_person_with_least_hobbies(file):
    """
    Find the person (or people) who have less hobbies than others.

    :param file: original file path
    :return: list
    """
    return find_person_with_most_or_least_hobbies(file, "least")


def find_most_or_least_popular_hobby(file, min_or_max):
    """
    Find the most or least popular hobby.

    :param file: original file path
    :param min_or_max: determines if to find the least or most popular hobby (or hobbies)
    :return: list
    """
    # print(min_or_max == "max")
    # print(min_or_max == "min")
    main_dict = create_dictionary(file)
    main_dict_reversed = {}
    for name in main_dict:
        for hobby in main_dict[name]:
            # main_dict_reversed[hobby] = name  # does not work, overwrites
            main_dict_reversed.setdefault(hobby, []).append(name)
    # print(main_dict_reversed)

    d_hobbies_popularity = {}
    for hobby in main_dict_reversed:
        number_of_names_per_hobby = (len(main_dict_reversed[hobby]))
        d_hobbies_popularity.update({hobby: number_of_names_per_hobby})
    print(d_hobbies_popularity)

    l_hobbies_with_most_or_least_people = []
    for hobby in d_hobbies_popularity:
        if min_or_max == "max":
            if d_hobbies_popularity[hobby] == max(d_hobbies_popularity.values()):
                # print("The most popular hobies: " + hobby, d_hobbies_popularity[hobby])
                l_hobbies_with_most_or_least_people.append(hobby)
        elif min_or_max == "min":
            if d_hobbies_popularity[hobby] == min(d_hobbies_popularity.values()):
                # print("The least popular hobies: " + hobby, d_hobbies_popularity[hobby])
                l_hobbies_with_most_or_least_people.append(hobby)
        else:
            return False
    # print(l_hobbies_with_most_or_least_people)
    return l_hobbies_with_most_or_least_people


def find_most_popular_hobby(file):
    """
    Find the most popular hobby.

    :param file: original file path
    :return: list
    """
    return find_most_or_least_popular_hobby(file, "max")


def find_least_popular_hobby(file):
    """
    Find the least popular hobby.

    :param file: original file path
    :return: list
    """
    return find_most_or_least_popular_hobby(file, "min")


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
        dict1 = create_dictionary(file)
        previous_name = ""
        for name in dict1:
            # print(list(dict1[name]))
            # print("number of hobbies: " + str(len(dict1[name])))
            hobby = dict1[name]
            for i in range(len(dict1[name])):
                if previous_name != name:
                    pass
            writer.writerow([name, hobby])
            previous_name = name


# These examples are based on a given text file from the exercise.


if __name__ == '__main__':
    dic = create_dictionary("hobbies_database.txt")  # Do not use
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
