from copy import deepcopy
from math import inf


class Tile:
    def __init__(self, row, column, character, is_end=False, character_value=0, changing_character_value=0,
                 cost_to_here=inf):
        self.row = row
        self.column = column
        self.character = character
        self.is_end = is_end
        self.character_value = character_value
        self.changing_character_value = changing_character_value
        self.cost_to_here = cost_to_here
        self.column_to_here = None
        self.row_to_here = None

    def __repr__(self):
        return f"[Tile loc: ({self.row}:{self.column}), character value: {self.changing_character_value}/" \
               f"{self.character_value}, path here: ({self.row_to_here}:{self.column_to_here}), " \
               f"cost here: {self.cost_to_here}]"


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
        self.configuration = configuration
        self.maze_str = maze_str
        self.maze_map = []  # maze_str will be made into a list, which will in turn be used to make maze_tile_object_map
        self.maze_tile_object_map = []
        self.tiles_to_check_next_no_modification = []
        # currently unused but could be great for mazes with high slowness tiles.
        # could store all tiles_to_check's fitting adjacent tiles.
        # useful for filtering out all tiles with changing_character_value 2 or higher,
        self.min_changing_character_value_2_or_higher = None
        # and then taking the minimum changing_character_value and saving it to min_changing_character_value_2_or_higher
        self.tiles_to_check = []  # pops tiles out until empty then copies tiles from tiles_to_check_next
        self.tile_to_check = None  # popped tile
        self.tiles_to_check_next = []  # tiles to check next, each time this is copied path cost increases by 1
        self.tiles_not_to_visit_again = []  # tiles with character_values 0, otherwise 2 adjacent such tiles will cause
        # an infinite loop
        self.end_doors = []
        self.start_doors = []  # Stores maze starting door objects
        self.path_found = False  # determines if path exists or not
        self.end_tile = None    # stores first end tile object that is reached

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
        self.reset_map(self.configuration, self.maze_str)
        self.make_map_list()
        self.tiles_to_objects()
        self.print_maze_tile_object_map()
        self.pathfinder("hole_map")
        row, column = goal[0], goal[1]
        path_end_to_start = [(row, column)]
        cost = self.maze_tile_object_map[row][column].character_value
        while True:
            row, column = self.maze_tile_object_map[row][column].row_to_here, self.maze_tile_object_map[row][column].column_to_here
            if row is not None and (row != start[0]) + (column != start[1]) != 0:
                cost += self.maze_tile_object_map[row][column].character_value
                path_end_to_start.append((row, column))
            elif row is not None:
                cost += self.maze_tile_object_map[row][column].character_value
                path_end_to_start.append((row, column))
                break
            else:
                break
        path_start_to_end = path_end_to_start[::-1]
        if not (abs(start[0] - goal[0]) + abs(start[1] - goal[1])) + 1 == len(path_start_to_end):
            return None, -1
        if cost == -1:
            path_start_to_end = (None, cost)
        else:
            path_start_to_end = (path_start_to_end, cost)
        # print(f"Path start to end: {path_start_to_end}")
        self.print_maze_tile_object_map()
        return path_start_to_end

    def solve(self):
        """
        Solve the given maze and return the path and the cost.

        Finds the shortest path from one of the doors on the left side to the one of the doors on the right side.
        Shortest path is the one with the lowest cost.

        This method should use get_shortest_path method and return the same values.
        If there are several paths with the same cost, return any of those.

        :return: shortest_path, cost
        """
        self.reset_map(self.configuration, self.maze_str)
        self.make_map_list()
        self.tiles_to_objects()
        return self.pathfinder("exit")


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
