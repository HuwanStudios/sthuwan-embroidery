import unittest
from sthuwan_embroidery.machines import validate_bounds

class TestSE600(unittest.TestCase):
    def test_valid_design(self):
        self.assertTrue(validate_bounds(31.8, 31.8))

    def test_oversize_design_rejected(self):
        with self.assertRaises(ValueError):
            validate_bounds(101.0, 31.8)

if __name__ == "__main__":
    unittest.main()
