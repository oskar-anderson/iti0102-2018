class MazeSolver:
    def __init__(self, maze_str: str, configuration: dict = None):
        """
        Initialize the solver with map string and configuration.
        Map string can consist of several lines, line break separates the lines.
        Empty lines in the beginning and in the end should be ignored.
        Line can also consist of spaces, so the lines cannot be stripped.
        Map can have non-rectangular shape (# indicates the border of the line):

        #####
        #   #
        #  #
        # #
        ##

        On the left and right sides there can be several doors (marked with "|").
        Solving the maze starts from a door from the left side and ends at the door on the right side.
        See more @solve().

        Configuration is a dict which indicates which symbols in the map string have what cost.
        Doors (|) are not shown in the configuration and are not used inside the maze.
        Door cell cost is 0.
        When a symbol on the map string is not in configuration, its cost is 0.
        Cells with negative cost cannot be moved on/through.

        Default configuration:
        configuration = {
            ' ': 1,
            '#': -1,
            '.': 2,
            '-': 5,
            'w': 10
        }

        :param maze_str: Map string
        :param configuration: Optional dictionary of symbol costs.

#        ########
#        #      #
#        #      #
#        |      |
#        ########

        """
        if configuration is None:
            configuration = {
                ' ': 1,
                '#': -1,
                '.': 2,
                '-': 5,
                'w': 10
            }

    def get_shortest_path(self, start, goal):
        """
        Return shortest path and the total cost of it.

        The shortest path is the path which has the lowest cost.
        Start and end are tuples of (y, x) where the first (upper) line is y = 0.
        The path should include both the start and the end.

        If there is no path from the start to goal, the path is None and cost is -1.

        If there are several paths with the same lowest cost, return any of those.

        :param start: Starting cell (y, x)
        :param goal: Goal cell (y, x)
        :return: shortest_path, cost
        """
        pass

    def solve(self):
        """
        Solve the given maze and return the path and the cost.

        Finds the shortest path from one of the doors on the left side to the one of the doors on the right side.
        Shortest path is the one with the lowest cost.

        This method should use get_shortest_path method and return the same values.
        If there are several paths with the same cost, return any of those.

        :return: shortest_path, cost
        """
        pass


if __name__ == '__main__':
    # tester was down 2
    maze = """
########
#      #
#      #
|      |
########
"""
    solver = MazeSolver(maze)
    assert solver.solve() == ([(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7)], 6)
    assert solver.get_shortest_path((3, 0), (3, 1)) == ([(3, 0), (3, 1)], 1)
    assert solver.get_shortest_path((3, 0), (2, 0)) == (None, -1)

    maze = """
#####
#   #
| # #
# # |
#####
    """
    solver = MazeSolver(maze)
    assert solver.solve() == ([(2, 0), (2, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4)], 6)

    maze = """
#####
#   |
#   |
| # #
#####
| # |
#####
    """
    solver = MazeSolver(maze)
    assert solver.solve() == ([(3, 0), (3, 1), (2, 1), (2, 2), (2, 3), (2, 4)], 4)
    # print(solver.get_shortest_path((3, 0), (1, 4)))
    # multiple paths possible, let's just assert the cost
    assert solver.get_shortest_path((3, 0), (1, 4))[1] == 5
    assert solver.get_shortest_path((5, 0), (5, 4)) == (None, -1)
