import pytest
from solar_budget import *

# Test get_phase function
def test_get_phase():
    assert get_phase() in ["Single-phase", "Biphasic", "Three-phase"]

# Test get_roof_type function
def test_get_roof_type():
    assert get_roof_type() in ["Brasilite", "Aluzinc", "Ceramic", "Ground", "Slab"]

# Test get_orientation function
def test_get_orientation():
    assert get_orientation() in ["North", "Northeast", "Northwest", "East", "West", "South", "Southeast", "Southwest"]

# Test get_module_power function
def test_get_module_power():
    assert get_module_power() in [550, 500, 450, 400, 350, 300]

# Test determine_irradiation function
def test_determine_irradiation():
    assert determine_irradiation("North") == 112
    assert determine_irradiation("South") == 95

# Test calculate_required_power function
def test_calculate_required_power():
    assert calculate_required_power(500, 110) == pytest.approx(4.545, 0.001)
    assert calculate_required_power(600, 100) == pytest.approx(6, 0.001)

# Test determine_module_quantity function
def test_determine_module_quantity():
    assert determine_module_quantity(500, 110, 400) == 13
    assert determine_module_quantity(600, 100, 350) == 21

# Test calculate_total_power function
def test_calculate_total_power():
    assert calculate_required_power(13, 400) == pytest.approx(5.2, 0.001)
    assert calculate_required_power(21, 350) == pytest.approx(7.35, 0.001)

# Test calculate_inverter_power function
def test_calculate_inverter_power():
    assert calculate_inverter_power(5.2) == pytest.approx(6.666, 0.001)
    assert calculate_inverter_power(7.35) == pytest.approx(9.464, 0.001)

# Test determine_inverter_phase function
def test_determine_inverter_phase():
    assert determine_inverter_phase(1.5) == "Single-phase"
    assert determine_inverter_phase(8) == "Three-phase"

# Test determine_inverter_quantity function
def test_determine_inverter_quantity():
    assert determine_inverter_quantity("Single-phase", 1.5) == 1
    assert determine_inverter_quantity("Biphasic", 8) == 2

# Test calculate_distance function
def test_calculate_distance():
    assert calculate_distance("Porto Alegre") == pytest.approx(294.5, 0.1)
    assert calculate_distance("Sao Paulo") == pytest.approx(974.2, 0.1)

# Test calculate_installation function
def test_calculate_installation():
    assert calculate_installation(13, 1, "Porto Alegre") == pytest.approx(5605.2, 0.1)
    assert calculate_installation(21, 2, "Sao Paulo") == pytest.approx(9225.2, 0.1)

# Test calculate_equipment_price function
def test_calculate_equipment_price():
    assert calculate_equipment_price(400, 6.666, "Brasilite") == 12880
    assert calculate_equipment_price(350, 9.464, "Ground") == 11760

# Test calculate_budget function
def test_calculate_budget():
    assert calculate_budget(5605.2, 12880, 13) == pytest.approx(2120.8, 0.1)
    assert calculate_budget(9225.2, 11760, 21) == pytest.approx(861.6, 0.1)

# Test generate_proposal function
def test_generate_proposal():
    assert generate_proposal("John Doe", "Porto Alegre", 500, "Single-phase", "Brasilite", "Mini Rail 24cm", "North", 400) is not None
    assert generate_proposal("Jane Smith", "Sao Paulo", 600, "Three-phase", "Ground", "Block", "South", 350) is not None
