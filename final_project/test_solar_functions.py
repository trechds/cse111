import unittest
from pytest import approx
import pytest
from solar_budget import *

class TestSolarEnergyProposal(unittest.TestCase):
    
    def test_calculate_required_power(self):
        # Test calculate_required_power function with different energy consumption and irradiation values
        power1 = calculate_required_power(500, 100)  # Test with energy consumption of 500 kWh and irradiation of 100
        self.assertAlmostEqual(power1, 5, delta=0.01)  # Assert the calculated power is approximately 5 kW

        power2 = calculate_required_power(800, 120)  # Test with energy consumption of 800 kWh and irradiation of 120
        self.assertAlmostEqual(power2, 6.67, delta=0.01)  # Assert the calculated power is approximately 6.67 kW

    def test_calculate_total_power(self):
        # Test calculate_total_power function with different module quantities and powers
        total_power1 = calculate_total_power(10, 300)  # Test with 10 modules and 300W power
        self.assertAlmostEqual(total_power1, 3, delta=0.01)  # Assert the calculated total power is approximately 3 kW
        self.assertAlmostEqual(total_power1 * 1000, 3000, delta=0.01)  # Assert the calculated total power in watts is approximately 3000 W
        
        total_power2 = calculate_total_power(20, 400)  # Test with 20 modules and 400W power
        self.assertAlmostEqual(total_power2, 8, delta=0.01)  # Assert the calculated total power is approximately 8 kW
        self.assertAlmostEqual(total_power2 * 1000, 8000, delta=0.01)  # Assert the calculated total power in watts is approximately 8000 W

    def test_get_average_monthly_generation(self):
        # Test get_average_monthly_generation function with different total powers, irradiations, and energy consumptions
        generation1, percentage1 = get_average_monthly_generation(5, 110, 500)  # Test with total power of 5 kW, irradiation of 110, and energy consumption of 500 kWh
        self.assertAlmostEqual(generation1, 550, delta=0.01)  # Assert the calculated average monthly generation is approximately 550 kWh
        self.assertAlmostEqual(percentage1, 10, delta=0.01)  # Assert the calculated surplus percentage is approximately 10%
        self.assertAlmostEqual(generation1 / percentage1, 55, delta=0.01)  # Assert the calculated ratio is approximately 55

        generation2, percentage2 = get_average_monthly_generation(8, 120, 800)  # Test with total power of 8 kW, irradiation of 120, and energy consumption of 800 kWh
        self.assertAlmostEqual(generation2, 960, delta=0.01)  # Assert the calculated average monthly generation is approximately 960 kWh
        self.assertAlmostEqual(percentage2, 20, delta=0.01)  # Assert the calculated surplus percentage is approximately 20%
        self.assertAlmostEqual(generation2 / percentage2, 48, delta=0.01)  # Assert the calculated ratio is approximately 48

    def test_determine_inverter_quantity(self):
        # Test determine_inverter_quantity function with different phases and inverter powers
        inverter_quantity1 = determine_inverter_quantity("Single-phase", 8)  # Test with single-phase and 8 kW inverter power
        self.assertEqual(inverter_quantity1, 1)  # Assert the calculated inverter quantity is 1
        self.assertEqual(inverter_quantity1 * 8, 8)  # Assert the calculated total power is 8 kW
        
        inverter_quantity2 = determine_inverter_quantity("Three-phase", 10)  # Test with three-phase and 10 kW inverter power
        self.assertEqual(inverter_quantity2, 1)  # Assert the calculated inverter quantity is 1
        self.assertEqual(inverter_quantity2 * 10, 10)  # Assert the calculated total power is 10 kW

pytest.main(["-v", "--tb=line", "-rN", __file__])
