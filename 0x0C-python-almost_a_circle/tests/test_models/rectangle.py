import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_init(self):
        """Test initialization with and without ID"""
        r1 = Rectangle(5, 4)
        self.assertEqual(r1.id, 1)  # Default ID should be 1
        r2 = Rectangle(10, 8, 2, 3, 15)
        self.assertEqual(r2.id, 15)  # Custom ID should be set

    # ... tests for other methods and functionalities ...

    def test_width_setter(self):
        """Test setting width with valid and invalid values"""
        r = Rectangle(5, 4)
        r.width = 10
        self.assertEqual(r.width, 10)

        with self.assertRaises(TypeError):
            r.width = "hello"
        with self.assertRaises(ValueError):
            r.width = -5

    def test_height_setter(self):
        """Test setting height with valid and invalid values"""
        # ... similar to width_setter test ...

    def test_x_setter(self):
        """Test setting x with valid and invalid values"""
        # ... similar to width_setter test ...

    def test_y_setter(self):
        """Test setting y with valid and invalid values"""
        # ... similar to width_setter test ...

    def test_area(self):
        """Test the area calculation"""
        r = Rectangle(5, 4)
        self.assertEqual(r.area(), 20)

    def test_display(self):
        """Test the display method with various rectangles"""
        # ... test different rectangle sizes and positions ...

    def test_update(self):
        """Test updating attributes using args and kwargs"""
        # ... test updating with both positional and keyword arguments ...

    def test_to_dictionary(self):
        """Test the dictionary representation"""
        r = Rectangle(5, 4, 2, 3, 15)
        expected_dict = {'id': 15, 'x': 2, 'y': 3, 'width': 5, 'height': 4}
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_str(self):
        """Test the string representation"""
        r = Rectangle(5, 4, 2, 3, 15)
        expected_str = "[Rectangle] (15) 2/3 - 5/4"
        self.assertEqual(str(r), expected_str)

if __name__ == "__main__":
    unittest.main()

