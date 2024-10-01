class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.spaces = [big, medium, small]
        self.carTypes = [None, 0, 1, 2]
        

    def addCar(self, carType: int) -> bool:
        if self.spaces[self.carTypes[carType]] <= 0:
            return False
        
        self.spaces[self.carTypes[carType]] -= 1
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)