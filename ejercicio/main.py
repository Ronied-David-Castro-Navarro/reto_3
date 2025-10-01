import math

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self.length = self.compute_length()
        self.slope = self.compute_slope()

    def compute_length(self) -> float:
        return math.sqrt(
            (self.end.x - self.start.x) ** 2 +
            (self.end.y - self.start.y) ** 2
        )

    def compute_slope(self) -> float:
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
        if dx == 0:
            return float("inf")
        return math.degrees(math.atan2(dy, dx))

    def compute_horizontal_cross(self) -> bool:
        return (self.start.y * self.end.y) <= 0

    def compute_vertical_cross(self) -> bool:
        return (self.start.x * self.end.x) <= 0

    def __repr__(self):
        return f"Line({self.start}, {self.end})"


class Rectangle:
    def __init__(self, lines: list[Line]):
        if len(lines) != 4:
            raise ValueError("A rectangle must have exactly 4 lines.")
        self.lines = lines

    def perimeter(self) -> float:
        return sum(line.length for line in self.lines)

    def area(self) -> float:
        width = self.lines[0].length
        height = self.lines[1].length
        return width * height

    def __repr__(self):
        return f"Rectangle with perimeter {self.perimeter():.2f} and area {self.area():.2f}"


if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(4, 0)
    p3 = Point(4, 3)
    p4 = Point(0, 3)

    l1 = Line(p1, p2)
    l2 = Line(p2, p3)
    l3 = Line(p3, p4)
    l4 = Line(p4, p1)

    rect = Rectangle([l1, l2, l3, l4])

    print("L1 length:", l1.length)
    print("L2 length:", l2.length)
    print("L1 slope:", l1.compute_slope())
    print("L2 slope:", l2.compute_slope())
    print("Perimeter:", rect.perimeter())
    print("Area:", rect.area())
    print(rect)
