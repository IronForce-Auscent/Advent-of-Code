from typing import *
from numpy import Inf

from .c_exceptions import PathfinderException
from .c_wrapper import timer
from .c_data import Node

import heapq
import random

WALKABLE, UNWALKABLE = 0, 1

class PathFinder:
    """
    A custom function to perform pathfinding algorithms and calculate distances between two points using various
    pathfinding algorithms

    Currently supported algorithms:
        - Djikstra's algorithm (naive and lazy)
        - A* algorithm

    For 2D grids, nodes should be marked using this convention
        0 - Walkable terrain
        1 - Unwalkable terrain
        X, Y - Start/End points (optional), defaults to (0,0) and (row_count - 1, column_count - 1) for origin and destination respectively

    Args:
        graph (dict[int: list[Tuple]] | list[list[str | int]]): Adjacency list representation of graph with key:value pairing of 
                    "node ID:[(other node ID: distance)]" / Grid representation with nodes marked
        origin (Tuple): Coordinates of origin node
        destination (Tuple): Coordinates of destination node
    """
    
    def __init__(self, graph: dict[int: list[Tuple]] | list[list[str | int]], origin: (int, int), destination: (int, int)):
        """
        Constructor method
        """
        self.graph = graph
        self.origin = origin
        self.destination = destination

    @timer    
    def djikstra_naive(self, root: int) -> list[int]:
        """
        Naive djikstra's algorithm using a brute-force solution to calculate the distances between all other nodes in a tree/network from an
        origin node

        Note: Only works with an adjacency list of representation of nodes and edge weights

        Example network represented as an adjacency list:

        sample_network = {
            0: [(1, 1)],
            1: [(0, 1), (2, 2), (3, 3)],
            2: [(1, 2), (3, 1), (4, 5)],
            3: [(1, 3), (2, 1), (4, 1)],
            4: [(2, 5), (3, 1)]
        }

        Args:
            graph (dict): Adjacency list representation of network
            root (int): The ID of the root node

        Returns:
            list[int]: List of distances from origin node to other nodes in the network, in order of ID
        """
        n = len(self.graph)
        distances = list(Inf for _ in range(n)) # Initialize a list of distances with default values of infinity
        distances[root] = 0  # Set the distance from the origin (root) node to 0        
        visited = [False for _ in range(n)] # Initialize a list of visited nodes

        # Loop through each node
        for _ in range(n):
            # Create a "start node" with a value of -1 (to signify we don't have a start/next node yet)
            u = -1
            # Loop through all nodes to check for visitation status
            for i in range(n):
                """
                Check if the current node "i" hasn't been visited and we haven't processed "i" or if the distance we have
                for "i" is less than the distance we have from the "start node"
                """
                if not visited[i] and (u == -1 or distances[i] < distances[u]):
                    u = i
            
            if distances[u] == Inf:
                # All nodes have been visited or node cannot be reached for whatever reason
                break

            visited[u] = True  # Adds the closest node to the list of visited nodes

            # Compares the distances to each node from the "start node" with the distances currently recorded
            for v, l in self.graph[u]:
                if distances[u] + l < distances[v]:
                    distances[v] = distances[u] + l
        return distances

    @timer
    def djikstra_lazy(self, root: int) -> list[int]:
        """
        Alternate implementation of the djikstra's algorithm, faster as it does not have to search through each node
        explicitly

        Note: Only works with an adjacency list of representation of nodes and edge weights

        Example network represented as an adjacency list:

        sample_network = {
            0: [(1, 1)],
            1: [(0, 1), (2, 2), (3, 3)],
            2: [(1, 2), (3, 1), (4, 5)],
            3: [(1, 3), (2, 1), (4, 1)],
            4: [(2, 5), (3, 1)]
        }

        Args:
            graph (dict): Adjacency list representation of network
            root (int): The ID of the root node

        Returns:
            list[int]: List of distances from origin node to other nodes in the network, in order of ID
        """
        n = len(self.graph)
        distances = list(Inf for _ in range(n)) # Initialize a list of distances with default values of infinity
        distances[root] = 0  # Set the distance from the origin (root) node to 0        
        visited = [False for _ in range(n)] # Initialize a list of visited nodes

        priority_queue = [(0, root)] # Create a priority queue
        while len(priority_queue) > 0:
            # Still have some nodes to process, let's keep going
            # Get the root ID and discard the current distance
            _, u = heapq.heappop(priority_queue)
            # Check if we have previously visited this node. If so, skip it
            if visited[u]:
                continue
            # Add this node to the visited list
            visited[u] = True

            for v, l in self.graph[u]:
                if distances[u] + l < distances[v]:
                    distances[v] = distances[u] + l
                    heapq.heappush(priority_queue, (distances[v], v))
        return distances

    def astar_grid(self):
        """
        An implementation of the A* pathfinding algorithm on a 2-dimensional grid

        Args:
            ...
        
        Returns:
            A list of tuples as a path from a given origin to a given destination in the given grid/maze

        Raises:
            PathfindingException: Origin node must be a traversable node
            PathfindingException: Destination node must be a traversable node
        """
        # Check if the nodes are walkable
        if self.graph[self.origin[0]][self.origin[1]] == UNWALKABLE:
            raise PathfinderException("Origin node must be a traversable node")
        if self.graph[self.destination[0]][self.destination[1]] == UNWALKABLE:
            raise PathfinderException(f"Destination node must be a traversable node. (Node {self.destination}: {self.graph[self.destination[0]][self.destination[1]]})")

        # Create the start and end nodes
        start_node = Node(None, self.origin)
        start_node.g = start_node.f = start_node.h = 0
        end_node = Node(None, self.destination)
        end_node.g = end_node.f = end_node.h = 0

        # Initialize open and closed lists
        open_list = []
        closed_list = []

        # Add the start node to the open list
        open_list.append(start_node)

        # Loop until we find the end node
        while len(open_list) > 0:
            # Get current node
            current_node: Node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index
            
            # Pop the current node off from open list, add to closed list
            open_list.pop(current_index)
            closed_list.append(current_node)

            # Check if arrived at goal
            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1], len(path) # Return a reversed path and path length
            
            # Generate children
            children = []
            adjacent_offsets = [(0, -1), (0, 1), (-1, 0), (1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
            for offset in adjacent_offsets:
                # Get the node's offsetted position
                node_position = (current_node.position[0] + offset[0], current_node.position[1] + offset[1])

                # Check if the node is in range
                if node_position[0] > (len(self.graph) - 1) or node_position[0] < 0 or node_position[1] > (len(self.graph[len(self.graph) - 1]) - 1) or node_position[1] < 0:
                    continue

                # Check if terrain is walkable
                if self.graph[node_position[0]][node_position[1]] != WALKABLE:
                    continue

                # Create a new node and add to the open list
                new_node = Node(current_node, node_position)
                children.append(new_node)
            
            # Loop through all children nodes
            for child in children:
                # Check if child is in the closed list
                    for closed_child in closed_list:
                        if child == closed_child:
                            continue
                    
                    # Create f, g and h values
                    child.g = current_node.g + 1
                    child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
                    child.f = child.g + child.h

                    # Check if child is already in the open list
                    for open_node in open_list:
                        if child == open_node and child.g > open_node.g:
                            continue
                    
                    # Add child node to open list
                    open_list.append(child)


    @timer
    def astar_graph(self):
        """
        An implementation of the A* pathfinding algorithm on a directed/undirected graph
        """
        NotImplemented

def calculate_manhatten_distance(origin: tuple[int, int], target: tuple[int, int]) -> int | float:
    """
    Calculates the Manhatten distance between two nodes by taking the
    sum of the distances in the cardinal directions (North, South, East, West)

    Args:
        Origin (tuple): The coordinates of the origin node
        Target (tuple): The coordinates of the destination node

    Returns:
        int | float: Calculated Manhatten distance between the two nodes
    """
    return abs(origin[0] - target[0]) + abs(origin[1] - target[1])

def calculate_chebyshev_distance(origin: tuple[int, int], target: tuple[int, int]) -> int | float:
    """
    Calculates the Chebyshev (or "Chessboard") distance between two nodes by taking the
    maximum of the horizontal and vertical distances (in the ordinal directions)

    Args:
        Origin (tuple): The coordinates of the origin node
        Target (tuple): The coordinates of the destination node

    Returns:
        int | float: Calculated Chebyshev distance between the two nodes
    """
    return max(abs(origin[0] - target[0]), abs(origin[1] - target[1]))


def generate_network(node_count: int = 10, max_distance: int | float = 1000, probability: float = 0.25) -> dict:
    """
    Helper function to generate a random network as an adjacency list

    Args:
        node_count (int): Total number of nodes to generate, defaults to 10
        max_distance (int | float | None): The maximum distance between any 2 nodes, defaults to None (max distance is 1000)
        probability (float): Probability that a given node will be connected to another node, defaults to 0.25

    Returns:
        dict: Network represented as an adjacency list with node ID:[(other node ID: distance)] as key:value pair

    Raises:
        PathfinderException: Probability chance should be a floating point value between 0 and 1 inclusive
    """
    if not (0 < probability <= 1):
        raise PathfinderException("Probability chance should be a floating point value between 0 and 1 inclusive")
    network = {}
    for node in range(node_count):
        connections = []
        connected_nodes = [n for n in range(node_count) if random.random() < probability and n != node]
        for connected_node in connected_nodes:
            connections.append((connected_node, random.randint(0, max_distance)))
        network[node] = connections
    return network