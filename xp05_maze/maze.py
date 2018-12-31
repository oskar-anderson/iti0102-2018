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

    def make_map_list(self):
        """Change maze map into list format"""
        self.maze_map = self.maze_str.splitlines()
        self.maze_map.remove("")
        # print(self.maze_map)
        print("List of maze map:" + "\n" + "\n".join(self.maze_map))
        print()

    def tiles_to_objects(self):
        """Make all maze tiles to objects and add them to maze list.

        Set configuration dictionary values for characters.
        Add starting tiles to tiles_to_check.
        """
        for row in range(len(self.maze_map)):
            row_tiles = []
            for column in range(len(self.maze_map[row])):
                tile = Tile(row, column, self.maze_map[row][column])
                if column == len(self.maze_map[row]) - 1 and self.maze_map[row][-1] == "|":
                    tile.is_end = True
                    self.end_doors.append(tile)
                    tile.cost_to_here = 0
                if column == 0 and self.maze_map[row][0] == "|":
                    self.tiles_to_check.append(tile)
                    self.tiles_to_check_next_no_modification.append(tile)
                    self.start_doors.append(tile)
                    tile.cost_to_here = 0
                if tile.character in self.configuration.keys():
                    tile.character_value = self.configuration[tile.character]
                    tile.changing_character_value = self.configuration[tile.character]
                row_tiles.append(tile)
            self.maze_tile_object_map.append(row_tiles)
        print(self.maze_tile_object_map)
        print(f"Starting position(s): {self.start_doors}")
        print()

    def pathfinder(self, run_until_exit_or_hole_map):
        """Main pathfinding function. Find shortest path from starting tile to end tile.

        Take starting tile(s) as tile(s) to check and start checking tiles adjacent to them.
        Check that adjacent tiles are not out of bounds.
        If any adjacent tile is not out of bounds call tile_checker function.
        If tile_checker finds a path call return_path.
        If tiles_to_check is empty no path could be found. Return (None, -1)
        """
        while len(self.tiles_to_check) != 0:
            # and self.maze_tile_object_map[self.tiles_to_check[0].row][self.tiles_to_check[0].column].is_end is False:
            print(f"Tiles to check list: {self.tiles_to_check}")
            print(f"Tiles to check next list: {self.tiles_to_check_next}")
            self.tile_to_check = self.tiles_to_check.pop(0)
            print(f"Tile being checked: {self.tile_to_check}")
            if self.tile_to_check.row - 1 != -1 and len(
                    self.maze_tile_object_map[self.tile_to_check.row - 1]) >= self.tile_to_check.column:  # N
                row, column = self.tile_to_check.row - 1, self.tile_to_check.column
                self.tile_checker(self.maze_tile_object_map[row][column], run_until_exit_or_hole_map)
                if self.path_found:
                    break
            if self.tile_to_check.column + 1 < len(self.maze_tile_object_map[self.tile_to_check.row]):  # E
                row, column = self.tile_to_check.row, self.tile_to_check.column + 1
                self.tile_checker(self.maze_tile_object_map[row][column], run_until_exit_or_hole_map)
                if self.path_found:
                    break
            if self.tile_to_check.row + 1 < len(self.maze_tile_object_map) and len(
                    self.maze_tile_object_map[self.tile_to_check.row + 1]) >= self.tile_to_check.column:  # S
                row, column = self.tile_to_check.row + 1, self.tile_to_check.column
                self.tile_checker(self.maze_tile_object_map[row][column], run_until_exit_or_hole_map)
                if self.path_found:
                    break
            if self.tile_to_check.column - 1 != -1:  # W
                row, column = self.tile_to_check.row, self.tile_to_check.column - 1
                self.tile_checker(self.maze_tile_object_map[row][column], run_until_exit_or_hole_map)
                if self.path_found:
                    break
            if len(self.tiles_to_check) == 0:
                self.tiles_to_check = deepcopy(self.tiles_to_check_next)
                self.tiles_to_check_next_no_modification = deepcopy(self.tiles_to_check_next)
                self.tiles_to_check_next = []
        if len(self.tiles_to_check) == 0 and not self.path_found:
            print("(None, -1)")
            return None, -1
        else:
            return self.return_path()

    def return_path(self):
        """Return maze path from start to end."""
        row, column = self.end_tile.row, self.end_tile.column
        path_end_to_start = [(self.end_tile.row, self.end_tile.column)]
        while True:
            row, column = self.maze_tile_object_map[row][column].row_to_here, self.maze_tile_object_map[row][column].column_to_here
            if (row is not None) and (column is not None) != 0:
                path_end_to_start.append((row, column))
            else:
                break
        path_start_to_end = path_end_to_start[::-1]
        path_start_to_end = (path_start_to_end, self.end_tile.cost_to_here)
        print(f"Final result: {path_start_to_end}")
        return path_start_to_end

    def tile_checker(self, target_tile, run_until_exit_or_hole_map):
        """Individual tile pathfinding helper.

        Modify target_tile data and add it to be checked back in the main pathfinding function if possible.
        If target_tile slowness is 2 or more then first tile to be adjacent to target_tile will be checked again, until
        target_tile slowness is 1 or a path to end is already found.

        :param target_tile: tile object being checked.
        """
        if target_tile.character_value < 0:  # tile is a wall
            pass
        elif target_tile.character_value == 0 and target_tile not in self.tiles_not_to_visit_again and target_tile not in self.start_doors:
            # Tile must be passed with current cycle. Tiles that are one of the original starting doors will be ignored.
            target_tile.cost_to_here = self.tile_to_check.cost_to_here
            target_tile.row_to_here = self.tile_to_check.row
            target_tile.column_to_here = self.tile_to_check.column
            if target_tile.is_end and run_until_exit_or_hole_map == "exit":  # Reached the end.
                self.end_tile = target_tile
                self.path_found = True
                print(target_tile)
                print("Path found!")
                self.print_maze_tile_object_map()
            elif target_tile not in self.tiles_to_check and target_tile not in self.end_doors:
                self.tiles_not_to_visit_again.append(target_tile)
                self.tiles_to_check.insert(0, target_tile)
            print(target_tile)
        elif target_tile.changing_character_value == 1 and target_tile.cost_to_here >= self.tile_to_check.cost_to_here + 1:
            # Move to tile, add that tile to be checked next cycle.
            target_tile.cost_to_here = self.tile_to_check.cost_to_here + target_tile.character_value
            target_tile.row_to_here = self.tile_to_check.row
            target_tile.column_to_here = self.tile_to_check.column
            if target_tile not in self.tiles_to_check_next:
                self.tiles_to_check_next.append(target_tile)
            print(target_tile)
        elif target_tile.changing_character_value > 1 and target_tile.cost_to_here >= self.tile_to_check.cost_to_here + target_tile.character_value:
            # Slow tile, first adjacent tile to this will be checked until a path to end is found or until slow tile can pass previous check.
            if target_tile.row_to_here is not None and self.tile_to_check.row != target_tile.row_to_here and self.tile_to_check.column != target_tile.column_to_here:
                print(f"Tile is being checked by inefficient route! Tile {target_tile}")
            else:
                target_tile.row_to_here = self.tile_to_check.row
                target_tile.column_to_here = self.tile_to_check.column
                target_tile.changing_character_value -= 1
                if self.tile_to_check not in self.tiles_to_check_next:
                    self.tiles_to_check_next.append(self.tile_to_check)
                print(target_tile)
        # else a quicker path to target tile already exists or tile is a wall, tile will be ignored.

    def print_maze_tile_object_map(self):
        """Print maze tile objects in a readable format."""
        for row in range(len(self.maze_tile_object_map)):
            print()
            for column in range(len(self.maze_tile_object_map[row])):
                print(self.maze_tile_object_map[row][column],
                      end=" " * (abs(90 - len(str(self.maze_tile_object_map[row][column])))))
        print()
        print()

    def reset_map(self, configuration, maze_str):
        """Reset the maze"""
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
        self.maze_map = []
        self.maze_tile_object_map = []
        self.tiles_to_check_next_no_modification = []
        self.min_changing_character_value_2_or_higher = None
        self.tiles_to_check = []
        self.tile_to_check = None
        self.tiles_to_check_next = []
        self.tiles_not_to_visit_again = []
        self.end_doors = []
        self.start_doors = []
        self.path_found = False
        self.end_tile = None


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
        print(f"Path start to end: {path_start_to_end}")
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
