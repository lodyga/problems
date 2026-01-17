class DetectSquares:
    """
    Time complexity: 
        add: O(1)
        count: O(n)
    Auxiliary space complexity: O(n)
    Tags:
        DS: hash map
        A: iteration
    """

    def __init__(self):
        # {(x, y): counter}
        self.points = {}

    def add(self, point: list[int]) -> None:
        p = tuple(point)
        self.points[p] = self.points.get(p, 0) + 1

    def count(self, new_point: list[int]) -> int:
        nx, ny = new_point
        counter = 0

        for x, y in self.points:
            if (
                nx != x and
                ny != y and
                abs(nx - x) == abs(ny - y) and
                (nx, y) in self.points and
                (x, ny) in self.points
            ):
                counter += (
                    self.points[(x, y)] *
                    self.points[(nx, y)] *
                    self.points[(x, ny)]
                )

        return counter


detectSquares = DetectSquares()
detectSquares.add([3, 10])
detectSquares.add([11, 2])
detectSquares.add([3, 2])
print(detectSquares.count([11, 10]) == 1)
print(detectSquares.count([14, 8]) == 0)
detectSquares.add([11, 2])
print(detectSquares.count([11, 10]) == 2)
