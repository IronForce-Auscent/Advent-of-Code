class BaseException(Exception):
    """
    Base exception for all errors in utility modules
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class PathfinderException(BaseException):
    """
    Exception raised for errors in the pathfinding module
    """

class InputException(BaseException):
    """
    Exception raised for errors in the input module
    """

class DataException(BaseException):
    """
    Exception raised for errors in the data module
    """