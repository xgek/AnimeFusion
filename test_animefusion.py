# test_animefusion.py
"""
Tests for AnimeFusion module.
"""

import unittest
from animefusion import AnimeFusion

class TestAnimeFusion(unittest.TestCase):
    """Test cases for AnimeFusion class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AnimeFusion()
        self.assertIsInstance(instance, AnimeFusion)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AnimeFusion()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
