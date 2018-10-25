"""Test shortest way back solutions."""
from shortest_way_back import shortest_way_back
import random


def simple_test():
    assert shortest_way_back("N") == "S"


def test_one_directional_movement():
    """Test shortest way back."""
    assert shortest_way_back("NNNNNNNNN") == "SSSSSSSSS"
    assert shortest_way_back("SSSSSSSSS") == "NNNNNNNNN"
    assert shortest_way_back("WWWWWWWWW") == "EEEEEEEEE"
    assert shortest_way_back("EEEEEEEEE") == "WWWWWWWWW"


def test_remove_duplicates():
    assert shortest_way_back("NNSSWWE") == "E"
    assert shortest_way_back("NSEW") == ""


def test_inproper_input():
    assert shortest_way_back("abc") == ""
    assert shortest_way_back("1234567890" + "abc") == ""
    assert shortest_way_back("ne") == ""


def solution(path):
    return "NSWE"


def test_random():
    path = "".join(random.choices("NSWE", k=random.randint(0, 10)))
    assert shortest_way_back(path) == solution(path)
