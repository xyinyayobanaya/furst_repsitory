class Car:
    price = 1000000

    def horse_powers(self):
        return "Unknown horsepower"

class Nissan(Car):
    price = 1500000

    def horse_powers(self):
        return "200 horsepower"

class Kia(Car):
    price = 800000

    def horse_powers(self):
        return "150 horsepower"


car = Car()
nissan = Nissan()
kia = Kia()

print(f"Car price: {car.price}")
print(f"Car horsepower: {car.horse_powers()}")

print(f"Nissan price: {nissan.price}")
print(f"Nissan horsepower: {nissan.horse_powers()}")

print(f"Kia price: {kia.price}")
print(f"Kia horsepower: {kia.horse_powers()}")