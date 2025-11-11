# Exercise: Practicing Classes
    # Create a class Circle having two attributes, centre a tuple (x,y) to record 
    # the centre of the cricle, and radius a float that records the radius of the circle. 
    # Implement the __init__ method with two parameters to initialise the attributes of the circle, 
    # the first parameter being a tuple (x,y) representing the coordinates 
    # of the centre and the second parameter being a float containing the radius of the cricle.

    #     (a) Implement a method getArea() that returns the area of the circle
    #     (b) Implement a method getPerimeter() that returns the perimeter of the circle.

    # Create a class Triangle having one attribute vertices, a list of three tuples (x,y) 
    # containing the coordinates of the three vertices. 
    # Implement the __init__ method with three parameters to initialise the attributes of the triangle, 
    # each parameter is a tuple (x,y) representing the coordinates of one of the vertices. 

        # (c) Implement a method getArea() that returns the area of the triangle.
        # (d) Implement a method getPerimeter() that returns the perimeter of the triangle.
        # (e) Implement a method getInscribedCircle() that returns the inscribed circle of the triangle. 
        #     The returned value must be of thetype Circle implemented earlier.
        # (f) Implement a method getCircumscribedCircle() that returns the circumscribed circle of the triangle. 
        #     The returned value must be of the type Circle implemented earlier.

PI = 3.14

class Circle:
    def __init__(self, centre:tuple[float, float], radius:float) -> None:
        self.centre = centre
        self.radius = radius

    def getArea(self) -> float:
        return PI * pow(self.radius, 2)
    
    def getPerimeter(self) -> float:
        return 2 * PI * self.radius
    
class Triangle:
    def __init__(self, a:tuple[float, float], b:tuple[float, float], c:tuple[float, float]) -> None:
        self.vertices = [a, b, c]

    def getArea(self) -> float:
        (x1, y1), (x2, y2), (x3, y3) = self.vertices
        return 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    
    def getPerimeter(self) -> float:
        (x1, y1), (x2, y2), (x3, y3) = self.vertices

        a = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
        b = ((x3 - x2)**2 + (y3 - y2)**2) ** 0.5
        c = ((x1 - x3)**2 + (y1 - y3)**2) ** 0.5
        
        return a + b + c
    
    def getInscribedCircle(self) -> Circle:
        (x1, y1), (x2, y2), (x3, y3) = self.vertices

        a = ((x2 - x3)**2 + (y2 - y3)**2) ** 0.5
        b = ((x1 - x3)**2 + (y1 - y3)**2) ** 0.5
        c = ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5

        s = (a + b + c) / 2

        area = self.getArea()

        r = area / s

        x = (a * x1 + b * x2 + c * x3) / (a + b + c)
        y = (a * y1 + b * y2 + c * y3) / (a + b + c)

        return Circle((x, y), r)
    
    def getCircumscribedCircle(self) -> Circle:
        (x1, y1), (x2, y2), (x3, y3) = self.vertices

        D = 2 * (x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))

        x = ((x1**2 + y1**2)*(y2 - y3) + 
              (x2**2 + y2**2)*(y3 - y1) + 
              (x3**2 + y3**2)*(y1 - y2)) / D

        y = ((x1**2 + y1**2)*(x3 - x2) + 
              (x2**2 + y2**2)*(x1 - x3) + 
              (x3**2 + y3**2)*(x2 - x1)) / D

        r = ((x - x1)**2 + (y - y1)**2) ** 0.5

        return Circle((x, y), r)