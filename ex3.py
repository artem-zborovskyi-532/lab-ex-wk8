# Exercise 3:
    # Implement the method dim() that returns the dimension of a vector (i.e. the number of
    # elements in a vector)

class Vector:
    def __init__(self, values:list[float]) -> None:
        if values is None or len(values) > 3:
            self._vector = []
        else:
            self._vector = values.copy()

    def __str__(self) -> str:
        return "<" + ", ".join(map(str, self._vector)) + ">"
    
    def dim(self) -> int:
        return len(self._vector)