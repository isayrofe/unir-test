import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_substract_returns_correct_result(self):
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(4, self.calc.substract(6, 2))
        self.assertEqual(-4, self.calc.substract(2, 6))
        self.assertEqual(0, self.calc.substract(0, 0))
        
    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")
        self.assertRaises(TypeError, self.calc.divide, "5", "0")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))
        self.assertEqual(0, self.calc.multiply(0, 0))
    
    def test_power_method_returns_correct_result(self):
        self.assertEqual(16, self.calc.power(2, 4))
        self.assertEqual(1, self.calc.power(1, 0))
        self.assertEqual(1, self.calc.power(0, 0))
        self.assertEqual(1, self.calc.power(1, 1))
    
    def test_power_method_fails_with_negative_exponent(self):
        self.assertRaises(TypeError, self.calc.power, 2, -1)
        self.assertRaises(TypeError, self.calc.power, 2, -1.5)
        self.assertRaises(TypeError, self.calc.power, 2, -1.5)
    
    def test_power_method_fails_with_zero_exponent(self):
        self.assertRaises(TypeError, self.calc.power, 0, -1.0)
        self.assertRaises(TypeError, self.calc.power, 0, -0.5)
    
    def test_square_root_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.square_root(4))
        self.assertEqual(0, self.calc.square_root(0))
        self.assertEqual(0, self.calc.square_root(-0))
        self.assertEqual(1.4142135623730951, self.calc.square_root(2))

    def test_square_root_method_fails_with_negative_number(self):
        self.assertRaises(TypeError, self.calc.square_root, -1)
        self.assertRaises(TypeError, self.calc.square_root, -1.5)
        

    def test_logarithm_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.logarithm(1))
    
    def test_logarithm_method_fails_with_negative_number(self):
        self.assertRaises(TypeError, self.calc.logarithm, -1)
        self.assertRaises(TypeError, self.calc.logarithm, -1.5)
    
    def test_check_types_correct_param(self):
        self.assertEqual(None, self.calc.check_types(1, 2))
        self.assertEqual(None, self.calc.check_types(1.0, 2.0))

    
if __name__ == "__main__":  # pragma: no cover
    unittest.main()
