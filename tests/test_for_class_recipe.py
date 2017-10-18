"""Test for Recipe class"""

import unittest
from app.models.Recipe import Recipe


class TestForClassRecipe(unittest.TestCase):
    """Test for recipe class"""
    def setUp(self):
        """Initializes test for recipe Class"""
        self.rec = Recipe()

    # tests for add recipe function
    def test_for_empty_fields(self):
        """Test for empty fields"""
        result = self.rec.create_recipe('', '', '', '', 0, 0)
        self.assertEqual({"status": "error", "message": 'Fill all fields'}, result)

    def test_for_empty_name_field(self):
        """Test for empty name field"""
        result = self.rec.create_recipe('', '1 hour', ' 1 tbsp ', 'stir', 1, 2)
        self.assertEqual({"status": "error", "message": 'Fill all fields'}, result)

    def test_for_empty_time_field(self):
        """Test for empty time field"""
        result = self.rec.create_recipe('biryani', '', '1 tbsp', 'stir', 1, 2)
        self.assertEqual({"status": "error", "message": 'Fill all fields'}, result)

    def test_for_empty_ingredients_field(self):
        """Test for empty ingredients field"""
        result = self.rec.create_recipe('biryani', '1 hour', '', 'stir', 1, 2)
        self.assertEqual({"status": "error", "message": 'Fill all fields'}, result)

    def test_for_empty_direction_field(self):
        """Test for empty direction field"""
        result = self.rec.create_recipe('biryani', '1 hour', '1 tbsp', '', 1, 2)
        self.assertEqual({"status": "error", "message": 'Fill all fields'}, result)

    def test_for_recipe_in_category(self):
        """Test for recipe in category"""
        self.rec.create_recipe('biryani', '1 hour', '1 tbsp', 'stir', 1, 2)
        result = self.rec.create_recipe('biryani', '1 hour', '1 tbsp', 'stir', 1, 2)
        self.assertEqual({"status": "error", "message": "Recipe exists"}, result)

    # tests for update recipe function
    def test_for_empty_update_fields(self):
        """Test for empty update field"""
        result = self.rec.update_recipe(0, '', '', '', '', 0, 0)
        self.assertEqual({"status": "error", "message": 'Fill all fields'}, result)

    def test_for_empty_update_name_field(self):
        """Test for empty update name field"""
        result = self.rec.update_recipe(0, '', '1 hour', '1 tbsp', 'stir', 1, 2)
        self.assertEqual({"status": "error", "message": 'Fill all fields'}, result)

    def test_for_empty_update_time_fields(self):
        """Test for empty update time field"""
        result = self.rec.update_recipe(0, 'biryani', '', '1 tbsp', 'stir', 1, 2)
        self.assertEqual({"status": "error", "message": 'Fill all fields'}, result)

    def test_for_empty_update_ingredients_field(self):
        """Test for empty update ingredients field"""
        result = self.rec.update_recipe(0, 'biryani', '1 hour', '', 'stir', 1, 2)
        self.assertEqual({"status": "error", "message": 'Fill all fields'}, result)

    def test_for_empty_update_direction_field(self):
        """Test for empty update direction field"""
        result = self.rec.update_recipe(0, 'biryani', '1 hour', '1 tbsp', '', 1, 2)
        self.assertEqual({"status": "error", "message": 'Fill all fields'}, result)

    def test_for_update_a_missing_recipe(self):
        """Test for update missing recipe"""
        self.rec.update_recipe(0, 'biryani', '1 hour', '1 tbsp', 'stir', 1, 2)
        result = self.rec.update_recipe(1, 'biryani', '1 hour', '1 tbsp', 'stir', 1, 2)
        self.assertEqual({"status": "error", "message": "Recipe does not exist"}, result)


if __name__ == '__main__':
    unittest.main()