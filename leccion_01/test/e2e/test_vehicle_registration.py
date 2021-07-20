import unittest
from lecciones_python.leccion_01.main import Application


class TestVehicleRegistration(unittest.TestCase):
    def test_brand_no_change(self):
        app = Application()
        brand, vehicle_id, license_plate, payable_tax = app.register_vehicle("Volkswagen ID3")
        self.assertEqual("Volkswagen ID3", brand)

    def test_id_have_right_length(self):
        app = Application()
        brand, vehicle_id, license_plate, payable_tax = app.register_vehicle("Volkswagen ID3")
        length_vehicle_id = len(vehicle_id)
        self.assertEqual(length_vehicle_id, 12)

    def test_have_licence_plate(self):
        app = Application()
        brand, vehicle_id, license_plate, payable_tax = app.register_vehicle("Volkswagen ID3")
        length_license_plate = len(license_plate)
        self.assertEqual(length_license_plate, 8)

    def test_payable_tax_amount_electric(self):
        app = Application()
        brand, vehicle_id, license_plate, payable_tax = app.register_vehicle("Volkswagen ID3")
        self.assertEqual(payable_tax, 700)


    def test_payable_tax_amount_non_electric(self):
        app = Application()
        brand, vehicle_id, license_plate, payable_tax = app.register_vehicle("BMW 5")
        self.assertEqual(payable_tax, 2250)


if __name__ == '__main__':
    unittest.main()


