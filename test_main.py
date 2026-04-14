import unittest
from main import customs_check

class TestCustomsCheck(unittest.TestCase):
    
    def test_wrong_passcode(self):
        # Fails if passcode isn't stroopwafel
        result = customs_check("Viento", "Coffee", "1234")
        self.assertIn("ACCESS DENIED", result)
        
    def test_easter_eggs_tax(self):
        # Ensures the tax is applied
        result = customs_check("Viento", "Easter Eggs", "stroopwafel")
        self.assertIn("CLEARED", result)
        self.assertIn("€15.0", result)
        
    def test_normal_item_case_insensitive(self):
        # Ensures .lower() is being used correctly
        result = customs_check("Viento", "Laptop", "Stroopwafel") 
        self.assertIn("CLEARED", result)
        self.assertIn("Enjoy your Laptop", result)

if __name__ == "__main__":
    unittest.main()
