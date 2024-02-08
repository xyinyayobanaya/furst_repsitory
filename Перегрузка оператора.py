class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        if isinstance(other, Building):
            return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType
        return False

building1 = Building(7, "жилой")
building2 = Building(7, "офисный")
building3 = Building(7, "жилой")

print(building1 == building2)  # False
print(building1 == building3)  # True