import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_init(self):
        """Test initialization with and without ID"""
        s1 = Square(5)
        self.assertEqual(s1.id, 1)  # Default ID should be 1
        s2 = Square(10, 2, 3, 15)
        self.assertEqual(s2.id, 15)  # Custom ID should be set
        self.assertEqual(s2.width, 10)
        self.assertEqual(s2.height, 10)

    def test_size_setter(self):
        """Test setting size with valid and invalid values"""
        s = Square(5)
        s.size = 12
        self.assertEqual(s.width, 12)
        self.assertEqual(s.height, 12)

        with self.assertRaises(TypeError):
            s.size = "hello"
        with self.assertRaises(ValueError):
            s.size = -4

    def test_area(self):
        """Test the area calculation"""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_display(self):
        """Test the display method with various squares"""
        # ... test different square sizes and positions ...

    def test_update(self):
        """Test updating attributes using args and kwargs"""
        # ... test updating with both positional and keyword arguments ...

    def test_to_dictionary(self):
        """Test the dictionary representation"""
        s = Square(5, 2, 3, 15)
        expected_dict = {'id': 15, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_str(self):
        """Test the string representation"""
        s = Square(5, 2, 3, 15)
        expected_str = "[Square] (15) 5/2 - 3"
        self.assertEqual(str(s), expected_str)

if __name__ == "__main__":
    unittest.main()

