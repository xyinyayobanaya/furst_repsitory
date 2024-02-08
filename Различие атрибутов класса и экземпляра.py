class Building:
    total = 0

    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType
        Building.total += 1

    def __str__(self):
        return f"Building with {self.numberOfFloors} floors, building type: {self.buildingType}"

# Создание 40 объектов класса Building
buildings = []
for i in range(40):
    building = Building(i+1, "Жилой")
    buildings.append(building)

# Вывод объектов на экран
for building in buildings:
    print(building)