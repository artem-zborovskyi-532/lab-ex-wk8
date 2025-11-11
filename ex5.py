# Exercise 5:
    # Implement the method add(other_vector) that emulate the vector addition operator. The
    # method should return a new vector.
        # • You will have to check that other_vector is a Vector instance, and raise a
        # TypeError if it is not the case.
        # • You must check that both vector have the same dimension, raise a ValueError if it
        # is not the case.
        # • You must return a new Vector instance like we have done in
        # scalar_product(scalar).
    # Once implemented we should be able to do the following:
        # >>> vector1 = Vector([1, 2, 3])
        # >>> vector2 = Vector([0, 1, 3])
        # >>> added = vector1.add(vector2)
        # >>> print(added)
        # <1, 3, 6>

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
    
    def add(self, other_vector:'Vector') -> 'Vector':
        if not isinstance(other_vector, Vector):
            raise TypeError("Addition requires both values to be Vector instances.")
        if self.dim() != other_vector.dim():
            raise ValueError("Addition requires dimensions of both vectors to be equal.")
        
        values_ = []
        for i in range(len(self._vector)):
            values_.append(self._vector[i] + other_vector._vector[i])
        return Vector(values_)