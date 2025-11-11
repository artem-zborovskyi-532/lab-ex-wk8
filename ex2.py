# Exercise 2:
    # Another very useful method to write is __str__. This will enable us to print the content of
    # the instance using the print function. For the purpose of this exercise we have decided to
    # represent the vector [𝑎, 𝑏, 𝑐] with the string '<a, b, c>' to differentiate it from a list.

    # Implement __str__.
        # def __str__(self):
            # pass
    # Now let see how we can instantiate (create) some vectors.
        # >>> my_vector = Vector([1, 2, 3])
        # >>> print(my_vector)
        # <1, 2, 3>
        # >>> empty_vector = Vector()
        # >>> print(empty_vector)
        # <>

class Vector:
    def __init__(self, values:list[float]) -> None:
        if values is None or len(values) > 3:
            self._vector = []
        else:
            self._vector = values.copy()

    def __str__(self) -> str:
        return "<" + ", ".join(map(str, self._vector)) + ">"