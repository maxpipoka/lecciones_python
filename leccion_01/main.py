import string
import random
from dataclasses import dataclass


@dataclass
class VehicleInfo:
    brand: str
    catalogue_price: int
    electric: bool

    def compute_tax(self):
        # compute the tax percentage (default 5% of the catalogue price, except for electric cars where it is 2%)
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02

        # compute the payable tax
        return tax_percentage * self.catalogue_price


@dataclass
class Vehicle:
    vehicle_id: str
    license_plate: str
    info: VehicleInfo


class VehicleRegistry:

    vehicle_info = {}

    def __init__(self):
        self._add_vehicle_info("Tesla Model 3", 60000, True)
        self._add_vehicle_info("Volkswagen ID3", 35000, True)
        self._add_vehicle_info("BMW 5", 45000, False)

    def _add_vehicle_info(self, brand: str, catalogue_price: int, electric: bool) -> None:
        self.vehicle_info[brand] = VehicleInfo(brand, catalogue_price, electric)

    def _generate_vehicle_id(self, length: int) -> str:
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def _generate_vehicle_license(self, id: str) -> str:
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand: str) -> Vehicle:
        # generate a vehicle id of length 12
        vehicle_id = self._generate_vehicle_id(12)

        # now generate a license plate for the vehicle
        # using the first two characters of the vehicle id
        license_plate = self._generate_vehicle_license(vehicle_id)

        return Vehicle(vehicle_id, license_plate, self.vehicle_info[brand])


class Application:

    def register_vehicle(self, brand: str) -> Vehicle:
        # create a registry instance
        registry = VehicleRegistry()
        return registry.create_vehicle(brand)

        #return brand, new_vehicle.vehicle_id, new_vehicle.license_plate, new_vehicle.info.compute_tax()

#app = Application()
#brand, vehicle_id, license_plate, payable_tax = app.register_vehicle("Volkswagen ID3")
# print out the vehicle registration information
#print("Registration complete. Vehicle information:")
#print(f"Brand: {brand}")
#print(f"Id: {vehicle_id}")
#print(f"License plate: {license_plate}")
#print(f"Payable tax: {payable_tax}")