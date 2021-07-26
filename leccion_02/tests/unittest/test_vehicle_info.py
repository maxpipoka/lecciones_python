from unittest import TestCase

from leccion_02.main import VehicleInfo
# from leccion_02 import VehicleInfo
# from lecciones_python.leccion_02.main import VehicleInfo


class TestVehicleInfo(TestCase):
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

    def test_catalogue_price_minor_exemption_amonunt(self):
        # create a vehicle info object
        v = VehicleInfo("BMW", True, 10000)
        # compute the tax
        tax = v.compute_tax(15000)

        self.assertEqual(tax, 0)

    # you can only lease this car if the catalogue price is not more than 70% of
    # your year income; year_income should be >= 0
    # def can_lease(self, year_income: int) -> bool:

    def test_catalogue_price_minor_70_percent_year_income(self):
        v = VehicleInfo("BMW", True, 69)
        self.assertTrue(v.can_lease(100))

    def test_catalogue_price_equal_70_percent_year_income(self):
        v = VehicleInfo("BMW", True, 70)
        self.assertTrue(v.can_lease(100))

    def test_catalogue_price_mayor_70_percent_year_income(self):
        v = VehicleInfo("BMW", True, 71)
        self.assertFalse(v.can_lease(100))

    def test_year_income_value_negative(self):
        v = VehicleInfo("BMW", True, 71)
        self.assertRaises(ValueError, v.can_lease, -1)
        # devuelve verdadero si devuelve error del tipo ValueError, al llamar la funcion pasandole ese valor.

# if __name__ == '__main__':
#     unittest.main()
