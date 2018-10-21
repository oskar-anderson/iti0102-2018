"""Find the shortest way back in a taxicab geometry."""


def shortest_way_back(path: str) -> str:
    """
    Find the shortest way back in a taxicab geometry.

    :param path: string of moves, where moves are encoded as follows:.
    N - north -  (1, 0)
    S - south -  (-1, 0)
    E - east  -  (0, 1)
    W - west  -  (0, -1)
    (first coordinate indicates steps towards north,
    second coordinate indicates steps towards east)

    :return: the shortest way back encoded the same way as :param path:.
    """
    y_coordinates = path.count("N") - path.count("S")
    x_coordinates = path.count("E") - path.count("W")
    print(f"Path: {path}")
    print(f"x = {x_coordinates}; y = {y_coordinates}")
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
    # print(result_list)
    result_string = "".join(result_list)
    print(f"Result: {result_string}")
    return result_string


if __name__ == '__main__':
    assert shortest_way_back("NNN") == "SSS"
    assert shortest_way_back("SS") == "NN"
    assert shortest_way_back("E") == "W"
    assert shortest_way_back("WWWW") == "EEEE"
    assert shortest_way_back("") == ""
    assert shortest_way_back("NESW") == ""
    assert shortest_way_back("NNEESEW") in ["SWW", "WSW", "WWS"]
