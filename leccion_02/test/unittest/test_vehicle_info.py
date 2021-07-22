import unittest
from lecciones_python.leccion_02.main import VehicleInfo


class TestVehicleInfo(unittest.TestCase):
    def test_non_electric_vehicle(self):
        # create a vehicle info object
        v = VehicleInfo("BMW", False, 10000)

        # compute the tax
        tax = v.compute_tax()

        self.assertEqual(tax, 500)

    def test_electric_vehicle(self):
        # create a vehicle info object
        v = VehicleInfo("BMW", True, 10000)

        # compute the tax
        tax = v.compute_tax()

        self.assertEqual(tax, 200)

    def test_tax_exemption_amount_non_electric(self):
        # create a vehicle info object
        v = VehicleInfo("BMW", False, 10000)

        # compute the tax
        tax = v.compute_tax(5000)

        self.assertEqual(tax, 250)

    def test_tax_exemption_amount_electric(self):
        # create a vehicle info object
        v = VehicleInfo("BMW", True, 10000)

        # compute the tax
        tax = v.compute_tax(5000)

        self.assertEqual(tax, 100)

    def test_exemption_value_negative(self):
        # create a vehicle info object
        v = VehicleInfo("BMW", True, 10000)

        self.assertRaises(ValueError, v.compute_tax, -5000)
        # devuelve verdadero si devuelve error del tipo ValueError, al llamar la funcion pasandole ese valor.

    def test_catalogue_price_value_negative(self):
        # create a vehicle info object

        self.assertRaises(ValueError, VehicleInfo, "BMW", True, -10000)
        # devuelve verdadero si devuelve error del tipo ValueError, al llamar la funcion pasandole ese valor.


if __name__ == '__main__':
    unittest.main()
