class Vehicle:
    vehicle_type = "none"


class Car(Vehicle):
    price = 1000000

    def horse_powers(self):
        return "Unknown horsepower"


class Nissan(Car):
    price = 1500000
    vehicle_type = "Nissan"

    def horse_powers(self):
        return "200 horsepower"


nissan = Nissan()
print(f"Vehicle type: {nissan.vehicle_type}")
print(f"Price: {nissan.price}")