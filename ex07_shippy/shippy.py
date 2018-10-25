"""Simulation."""
from typing import Tuple
from copy import deepcopy


# test15
def move_to_capital_w(new_world_map, x_pos_of_x_in_list, y_pos_of_x_in_list):
    """Shippy moves to "W"."""
    row_string = new_world_map[y_pos_of_x_in_list]
    row_string = row_string[:x_pos_of_x_in_list] + "w" + row_string[1 + x_pos_of_x_in_list:]
    new_world_map[y_pos_of_x_in_list] = row_string
    return new_world_map


def move_to_w(new_world_map, x_pos_of_x_in_list, y_pos_of_x_in_list):
    """Shippy moves to "w"."""
    row_string = new_world_map[y_pos_of_x_in_list]
    row_string = row_string[:x_pos_of_x_in_list] + "-" + row_string[1 + x_pos_of_x_in_list:]
    new_world_map[y_pos_of_x_in_list] = row_string
    return new_world_map


def get_new_world_map(x_pos_of_x_in_list, y_pos_of_x_in_list, new_world_map, x, y):
    """Get new world map after movement, Shippy not in map."""
    if new_world_map[y_pos_of_x_in_list + y][x_pos_of_x_in_list + x] == "#":
        return x_pos_of_x_in_list, y_pos_of_x_in_list, new_world_map
    elif new_world_map[y_pos_of_x_in_list + y][x_pos_of_x_in_list + x] == "W":
        y_pos_of_x_in_list = y_pos_of_x_in_list + y
        x_pos_of_x_in_list = x_pos_of_x_in_list + x
        new_world_map = move_to_capital_w(new_world_map, x_pos_of_x_in_list, y_pos_of_x_in_list)
        return x_pos_of_x_in_list, y_pos_of_x_in_list, new_world_map
    elif new_world_map[y_pos_of_x_in_list + y][x_pos_of_x_in_list + x] == "w":
        y_pos_of_x_in_list = y_pos_of_x_in_list + y
        x_pos_of_x_in_list = x_pos_of_x_in_list + x
        new_world_map = move_to_w(new_world_map, x_pos_of_x_in_list, y_pos_of_x_in_list)
        return x_pos_of_x_in_list, y_pos_of_x_in_list, new_world_map
    else:
        y_pos_of_x_in_list = y_pos_of_x_in_list + y
        x_pos_of_x_in_list = x_pos_of_x_in_list + x
        return x_pos_of_x_in_list, y_pos_of_x_in_list, new_world_map


def simulate(world_map: list, flight_plan: list) -> list:
    """
    Simulate a flying space ship fighting space pirates.

    :param world_map: A list of strings indicating rows that make up the space map.
                 The space map is always rectangular and the minimum given size is 1x1.
                 Space pirate free zone is indicated by the symbol ('-'), low presence by ('w') and high presence by
                 'W'). The ship position is indicated by the symbol ('X'). There is always one ship on the space map.
                 Asteroid fields are indicated by the symbol ('#').

    :param flight_plan: A list of moves.
                  The moves are abbreviated N - north, E - east, S - south, W - west.
                  Ignore moves that would put the ship out of bounds or crash it into an asteroid field.

    :return: A list of strings indicating rows that make up the space map. Same format as the given wmap.

    Pirates under Shippy's starting position are always eliminated ('-').
    If Shippy fights pirates in high presence area, it first turns into low presence ('w')
     and then from low presence into no presence area ('-').
    """
    new_world_map = deepcopy(world_map)  # Remember about coping lists next time
    y_pos_of_x_in_list = get_y_x_pos_of_x(new_world_map)[0]
    x_pos_of_x_in_list = get_y_x_pos_of_x(new_world_map)[1]
    # x_pos_of_x_in_list should not be -1 according to docstring.

    row_string = new_world_map[y_pos_of_x_in_list]
    row_string = str(row_string[:x_pos_of_x_in_list]) + "-" + str(row_string[1 + x_pos_of_x_in_list:])
    new_world_map[y_pos_of_x_in_list] = row_string

    for i in range(len(flight_plan)):
        # print(flight_plan[i])
        if flight_plan[i] == "N" and y_pos_of_x_in_list - 1 != -1:
            x_pos_of_x_in_list, y_pos_of_x_in_list, new_world_map = \
                get_new_world_map(x_pos_of_x_in_list, y_pos_of_x_in_list, new_world_map, 0, -1)
        elif flight_plan[i] == "S" and y_pos_of_x_in_list + 1 != len(new_world_map):
            x_pos_of_x_in_list, y_pos_of_x_in_list, new_world_map = \
                get_new_world_map(x_pos_of_x_in_list, y_pos_of_x_in_list, new_world_map, 0, 1)
        elif flight_plan[i] == "E" and x_pos_of_x_in_list + 1 != len(new_world_map[0]):
            x_pos_of_x_in_list, y_pos_of_x_in_list, new_world_map = \
                get_new_world_map(x_pos_of_x_in_list, y_pos_of_x_in_list, new_world_map, 1, 0)
        elif flight_plan[i] == "W" and x_pos_of_x_in_list - 1 != -1:
            x_pos_of_x_in_list, y_pos_of_x_in_list, new_world_map = \
                get_new_world_map(x_pos_of_x_in_list, y_pos_of_x_in_list, new_world_map, -1, 0)
        else:
            print("Out of bounds.")
    row_string = new_world_map[y_pos_of_x_in_list]
    row_string = str(row_string[:x_pos_of_x_in_list]) + "X" + str(row_string[1 + x_pos_of_x_in_list:])
    new_world_map[y_pos_of_x_in_list] = row_string
    print(f"World map after replacements: {new_world_map}")
    return new_world_map


def get_y_x_pos_of_x(world_map):
    """Find and return y and x position of Shippy."""
    y_pos_of_x_in_list = 0
    for i in range(len(world_map)):
        if world_map[i].find("X") != -1:
            y_pos_of_x_in_list = i
            break
    x_pos_of_x_in_list = (world_map[y_pos_of_x_in_list]).find("X")
    return y_pos_of_x_in_list, x_pos_of_x_in_list


def list_to_dictionary_converter(world_map: list) -> Tuple[dict, int, int]:
    """
    Convert a list to dictionary using coordinates as keys.

    :param world_map: list of strings.
    :return: dictionary of the space, shippy y position, shippy x position

    Map tile under Shippy's location is marked as "-" or no presence area.
    Dictionaries key is a Tuple which has Y-position as the first value and X-position as
    the second value. If there is no Shippy (Marked as X in the list) in the list, the
    coordinates are marked as 0 and 0.
    """
    coordinates_and_symbols = {}
    for y in range(len(world_map)):
        for x in range(len(world_map[y])):
            dict_key = (y, x)
            dict_value = world_map[y][x]
            if dict_value == "X":
                dict_value = "-"
            coordinates_and_symbols.setdefault(dict_key, dict_value)
    y_x_pos_of_x = get_y_x_pos_of_x(world_map)
    x_pos_of_x = y_x_pos_of_x[1]
    y_pos_of_x = y_x_pos_of_x[0]
    if x_pos_of_x == -1:
        x_pos_of_x = 0
        y_pos_of_x = 0
    tuple_with_dict_and_shippy_position = (coordinates_and_symbols, y_pos_of_x, x_pos_of_x)
    return tuple_with_dict_and_shippy_position


def dictionary_to_list_converter(space_map: dict, width: int, height: int) -> list:
    """
    Convert dictionary of coordinates to list of strings.

    :param space_map: Dictionary of the space
    :param width: Width of the world.
    :param height: Height of the world.
    :return: List of strings

    PS: You should add Shippy back the the dictionary before you call this method.
    """
    dict_to_space_map_list = []
    for y in range(height):
        for x in range(width):
            dict_to_space_map_list.append(space_map.get((y, x)))    # double () are important
    long_str_of_dict_values = "".join(dict_to_space_map_list)
    remaining_string = long_str_of_dict_values
    dict_to_space_map_list = []
    for i in range(height):
        long_str_of_dict_values = remaining_string[:width]
        remaining_string = remaining_string[width:]
        dict_to_space_map_list.append(long_str_of_dict_values)
    return dict_to_space_map_list


if __name__ == '__main__':
    space_map_list = [
        "#www-",
        "wXw#-",
    ]
    flight_plan1 = ["N", "E", "E", "S", "E"]
    print("\n".join(simulate(space_map_list, flight_plan1)))
    assert simulate(space_map_list, flight_plan1) == ["#---X", "w-w#-"]
    # #---X
    # w-w#-
    print(list_to_dictionary_converter(flight_plan1))
    space_map_list5 = [
        "-WWw--",
        "Xw#---"
    ]
    flight_plan5 = ["E", "N", "E", "S", "E", "E"]
    #   "-w--X-"
    #   "--#---"
    print(simulate(space_map_list5, flight_plan5))
#    space_map_list = [
#        "#www-",
#        "wXw#-",
#    ]
    assert simulate(space_map_list, flight_plan1) == ["#---X", "w-w#-"]

    space_list2 = [
        "WWWW",
        "-wwW",
        "X-#W",
    ]

    flight_plan2 = ["N", "N", "E", "E", "S", "W", "W", "S", "E", "E"]
    print(simulate(space_list2, flight_plan2))
    print("\n".join(simulate(space_list2, flight_plan2)))

    # wwwW
    # ---W
    # -X#W
    assert simulate(space_list2, flight_plan2) == ["wwwW", "---W", "-X#W"]
    print(list_to_dictionary_converter(['W#', '-X']) == ({(0, 0): 'W', (0, 1): '#', (1, 0): '-', (1, 1): '-'}, 1, 1))
    assert list_to_dictionary_converter(["-"]) == ({(0, 0): "-"}, 0, 0)
    print("tttttttttttt")
    assert list_to_dictionary_converter(['W#', '-X']) == ({(0, 0): 'W', (0, 1): '#', (1, 0): '-', (1, 1): '-'}, 1, 1)

    assert list_to_dictionary_converter(
        world_map=space_map_list
    ) == ({(0, 0): '#', (0, 1): 'w', (0, 2): 'w', (0, 3): 'w', (0, 4): '-', (1, 0): 'w', (1, 1): '-', (1, 2): 'w',
           (1, 3): '#', (1, 4): '-'}, 1, 1)                                                    # /\ This is "X"?

    assert dictionary_to_list_converter(
        {(0, 0): '#', (0, 1): 'w', (0, 2): 'w', (0, 3): 'w', (0, 4): '-', (1, 0): 'w', (1, 1): 'X', (1, 2): 'w',
         (1, 3): '#', (1, 4): '-'}, 5, 2) == space_map_list

    assert dictionary_to_list_converter({(0, 0): "X"}, 1, 1) == ["X"]
