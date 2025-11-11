# Exercise 4:
    # Implement the following accessor and mutator:
    # • get(index) which returns the value of the element at position index in the vector
    # • set(index, value) which set the element at position index to the new value
    # value. The method does not return any value.

    # -------------------------------------------------------------------------------

    # Let’s implement the scalar product method scalar_product(scalar) as an example.
    # The method needs only one parameter, the scalar. In addition, the method should return a new
    # Vector containing the result of the operation, but MUST NOT modify the calling instance,
    # e.g. my_vector.scalar_product(3) must not modify the instance my_vector.
        # def scalar_product(self, scalar):
        # ''' add some doc-string'''
        # pass

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
    
    def __getitem__(self, index:int) -> float:
        return self._vector[index]
    
    def __setitem__(self, index:int, value:float) -> None:
        self._vector[index] = value

    def scalar_product(self, scalar:float) -> 'Vector':
        values_ = []
        for v in self._vector:
            values_.append(scalar * v)
        return Vector(values_)