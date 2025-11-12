class Vector:
    def __init__(self, values:list[float] = []) -> None:
        if values is None or len(values) > 3:
            self._vector = []
        else:
            self._vector = list(map(float, values))

    def __str__(self) -> str:
        return "<" + ", ".join(map(str, self._vector)) + ">"
    
    def dim(self) -> int:
        return len(self._vector)
    
    def get(self, index:int) -> float:
        return self._vector[index]
    
    def __getitem__(self, index:int) -> float:
        return self._vector[index]
    
    def set(self, index:int, value:float) -> None:
        self._vector[index] = value
    
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
            return False
        
        if self.dim() != other_vector.dim():
            return False
        
        for i in range(len(self._vector)):
            if self._vector[i] != other_vector._vector[i]:
                return False
        
        return True