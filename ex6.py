# Exercise 6:
    # In Programming, being able to compare objects is important, in particular determining if two
    # objects are equal or not. Let’s try a comparison of two vectors:
        # >>> vector1 = Vector([1, 2, 3])
        # >>> vector2 = Vector([1, 2, 3])
        # >>> vector1 == vector2
        # False
        # >>> vector1 != vector2
        # True
        # >>> vector3 = vector1
        # >>> vector3 == vector1
        # True
    # As you can see, in the current state of implementation of our class Vector does not produce the
    # expected result when comparing two vectors. In the example above the == operator return
    # True if the two vectors are physically stored at the same memory address, it does not compare
    # the content of the two vectors.
    # Therefore, you need to implement a method equals(other_vector) that returns True
    # if the vectors are equals (i.e. have the same value at the same position), False otherwise.

    # Hint: to check if an object is of a certain type you can use isinstance(var, Type). For
    # example isinstance(other_vector, Vector).

    # Once implemented we should have the following results
        # >>> vector1 = Vector([1, 2, 3])
        # >>> vector2 = Vector([1, 2, 3])
        # >>> vector1.equals(vector2)
        # True
        # >>> vector3 = Vector([0, 2, 0])
        # >>> vector3.equals(vector1)
        # False
        # >>> vector1 == vector2
        # False

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
    
    def equals(self, other_vector:'Vector') -> bool:
        if not isinstance(other_vector, Vector):
            raise TypeError("Assessing equality requires both values to be Vector instances.")
        
        if self.dim() != other_vector.dim():
            return False
        
        for i in range(len(self._vector)):
            if self._vector[i] != other_vector._vector[i]:
                return False
        
        return True