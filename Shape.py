import math

# Point class
class Point:
    def __init__(self, x, y):
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            raise TypeError("Coordinates must be numbers") ##Indica error si se intentan incluir valores no numéricos para las coordenadas
        self.x = x
        self.y = y

    def compute_distance(self, other_point):
        if not isinstance(other_point, Point):
            raise TypeError("Argument must be a Point instance") ##Indica error si se intenta calcular una distancia entre dos elementos "no puntos"
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

# Line class
class Line:
    def __init__(self, start_point, end_point):
        if not all(isinstance(p, Point) for p in [start_point, end_point]):
            raise TypeError("Start and end points must be Point instances") ##Indica error si alguno de los puntos (final o inicial), no es de tipo punto
        self.start_point = start_point
        self.end_point = end_point
        self.length = self.compute_length()

    def compute_length(self):
        return self.start_point.compute_distance(self.end_point)

# Shape class
class Shape:
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.inner_angles = []
        self.is_regular = False

    def compute_area(self):
        raise NotImplementedError("Subclasses should implement this method")
    
    def compute_perimeter(self):
        raise NotImplementedError("Subclasses should implement this method")

# Triangle class
class Triangle(Shape):
    def __init__(self, p1, p2, p3):
        super().__init__()
        self.vertices = [p1, p2, p3]
        self.edges = [Line(p1, p2), Line(p2, p3), Line(p3, p1)]
        try:
            self.inner_angles = self.compute_angles()
        except ValueError as e:
            raise ValueError("Invalid triangle: " + str(e))
    
    def compute_angles(self):
        a, b, c = (self.edges[0].length, self.edges[1].length, self.edges[2].length)
        try: ##Verifica que los lados del triángulo conformen un triángulo (ningun par es paralelo)
            angle_A = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
            angle_B = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
            angle_C = math.acos((a**2 + b**2 - c**2) / (2 * a * b))
        except ValueError:
            raise ValueError("Triangle sides do not form a valid triangle")
        return [math.degrees(angle_A), math.degrees(angle_B), math.degrees(angle_C)]
    
    def compute_area(self):
        a, b, c = (self.edges[0].length, self.edges[1].length, self.edges[2].length)
        s = (a + b + c) / 2
        try: ##Verifica que el triángulo efectivamente tenga un área (ningún punto se solapa)
            return math.sqrt(s * (s - a) * (s - b) * (s - c))
        except ValueError:
            raise ValueError("Invalid triangle: Area calculation failed")

    def compute_perimeter(self):
        return sum(edge.length for edge in self.edges)

# Square class
class Square(Shape):
    def __init__(self, p1, p2, p3, p4):
        super().__init__()
        self.vertices = [p1, p2, p3, p4]
        self.edges = [Line(p1, p2), Line(p2, p3), Line(p3, p4), Line(p4, p1)]
        if not all(math.isclose(self.edges[0].length, edge.length) for edge in self.edges):
            raise ValueError("All sides must be equal for a square") ##Indica error si los lados no son iguales, y se intenta pasar como cuadrado
    
    def compute_area(self):
        return self.edges[0].length ** 2
    
    def compute_perimeter(self):
        return 4 * self.edges[0].length

# Example usage:
p1 = Point(0, 0)
p2 = Point(5, 0)
p3 = Point(5, 5)
p4 = Point(0, 5)

try: ##Si el área o el perímetro del cuadrilátero no se pueden calcular (valores negativos), muestra un error
    square = Square(p1, p2, p3, p4)
    print(f"Square area: {square.compute_area()}")
    print(f"Square perimeter: {square.compute_perimeter()}")
except Exception as e:
    print(f"Error creating square: {e}")

try: ##Si el área o el perímetro del triángulo no se pueden calcular (valores negativos), muestra un error
    t1, t2, t3 = Point(0, 0), Point(4, 0), Point(4, 3)
    triangle = Triangle(t1, t2, t3)
    print(f"Triangle area: {triangle.compute_area()}")
    print(f"Triangle perimeter: {triangle.compute_perimeter()}")
except Exception as e:
    print(f"Error creating triangle: {e}")
