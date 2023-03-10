"""Make life easier whilst volunteering in a French language camp."""
import math


def count_portions(number_of_participants: int, day: int) -> int:
    """
    Count the total of portions served to participants during the camp recursively.

    There are 4 meals in each day and we expect that every participant eats 1 portion
    per meal. At the end of each day one participant leaves the camp and is not ours to
    feed.

    We are only counting the participants' meals, the organisers and volunteers
    eat separately. In case of negative participants or days the number of meals is
    still 0.

    count_portions(0, 7) == 0
    count_portions(6, 0) == 0
    count_portions(-8, 5) == 0
    count_portions(9, -5) == 0

    count_portions(6, 1) == 24
    count_portions(6, 2) == 44
    count_portions(6, 3) == 60

    :param number_of_participants: the initial number of participants.
    :param day: the specified day.
    :return: a total of portions served during the camp at the end of the specified day.
    """
    if day < 1:
        return 0
    if number_of_participants < 1:
        return 0
    return number_of_participants * 4 + count_portions(number_of_participants - 1, day - 1)

#    if day < 1:
#        return 0
#    if number_of_participants < 1:
#        return 0
#    day_count = 1
#    number_of_meals = 0
#    while number_of_participants > 0:
#        number_of_meals += number_of_participants * 4
#        if day == day_count:
#            return number_of_meals
#        day_count += 1
#        number_of_participants -= 1


def names_to_be_eliminated(points_dict: dict, names: set = None, lowest_score: int = None) -> set:
    """
    Recursively find the names that are to be eliminated.

    When two or more people have the same lowest score, return a set in which every lowest
    scoring person is listed.

    names_to_be_eliminated({}) == set()
    names_to_be_eliminated({"Dylan": 10}) == {"Dylan"}
    names_to_be_eliminated({"Carl": 4, "Bert": -10}) == {"Bert"}
    names_to_be_eliminated({"Terry": 4, "Pete": 4}) == {"Terry", "Pete"}

    :param points_dict: dictionary containing name strings as
                        keys and points integers as values.
    :param names: helper to store current names
    :param lowest_score: helper to store current lowest score
    :return: set of names of lowest scoring people.
    """
    if not names:
        names = set()
    if not lowest_score:
        lowest_score = math.inf
    keys = list(points_dict.keys())
    values = list(points_dict.values())
    if not keys or not values:      # they should be empty at the same time
        print(f"Result: {names}")
        return names
    print(f"keys:    {keys}")
    print(f"values:  {values}")
    if values[0] == lowest_score:
        names.add(keys[0])
    elif values[0] < lowest_score:
        names = set()
        names.add(keys[0])
    else:
        print("This should not be reached!")
    if values[0] < lowest_score:
        lowest_score = values[0]
    del keys[0]
    del values[0]
    new_points_dict = dict(zip(keys, values))
    print(f"New dict: {new_points_dict}, Names: {names}, Lowest score: {lowest_score}")
    return names_to_be_eliminated(new_points_dict, names, lowest_score)


def people_in_the_know(hours_passed, cache: dict = None) -> int:
    """
    Return the number of people who know a rumor given the hours passed from the initial release.

    Every hour there is a recess where everybody can talk to everybody. Rumors always spread in
    the same fashion: everybody who are in the know are silent one recess after the recess they
    were told of the rumor. After that they begin to pass it on, one person per recess.

    people_in_the_know(0) == 0 #0#0
    people_in_the_know(1) == 1 #1#0
    people_in_the_know(2) == 1 #1#1
    people_in_the_know(3) == 2 #2#1
    people_in_the_know(4) == 3 #3#2
    people_in_the_know(5) == 5 #5#3
    people_in_the_know(6) == 8 #8#5
    people_in_the_know(7) == 13

    :param hours_passed: the hours passed from the initial release.
    :param cache: helper to store already calculated results.
    :return: the number of people that have heard the rumor.
    """
#    return round(((1 + math.sqrt(5)) ** hours_passed - (1 - math.sqrt(5)) ** hours_passed) /
#                 (2 ** hours_passed * math.sqrt(5)))
    if not cache:
        pass
    if hours_passed == 2 or hours_passed == 1:
        return 1
    if hours_passed < 1:
        return 0
    return people_in_the_know(hours_passed - 1) + people_in_the_know(hours_passed - 2)


def traversable_coordinates(world_map: list, coord: tuple = (0, 0), traversable_coords: set = None) -> set:
    """
    Return the coordinates that are traversable by humans or adjacent to traversable coordinates.

    Given a two-dimensional list as a map, give the coordinates of traversable cells with the
    coordinates of cells which are adjacent to traversable cells with respect to the
    beginning coordinate.

    If there is not a traversable path from the beginning coordinate
    to the traversable cell, the traversable cell coordinate is not returned. Traversable
    cells are represented by empty strings. If the beginning coordinate cell is not traversable,
    return empty set.

    Coordinates are in the format (current_row, current_column). Negative coordinate values are considered invalid.
    world_map is not necessarily rectangular. Paths can be made through a diagonal.

    traversable_coordinates([]) == set()
    traversable_coordinates([[]]) == set()
    traversable_coordinates([["", "", ""]], (5, 2)) == set()
    traversable_coordinates([["1", "1", ""]], (-4, -9)) == set()
    traversable_coordinates([["1", [], "1"]], (0, 1)) == set()

    world = [["1", "1", "1", "1", "1"],
             ["1", "1", "1",  "", "1"],
             ["1", "1",  "", "1", "1"],
             ["1", "1",  "", "1", "1"],
             ["1", "1", "1", "1", "1"]]

    traversable = {(0, 2), (0, 3), (0, 4),
                   (1, 1), (1, 2), (1, 3), (1, 4),
                   (2, 1), (2, 2), (2, 3), (2, 4),
                   (3, 1), (3, 2), (3, 3),
                   (4, 1), (4, 2), (4, 3)}

    traversable_coordinates(world, (2, 2)) == traversable

    :param world_map: two-dimensional list of strings.
    :param coord: the (beginning) coordinate.
    :param traversable_coords: helper to store traversable coordinates.
    :return: set of traversable and traversable-adjacent cell
            coordinate tuples with respect to starting coord
    """
    try:
        if world_map[coord[0]][coord[1]] != "check" and world_map[coord[0]][coord[1]] != "":
            return set()
    except IndexError:
        return set()

    coord = turn_negative_coord_positive(world_map, coord)

    traversable_coords, world_map = create_set_of_coords_to_check(world_map, coord, traversable_coords)

    current_row, current_column = coord
    print(f"traversable coords: {traversable_coords}")
    world_map[current_row][current_column] = "been here"
    print(f"current world map: {world_map}")
    new_coord = None
    if traversable_coords:
        new_coord = traversable_coords.pop()
    if new_coord is not None:
        return traversable_coordinates(world_map, new_coord, traversable_coords)
    print(f"final world map: {world_map}")
    for row in range(len(world_map)):
        for column in range(len(world_map[row])):
            if world_map[row][column] == "been here" or world_map[row][column] == "border":
                traversable_coords.add((row, column))
    print(traversable_coords)
    return traversable_coords


def turn_negative_coord_positive(world_map, coord):
    """Turn negative list position in coord to positive."""
    current_row, current_column = coord
    while current_row < 0:
        current_row = len(world_map) + current_row
    while current_column < 0:
        current_column = len(world_map[current_row]) + current_column
    coord = (current_row, current_column)
    return coord


def create_set_of_coords_to_check(world_map, coord, traversable_coords):
    """Modify world map and give coordinates of ""."""
    possible_moves = [
        [-1, -1], [-1, 0], [-1, 1],
        [0, -1], [0, 1],
        [1, -1], [1, 0], [1, 1]
    ]

    current_row, current_column = coord

    print(f"Given world map: {world_map}")
    print(f"current_row: {current_row}, current_column: {current_column}")
    print(f"row length: {len(world_map[current_row])}, column length: {len(world_map)}")

    error_check = str(0)

    if traversable_coords is None:
        traversable_coords = set()
    for i in range(8):
        if current_column + possible_moves[i][1] != -1 and current_row + possible_moves[i][0] != -1:
            try:
                error_check += str(world_map[current_row + possible_moves[i][0]][current_column + possible_moves[i][1]])
            except IndexError:
                continue
            if world_map[current_row + possible_moves[i][0]][current_column + possible_moves[i][1]] == "" or\
                    world_map[current_row + possible_moves[i][0]][current_column + possible_moves[i][1]] == "1":
                if world_map[current_row + possible_moves[i][0]][current_column + possible_moves[i][1]] == "" or\
                        world_map[current_row + possible_moves[i][0]][current_column + possible_moves[i][1]] == "check":
                    world_map[current_row + possible_moves[i][0]][current_column + possible_moves[i][1]] = "check"
                    traversable_coords.add((current_row + possible_moves[i][0], current_column + possible_moves[i][1]))
                elif world_map[current_row + possible_moves[i][0]][current_column + possible_moves[i][1]] == "1":
                    world_map[current_row + possible_moves[i][0]][current_column + possible_moves[i][1]] = "border"
                else:
                    pass
    return traversable_coords, world_map    # lists do not really have to be returned


if __name__ == '__main__':
    """
    print(count_portions(6, 1))
    print(count_portions(6, 2))
    print(count_portions(6, 3))
    print()
    print(names_to_be_eliminated({}) == set())
    print()
    print(names_to_be_eliminated({"Dylan": 10}) == {"Dylan"})
    print()
    print(names_to_be_eliminated({"Carl": 4, "Bert": -10}) == {"Bert"})
    print()
    print(names_to_be_eliminated({"Terry": 4, "Pete": 4}) == {"Terry", "Pete"})
    print()
#    assert count_portions(6, 1) == 24
#    assert count_portions(6, 2) == 44
#    assert count_portions(6, 3) == 60
    print(people_in_the_know(0) == 0)
    print(people_in_the_know(1) == 1)
    print(people_in_the_know(2) == 1)
    print(people_in_the_know(3) == 2)
    print(people_in_the_know(4) == 3)
    print(people_in_the_know(7) == 13)
    print()
    """
    world = [
        ["1", "1", "1", "1", "1"],
        ["1", "1", "1", "", "1"],
        ["1", "1", "", "1", "1"],
        ["1", "1", "", "1", "1"],
        ["1", "1", "1", "1", "1"]
    ]

    traversable = {(0, 2), (0, 3), (0, 4),
                   (1, 1), (1, 2), (1, 3), (1, 4),
                   (2, 1), (2, 2), (2, 3), (2, 4),
                   (3, 1), (3, 2), (3, 3),
                   (4, 1), (4, 2), (4, 3)}
    print(traversable_coordinates([]) == set())
    print(traversable_coordinates([[]]) == set())
    print(traversable_coordinates([["", "", ""]], (5, 2)) == set())
    print(traversable_coordinates([["1", "1", ""]], (-4, -9)) == set())
    print(traversable_coordinates([["1", [], "1"]], (0, 1)) == set())
    print("the real test:")
    print(traversable_coordinates(world, (2, 2)) == traversable)
    print()
    world2 = [
        ["1", "1", "1", "1", "1"],
        ["1", "", "1", "1", "1"],
        ["1", "", "1", "1", ""],
        ["", "1", "1", "", "1"],
        ["1", "", "", "1", "1"]
    ]
    traversable = {(0, 0), (0, 1), (0, 2),
                   (1, 0), (1, 1), (1, 2), (1, 3), (1, 4),
                   (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
                   (3, 0), (3, 1), (3, 2), (3, 3), (3, 4),
                   (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)}
    print(traversable_coordinates(world2, (-4, -4)) == traversable)
    print()

    world3 = [
        ["", "1", "1", "1", "1"],
        ["", "1", "", "1", "1"],
        ["1", ""],
    ]
    traversable = {(0, 0), (0, 1), (0, 2), (0, 3),
                   (1, 0), (1, 1), (1, 2), (1, 3),
                   (2, 0), (2, 1)}

    print(traversable_coordinates(world3, (0, 0)) == traversable)
