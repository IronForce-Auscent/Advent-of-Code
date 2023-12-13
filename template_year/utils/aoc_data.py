from __future__ import annotations

class Range:
    """
    Represents a range in the format a < x < b, where a and b are integers and x is a random value in between the two integers

    :param lower: The lower value of the range
    :type lower: int
    :param upper: The upper value of the range
    :type upper: int

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

        :param other: The range to be compared to
        :type other: Range()
        :return: Highest minimum and smallest maximum points of the 2 ranges
        :rtype: Range()
        """
        tmp = Range(max(self.lower, other.lower), min(self.upper, other.upper))
        return tmp if tmp.lower < tmp.upper else None

    def subtraction(self, other) -> list[Range]:
        """
        Returns the subtraction of 2 intersecting ranges

        :param other: The other range to be compared to
        :type other: Range()
        :return: The product of subtracting 2 intersecting ranges
        :rtype: list[Range()]
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

        :param offset: The offset to add
        :type offset: int | float
        :return: The offsetted range
        :rtype: Range()
        """
        return Range(self.lower + offset, self.upper + offset)
    

class Coordinates:
    """
    Custom class used to represent a set of coordinates

    :param x: The x-coordinate
    :type x: int
    :param y: The y-coordinate
    :type y: int
    """
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"