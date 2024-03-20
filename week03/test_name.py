from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    result = extract_family_name('Brown; Sally')
    assert result == 'Brown; Sally'

    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("John", "Doe") == "Doe; John"
    assert make_full_name("Alexander", "Hamilton") == "Hamilton; Alexander"
    assert make_full_name("Elizabeth", "Smith-Jones") == "Smith-Jones; Elizabeth"
    assert make_full_name("Mary-Jane", "Parker") == "Parker; Mary-Jane"
    assert make_full_name("Peter", "Parker") == "Parker; Peter"

def test_extract_family_name():
    result = extract_family_name('Brown; Sally')
    assert result == 'Brown'

def test_extract_given_name():
    result = extract_given_name('Brown; Sally')
    assert result == 'Sally'


pytest.main(["-v", "--tb=line", "-rN", __file__])
 

