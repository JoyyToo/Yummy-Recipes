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
        result = self.rec.create_recipe('', '', '', '', 0, 0, 'file.png')
        self.assertEqual({"status": "error", "message": 'Fill all fields'}, result)

    def test_for_empty_name_field(self):
        """Test for empty name field"""
        result = self.rec.create_recipe('', '1 hour', ' 1 tbsp ', 'stir', 1, 2, 'file.png')
        self.assertEqual({"status": "error", "message": 'Fill all fields'}, result)

    def test_for_empty_time_field(self):
        """Test for empty time field"""
        result = self.rec.create_recipe('biryani', '', '1 tbsp', 'stir', 1, 2, 'file.png')
        self.assertEqual({"status": "error", "message": 'Fill all fields'}, result)

    def test_for_empty_ingredients_field(self):
        """Test for empty ingredients field"""
        result = self.rec.create_recipe('biryani', '1 hour', '', 'stir', 1, 2, 'file.png')
        self.assertEqual({"status": "error", "message": 'Fill all fields'}, result)

    def test_for_empty_direction_field(self):
        """Test for empty direction field"""
        result = self.rec.create_recipe('biryani', '1 hour', '1 tbsp', '', 1, 2, 'file.png')
        self.assertEqual({"status": "error", "message": 'Fill all fields'}, result)

    def test_for_empty_image_url_field(self):
        """Test for empty image url field"""
        result = self.rec.create_recipe('biryani', '1 hour', ' 1 tbsp ', 'stir', 1, 2, '')
        self.assertEqual({"status": "error", "message": 'No file chosen'}, result)

    # tests for update recipe function
    def test_for_update_missing_recipe(self):
        """Test for update missing recipe"""
        self.rec.update_recipe(0, 'biryani', '1 hour', '1 tbsp', 'stir', 1, 2, 'file.png')
        result = self.rec.update_recipe(1, 'biryani', '1 hour', '1 tbsp', 'stir', 1, 2, 'file.png')
        self.assertEqual({"status": "error", "message": "Recipe does not exist"}, result)

    def test_for_delete_non_existing_recipe(self):
        """Test for delete non existing recipe"""
        self.rec.delete_recipe(2)
        result = self.rec.delete_recipe(0)
        self.assertEqual({"status": "error", "message": "Recipe does not exist"}, result)

    def test_for_missing_update_recipe(self):
        """Test for non-existing update recipe"""
        self.rec.update_recipe(1, 'biryani', '1 hour', '1 tbsp', 'stir', 1, 2, 'file.png')
        result = self.rec.update_recipe(0, 'biryani', '1 hour', '1 tbsp', 'stir', 1, 2, 'file.png')
        self.assertEqual({"status": "error", "message": "Recipe does not exist"}, result)

    def test_for_view_non_existing_recipes(self):
        """Test for non-existing update category"""
        self.rec.all_recipe()
        result = self.rec.all_recipe()
        self.assertEqual({"status": "error", "message": "Sorry, Recipe not available at the moment"}, result)

    def test_for_view_single_non_existing_recipes(self):
        """Test for non-existing update category"""
        self.rec.single_recipe(0)
        result = self.rec.single_recipe(2)
        self.assertEqual({"status": "error", "message": "Recipe does not exist"}, result)


if __name__ == '__main__':
    unittest.main()
