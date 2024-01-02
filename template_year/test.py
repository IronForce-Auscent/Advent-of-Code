from utils.c_pathfind import PathFinder
from utils.c_pathfind import generate_network
from utils.c_wrapper import timer

grid_1 = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 0, 1],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0]
    ]
grid_2 = [
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0]
]

@timer
def main(grid, origin, destination):    
    pathfinder = PathFinder(graph=grid, origin=origin, destination=destination)
    path, path_length = pathfinder.astar_grid()
    print(f"Length of path: {path_length}")
    print(f"Path calculated: {path}")

if __name__ == "__main__":
    main(grid_1, (0, 0), (4, 4))
    main(grid_2, (0, 0), (9, 5))