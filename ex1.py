# Exercise 1: Class’ constructor
    # First of all, create a module called vector.py, then define the class Vector. The next step is to
    # define what will be the internal representation of a vector and then write the constructor
    # __init__. The design decision is to store the element of the vector [𝑎, 𝑏, 𝑐] in a list [a,b,c].
    # The constructor will take only one parameter, a list of float. The instance attribute _vector.
    # should have a copy of the list passed in the parameters.
        # def __init__(self, data = None):
        # “”” some doc-string “””
        # Pass

class Vector:
    def __init__(self, values:list[float]) -> None:
        if values is None or len(values) > 3:
            self._vector = []
        else:
            self._vector = values.copy()