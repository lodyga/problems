class ParkingSystem:
    """
    Time complexity: O(1)
    Auxiliary space complexity: O(1)
    Tags:
        DS: array
        A: iteration
    """

    def __init__(self, big: int, medium: int, small: int):
        self.parking_slot = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self.parking_slot[carType - 1] == 0:
            return False
        else:
            self.parking_slot[carType - 1] -= 1
            return True


parkingSystem = ParkingSystem(1, 1, 0)
print(parkingSystem.addCar(1) == True)
print(parkingSystem.addCar(2) == True)
print(parkingSystem.addCar(3) == False)
print(parkingSystem.addCar(1) == False)
