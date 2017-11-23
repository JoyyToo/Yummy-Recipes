"""Test for Recipe class"""

import os
import unittest
from app.models.Recipe import Recipe
from PIL import Image


class TestForClassRecipe(unittest.TestCase):
    """Test for recipe class"""
    def setUp(self):
        """Initializes test for recipe Class"""
        self.recipe = Recipe()
        self.recipe.allrecipes = {}

    # tests for add recipe function
    def test_for_empty_fields(self):
        """Test for empty fields"""
        result = self.recipe.create_recipe('', '', '', '', 0, 0, 'file.png')
        self.assertEqual({"status": "error", "message": {
                'type': '',
                'msg': "Fill all fields"
            }}, result)

    def test_for_empty_name_field(self):
        """Test for empty name field"""
        result = self.recipe.create_recipe('', '1 hour', ' 1 tbsp ', 'stir', 1, 2, 'file.png')
        self.assertEqual({"status": "error", "message": {
                'type': '',
                'msg': "Fill all fields"
            }}, result)

    def test_for_empty_time_field(self):
        """Test for empty time field"""
        result = self.recipe.create_recipe('biryani', '', '1 tbsp', 'stir', 1, 2, 'file.png')
        self.assertEqual({"status": "error", "message": {
                'type': '',
                'msg': "Fill all fields"
            }}, result)

    def test_for_empty_ingredients_field(self):
        """Test for empty ingredients field"""
        result = self.recipe.create_recipe('biryani', '1 hour', '', 'stir', 1, 2, 'file.png')
        self.assertEqual({"status": "error", "message": {
                'type': '',
                'msg': "Fill all fields"
            }}, result)

    def test_for_empty_direction_field(self):
        """Test for empty direction field"""
        result = self.recipe.create_recipe('biryani', '1 hour', '1 tbsp', '', 1, 2, 'file.png')
        self.assertEqual({"status": "error", "message": {
                'type': '',
                'msg': "Fill all fields"
            }}, result)

    # tests for update recipe function
    def test_for_update_non_existing_recipe(self):
        """Test for update missing recipe"""
        image = os.path.dirname(os.path.realpath(__file__)) + "/test.jpg"
        img = Image.open(image)
        self.recipe.update_recipe(1, 'biryani', '1 hour', '1 tbsp', 'stir', 1, 2, img)
        result = self.recipe.update_recipe(0, 'biryani', '1 hour', '1 tbsp', 'stir', 1, 2, img)
        self.assertEqual({"status": "error", "message": {
                'type': 'name_error',
                'msg':  "Recipe does not exist"
            }}, result)

    def test_for_delete_non_existing_recipe(self):
        """Test for delete non existing recipe"""
        self.recipe.delete_recipe(2)
        result = self.recipe.delete_recipe(0)
        self.assertEqual({"status": "error", "message": "Recipe does not exist"}, result)

    def test_for_missing_update_recipe(self):
        """Test for non-existing update recipe"""
        image = os.path.dirname(os.path.realpath(__file__)) + "/test.jpg"
        img = Image.open(image)
        self.recipe.update_recipe(1, 'biryani', '1 hour', '1 tbsp', 'stir', 1, 2, img)
        result = self.recipe.update_recipe(0, 'biryani', '1 hour', '1 tbsp', 'stir', 1, 2, img)
        self.assertEqual({"status": "error", "message": {
                'type': 'name_error',
                'msg':  "Recipe does not exist"}}, result)

    def test_for_view_single_non_existing_recipes(self):
        """Test for non-existing update category"""
        self.recipe.single_recipe(0)
        result = self.recipe.single_recipe(2)
        self.assertEqual({"status": "error", "message": "Recipe does not exist"}, result)

    def test_for_correct_creation_of_recipe(self):
        """Test for correct recipe creation"""
        image = os.path.dirname(os.path.realpath(__file__)) + "/test.jpg"
        img = Image.open(image)
        result = self.recipe.create_recipe('name', 'time', 'ingredients', 'directions', 1, 1, img)
        self.assertEqual("success", result['status'])

    def test_for_creation_of_recipe_with_invalid_characters(self):
        """Test for recipe creation with invalid characters"""
        image = os.path.dirname(os.path.realpath(__file__)) + "/test.jpg"
        img = Image.open(image)
        result = self.recipe.create_recipe(' ', ' ', ' ', ' ', 1, 1, img)
        self.assertEqual({'status': 'error', "message": {'msg': 'Input cannot be empty', 'type': ''}}, result)

    def test_adding_recipe_having_same_name_as_an_existing_recipe(self):
        """Test for adding recipe with existing name"""
        image = os.path.dirname(os.path.realpath(__file__)) + "/test.jpg"
        img = Image.open(image)
        self.recipe.create_recipe('name', 'time', 'ingredients', 'directions', 1, 1, img)
        result = self.recipe.create_recipe('name', 'different time', 'other ingredients', 'other directions', 1, 1, img)
        self.assertEqual({"message": {'msg': 'Recipe already exists', 'type': 'name_error'},
                          "status": "error"}, result)

    def test_deletion_of_recipe(self):
        """Test recipe deletion"""
        image = os.path.dirname(os.path.realpath(__file__)) + "/test.jpg"
        img = Image.open(image)
        self.recipe.create_recipe('name', 'time', 'ingredients', 'directions', 1, 1, img)
        result = self.recipe.delete_recipe(1)
        self.assertEqual({'message': 'Recipe deleted successfully', 'status': 'success'}, result)

    def test_deletion_of_non_existing_recipe(self):
        """Test for delete non existing recipe"""
        self.recipe.delete_recipe(2)
        result = self.recipe.delete_recipe(0)
        self.assertEqual({'message': 'Recipe does not exist', 'status': 'error'}, result)

    def test_get_single_recipe(self):
        """Test for get single recipe"""
        image = os.path.dirname(os.path.realpath(__file__)) + "/test.jpg"
        img = Image.open(image)
        self.recipe.create_recipe('name', 'time', 'ingredients', 'directions', 1, 1, img)
        self.assertEqual("success", self.recipe.single_recipe(1)['status'])

    def test_get_non_existing_single_recipe(self):
        """Test for get non existing single recipe"""
        self.assertEqual({"message": "Recipe does not exist", "status": "error"},
                         self.recipe.single_recipe(1))

    def test_get_all_recipes(self):
        """Test for get all recipes"""
        image = os.path.dirname(os.path.realpath(__file__)) + "/test.jpg"
        img = Image.open(image)
        self.recipe.create_recipe('name', 'time', 'ingredients', 'directions', 1, 1, img)
        self.recipe.create_recipe('name 1', 'time 1', 'ingredients 1', 'directions 1', 1, 1, img)
        result = self.recipe.view_recipes(1, 1)
        self.assertEqual(self.recipe.allrecipes, result)


if __name__ == '__main__':
    unittest.main()
