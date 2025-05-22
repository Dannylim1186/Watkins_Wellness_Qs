import pytest 
from src.math_checker import math_addition, math_division, math_subtraction, math_multiplication

def test_positive_numbers():
    """Testing adding, dividing, subtracting, and multiple positive numbers """
    assert math_addition(2, 2) == 4
    assert math_addition(21, 15) == 36
    assert math_division(8, 2) == 4
    assert math_division(10, 5) == 2
    assert math_subtraction (10, 3) == 7
    assert math_subtraction (7, 5) == 2
    assert math_multiplication (9, 9) == 81
    assert math_multiplication (10, 10) == 100
