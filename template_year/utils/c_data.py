from __future__ import annotations
from dataclasses import dataclass
from typing import *

class Range:
    """
    Represents a range in the format a < x < b, where a and b are integers and x is a random value in between the two integers

    Args:
        lower (int): Lower value of range
        upper (int): Upper value of range
    """
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def __repr__(self) -> str:
        return f"[{self.lower}, {self.upper}]"
    
    def intersection(self, other: Range) -> Range:
        """
        Returns the highest minimum and smallest maximum intersection points of 2 ranges as a Range() object, or None if the ranges do not intersect

        Example:
        ----------
                -------
        Code returns Range(8, 10)

        ---------
                    -----
        Code returns None


        Args: 
            other (Range): Range to be comapred to

        Returns:
            Range: Highest minimum and smallest maximum points of the 2 ranges
        """
        tmp = Range(max(self.lower, other.lower), min(self.upper, other.upper))
        return tmp if tmp.lower < tmp.upper else None

    def subtraction(self, other) -> list[Range]:
        """
        Returns the subtraction of 2 intersecting ranges

        Args:
            other (Range): Other range to be compared to
        
        Returns:
            list[Range]: Product of subtracting 2 intersecting ranges
        """
        intersection = self.intersection(other)
        if intersection == None:
            """
            If there are no intersections found, return Range() object containing the current lower and upper values

            Visualisation:
            --------          (Our range)
                     -------- (Intersecting range)
            """
            return [Range(self.lower, self.upper)]
        elif (intersection.lower, intersection.upper) == (self.lower, self.upper):
            """
            If the lower and upper values of the intersecting range is the same as ours, return an empty list

            Visualisation:
            -------- (Our range)
            -------- (Intersecting range)
            """
            return []
        elif intersection.lower == self.lower:
            """
            If the lower value of the intersecting range is the same as ours, return a Range() object with the upper values of the two ranges

            Visualisation:
            --------- (Our range)
            ---       (Intersecting range)
            """
            return [Range(intersection.upper, self.upper)]
        elif intersection.upper == self.upper:
            """
            If the upper value of the intersecting range is the same as ours, return a Range() object with the lower values of the two ranges

            Visualisation:
            ------- (Our range)
               ---- (Intersecting range)
            """
            return [Range(self.lower, intersection.lower)]
        else:
            """
            If none of the ranges' values match, return a list of two Range() objects containing the lower and upper values respectively

            Visualisation:
            --------- (Our range)
              ---     (Intersecting range)
            """
            return [Range(self.lower, intersection.lower), Range(intersection.upper, self.upper)]
    
    def add(self, offset: int | float) -> Range:
        """
        Return the product of the addition of an offset to the current range

        Args:
            offset (int | float): Offset to add to range
        
        Returns:
            Range: offsetted range
        """
        return Range(self.lower + offset, self.upper + offset)
    

@dataclass
class Coordinates:
    """
    Custom class used to represent a set of coordinates
    """
    x: int
    y: int
    

@dataclass
class Node:
    """
    Custom class used to represent a node for A* pathfinding
    """
    parent: any
    position: Tuple(int, int)

    g: int = 0  # Cost of path from start node to current node
    h: int = 0  # Heuristics - Est. distance from current node to end node
    f: int = 0  # Total cost of node

    def __eq__(self, other):
        return self.position == other.position