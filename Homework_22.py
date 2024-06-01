class Vehicle:
    vehicle_type = 'none'


class Car:
    price = 1000000

    def horse_power(self):
        self.horse_power_quantity = 100


class Nissan(Car, Vehicle):
    price = 2000000
    vehicle_type = 'sedan'
    print(vehicle_type, price)

    def horse_power(self):
        self.horse_power_quantity = 300


car_1 = Nissan()
