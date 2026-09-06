# test_veilapex.py
"""
Tests for VeilApex module.
"""

import unittest
from veilapex import VeilApex

class TestVeilApex(unittest.TestCase):
    """Test cases for VeilApex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VeilApex()
        self.assertIsInstance(instance, VeilApex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VeilApex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
