class DetectSquares:
    """
    Time complexity: 
        add: O(1)
        count: O(n)
    Auxiliary space complexity: O(n)
    Tags: hash map
    """

    def __init__(self):
        self.points = {}  # {(x, y): counter}

    def add(self, point: list[int]) -> None:
        point = tuple(point)
        self.points[point] = self.points.get(point, 0) + 1

    def count(self, new_point: list[int]) -> int:
        nx, ny = new_point
        square_count = 0
        
        for x, y in self.points:
            if (
                    x != nx 
                and y != ny
                and abs(x - nx) == abs(y - ny)
                and (x, ny) in self.points
                and (nx, y) in self.points
            ):
                square_count += self.points[(x, y)] * self.points[(x, ny)] * self.points[(nx, y)]
        
        return square_count
        

detectSquares = DetectSquares()
detectSquares.add([3, 10])
detectSquares.add([11, 2])
detectSquares.add([3, 2])
print(detectSquares.count([11, 10])) # return 1. You can choose:
                              #   - The first, second, and third points
print(detectSquares.count([14, 8]))  # return 0. The query point cannot form a square with any points in the data structure.
detectSquares.add([11, 2])    # Adding duplicate points is allowed.
print(detectSquares.count([11, 10])) # return 2. You can choose:
                              #   - The first, second, and third points
                              #   - The first, third, and fourth points


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)