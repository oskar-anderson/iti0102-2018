"""Test shortest way back solutions."""
from shortest_way_back import shortest_way_back
import random


def test_one_directional_movement():
    """Test with one directional movement."""
    assert shortest_way_back("N") == "S"
    assert shortest_way_back("S") == "N"
    assert shortest_way_back("W") == "E"
    assert shortest_way_back("E") == "W"
    assert shortest_way_back("NNNNNNNNN") == "SSSSSSSSS"
    assert shortest_way_back("SSSSSSSSS") == "NNNNNNNNN"
    assert shortest_way_back("WWWWWWWWW") == "EEEEEEEEE"
    assert shortest_way_back("EEEEEEEEE") == "WWWWWWWWW"


def test_remove_duplicates():
    """Test with opposite directions"""
    assert shortest_way_back("NNSSWWE") == "E"
    assert shortest_way_back("NSEW") == ""


def test_inproper_input():
    """Test with inproper variables."""
    assert shortest_way_back("abc") == ""
    assert shortest_way_back("1234567890" + "abc") == ""
    assert shortest_way_back("ne") == ""
    assert shortest_way_back("") == ""


def solution(path):
    """Run my solution for shortest way back."""
    y_coordinates = path.count("N") - path.count("S")
    x_coordinates = path.count("E") - path.count("W")
    result_list = []
    for i in range(abs(x_coordinates) + abs(y_coordinates)):
        if y_coordinates > 0:
            y_coordinates -= 1
            result_list.append("S")
        elif y_coordinates < 0:
            y_coordinates += 1
            result_list.append("N")
        elif x_coordinates > 0:
            x_coordinates -= 1
            result_list.append("W")
        elif x_coordinates < 0:
            x_coordinates += 1
            result_list.append("E")
    result_string = "".join(result_list)
    return result_string


def test_random():
    """Test randomly generated directions variable."""
    path = "".join(random.choices("NSWE", k=random.randint(0, 10)))
    assert shortest_way_back(path) == solution(path)
