import time

class Cell:
    North = 1 << 0
    East = 1 << 1
    South = 1 << 2
    West = 1 << 3

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.walls = 15

    def has_wall(self, direction):
        if (self.walls & direction) != 0:
            return True
        return False

    def remove_wall(self , direction : int):
        self.walls -= direction
    
    def connect_cells(self , other : "Cell"):
        dx = other.x - self.x 
        dy = other.y - self.y 

        if ( dx > 0):
            self.remove_wall(2)
            other.remove_wall(8)
        else :
            other.remove_wall(2)
            self.remove_wall(8)
        if ( dy > 0):
            self.remove_wall(4)
            other.remove_wall(1)
        else :
            self.remove_wall(1)
            other.remove_wall(4)

    def __repr__(self):
        return f"Cell({self.x , self.y})"


class Maze:
    def __init__(self, height, width):
        self.height = height
        self.width = width

        self.grid = [[Cell(x, y) for x in range(width)] for y in range(height)]
        lst_grid = [
            [13, 3, 9, 7, 9, 1, 5, 5, 5, 5, 3, 13, 1, 3, 13, 1, 3, 13, 1, 7],
            [11, 10, 12, 5, 6, 12, 5, 3, 9, 7, 12, 3, 10, 12, 5, 6, 12, 3, 12, 3],
            [8, 6, 9, 5, 5, 5, 3, 10, 12, 1, 3, 12, 6, 11, 9, 3, 9, 6, 9, 6],
            [10, 11, 8, 3, 9, 3, 10, 8, 3, 14, 12, 5, 5, 4, 6, 12, 4, 3, 8, 3],
            [10, 12, 6, 10, 10, 14, 10, 14, 10, 9, 5, 5, 5, 5, 5, 3, 11, 10, 14, 10],
            [10, 9, 5, 6, 8, 3, 12, 3, 8, 6, 9, 5, 5, 5, 5, 6, 10, 10, 9, 6],
            [12, 6, 9, 3, 10, 12, 3, 10, 10, 11, 10, 9, 3, 9, 3, 9, 4, 6, 12, 3],
            [9, 3, 10, 12, 6, 11, 12, 6, 8, 6, 10, 14, 12, 6, 10, 12, 5, 3, 9, 2],
            [10, 14, 10, 11, 9, 4, 3, 15, 10, 15, 10, 15, 15, 15, 8, 5, 7, 12, 6, 10],
            [10, 9, 6, 10, 10, 9, 6, 15, 14, 15, 8, 5, 7, 15, 8, 5, 5, 1, 7, 10],
            [10, 12, 3, 10, 10, 12, 3, 15, 15, 15, 10, 15, 15, 15, 10, 13, 3, 12, 5, 6],
            [8, 5, 6, 12, 4, 7, 8, 5, 3, 15, 10, 15, 13, 5, 0, 5, 4, 5, 5, 3],
            [10, 13, 1, 1, 5, 3, 12, 3, 10, 15, 10, 15, 15, 15, 14, 9, 3, 9, 3, 10],
            [12, 3, 10, 10, 9, 6, 13, 6, 10, 9, 4, 1, 5, 7, 9, 6, 12, 6, 10, 10],
            [9, 6, 14, 10, 12, 5, 5, 3, 8, 4, 7, 12, 1, 5, 4, 3, 13, 3, 10, 14],
            [12, 5, 5, 6, 11, 9, 3, 10, 12, 3, 9, 3, 14, 9, 3, 12, 3, 10, 12, 3],
            [13, 5, 5, 3, 8, 6, 12, 6, 9, 6, 10, 12, 5, 6, 10, 13, 2, 8, 7, 10],
            [9, 5, 5, 2, 10, 9, 1, 3, 12, 7, 12, 5, 3, 13, 4, 3, 12, 2, 9, 2],
            [10, 9, 3, 14, 10, 14, 10, 10, 9, 5, 5, 3, 12, 5, 3, 12, 3, 14, 10, 10],
            [12, 6, 12, 5, 4, 5, 6, 12, 6, 13, 5, 4, 5, 5, 6, 13, 4, 5, 6, 14],
        ]
        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x].walls = lst_grid[y][x]

        # maze_generation 
        def generate_dfs(self):
            stack : list[Cell] = []

            start : Cell = self.grid[0][0]
            start.visited = True
            stack.append(start)

            while ( stack ) :
                pass



    # def create_42_cell(self):
    #     center_x = (self.width // 2) - 3
    #     center_y = (self.height // 2) - 2
    #     config = {}
    #     config["pattern"] = {(center_y, center_x)}
    #     if self.width > 7 and self.height > 5:
    #         for y, x in config["pattern"]:
    #             self.grid[y][x].visited = True


maze = Maze(20, 20)

#█
RESET: str = "\033[0m"
color: str = "\x1b[46m"
# ⬜

def display(maze):

    width = maze.width
    height = maze.height
    print(color + "██" * (width * 2 + 1) + RESET)
    for y in range( 0 , height ):
        line_top = color + "██"
        line_bottom = color + "██"

        for x in range ( 0 , width ):
            my_cell = maze.grid[y][x]

            if ( my_cell.walls == 15):
                line_top+= "⬜"
            else :
                line_top += "  "
            
            if ( my_cell.has_wall(2)) :
                line_top += "██"
            else :
                line_top += "  "
            
            if (my_cell.has_wall(4)):
                line_bottom += "████"
            else :
                line_bottom += "  ██"
        print(line_top + RESET)
        print(line_bottom + RESET)
        # time.sleep(0.5)





display(maze)

# print(maze.grid)

# RESET: str = "\033[0m"
# color : str = "\x1b[46m"

# print(color + "abc " + RESET)
# print(color +"Efg")
# print("efg")
