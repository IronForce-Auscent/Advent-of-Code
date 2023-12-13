def calculate_manhatten_distance(origin: tuple[int, int], target: tuple[int, int]) -> int | float:
    """
    Calculates the Manhatten distance between two nodes

    :param origin: The coordinates of the origin node
    :type origin: tuple(x: int, y: int)
    :param target: The coordinates of the target node
    :type target: tuple(x: int, y: int)

    :return: The calculated Manhatten distance between the two nodes
    :rtype: int | float
    """
    return abs(origin[0] - target[0]) + abs(origin[1] - target[1])