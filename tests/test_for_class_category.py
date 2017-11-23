"""Test for category class"""
import os
import unittest
from app.models.Category import Category
from PIL import Image


class TestForClassCategory(unittest.TestCase):
    """Test for category class"""

    def setUp(self):
        """Initializes test for user Class"""
        self.category = Category()
        self.category.category = {}

    def test_for_add_category_with_invalid_characters(self):
        """Tests for successfull creation of a category"""
        image = os.path.dirname(os.path.realpath(__file__)) + "/test.jpg"
        img = Image.open(image)
        response = self.category.create_category(' ', ' ', ' ', img)
        self.assertEqual({ "message": {
                    'type': '',
                    'msg': "Input cannot be empty"
                }, 'status': 'error'}, response)

    def test_for_adding_existing_category(self):
        image = os.path.dirname(os.path.realpath(__file__)) + "/test.jpg"
        img = Image.open(image)
        self.category.create_category('name', 'desc', 'user_id', img)
        response = self.category.create_category('name', 'desc', 'user_id', img)
        self.assertEqual({"message": {
                            'type': 'name_error',
                            'msg': "Category already exists"
                        }, 'status': 'error'}, response)

    def test_update_category_without_image(self):
        image = os.path.dirname(os.path.realpath(__file__)) + "/test.jpg"
        img = Image.open(image)
        self.category.create_category('name', 'desc', 'user_id', img)
        response = self.category.update_category(1, 'new name', 'new desc', 'user_id', '')
        self.assertEqual('Category updated successfully', response['message'])

    def test_update_category_with_image(self):
        image = os.path.dirname(os.path.realpath(__file__)) + "/test.jpg"
        img = Image.open(image)
        self.category.create_category('name', 'desc', 'user_id', img)
        response = self.category.update_category(1, 'new name', 'new desc', 'user_id', img)
        self.assertEqual('Category updated successfully', response['message'])

    def test_update_existing_category(self):
        image = os.path.dirname(os.path.realpath(__file__)) + "/test.jpg"
        img = Image.open(image)
        self.category.create_category('name', 'desc', 'user_id', img)
        self.category.create_category('name 1', 'desc 1', 'user_id 1', img)
        response = self.category.update_category(2, 'name', 'desc', 'user_id', img)
        self.assertEqual({'msg': 'Category already exists', 'type': 'name_error'},
                         response['message'])

    def test_update_category_with_invalid_input(self):
        image = os.path.dirname(os.path.realpath(__file__)) + "/test.jpg"
        img = Image.open(image)
        self.category.create_category('name', 'desc', 'user_id', img)
        response = self.category.update_category(1, ' ', ' ', ' ', img)
        self.assertEqual({'msg': 'Input cannot be empty', 'type': ''}, response['message'])

    def test_delete_category(self):
        image = os.path.dirname(os.path.realpath(__file__)) + "/test.jpg"
        img = Image.open(image)
        self.category.create_category('name', 'desc', 'user_id', img)
        self.category.update_category(1, 'new name', 'new desc', 'user_id', img)
        response = self.category.delete_category(1)
        self.assertEqual({"message": "Category deleted successfully", "status": "success"}, response)

    def test_delete_non_existing_category(self):
        response = self.category.delete_category(1)
        self.assertEqual({"message": "Sorry, Category does not exist", "status": "error"}, response)

    def test_get_all_categories(self):
        image = os.path.dirname(os.path.realpath(__file__)) + "/test.jpg"
        img = Image.open(image)
        self.category.create_category('name', 'desc', 'user_id', img)
        self.category.create_category('new name', 'new desc', 'user_id', img)
        response = self.category.all_categories('user_id')
        self.assertEqual(self.category.category, response)

    def test_get_single_category(self):
        image = os.path.dirname(os.path.realpath(__file__)) + "/test.jpg"
        img = Image.open(image)
        self.category.create_category('name', 'desc', 'user_id', img)
        response = self.category.single_category(1)
        self.assertEqual("success", response['status'])

    def test_get_single_non_existing_category(self):
        response = self.category.single_category(1)
        self.assertEqual({"message": "Category not available", "status": "error"}, response)

    def test_corrent_assign_id(self):
        res = self.category.assign_id()
        self.assertEqual(1, res)

    def test_check_if_category_exists(self):
        image = os.path.dirname(os.path.realpath(__file__)) + "/test.jpg"
        img = Image.open(image)
        self.category.create_category('name', 'desc', 'user_id', img)
        self.assertTrue(self.category.check_if_exists(1))

    def test_for_empty_fields(self):
        """Test for empty fields"""
        result = self.category.create_category('', '', '', '')
        self.assertEqual({"status": "error", "message": {
                'type': '',
                'msg': "Fill all the fields"
            }}, result)

    def test_for_empty_name_field(self):
        """Test for empty name field"""
        result = self.category.create_category('', 'after dinner', 1, 'file.png')
        self.assertEqual({"status": "error", "message": {
                'type': '',
                'msg': "Fill all the fields"
            }}, result)

    def test_for_empty_description_field(self):
        """Test for empty description field"""
        result = self.category.create_category('dessert', '', 1, 'file.png')
        self.assertEqual({"status": "error", "message": {
                'type': '',
                'msg': "Fill all the fields"
            }}, result)

    def test_for_non_existing_category(self):
        """Test for non-existing category"""
        self.category.single_category(1)
        result = self.category.single_category(2)
        self.assertEqual({"status": "error", 'message': 'Category not available', 'status': 'error'}, result)

    def test_for_missing_update_category(self):
        """Test for non-existing update category"""
        self.category.update_category(1, 'Appetizers', 'a desc', 1, 'file.png')
        result = self.category.update_category(2, 'App', 'available before', 1, 'file.png')
        self.assertEqual({"status": "error", "message": {
                'type': 'name_error',
                'msg': "Category does not exist"
            }}, result)

    def test_for_delete_missing_category(self):
        """Test for non-existing delete category"""
        self.category.delete_category(2)
        result = self.category.delete_category(0)
        self.assertEqual({"status": "error", "message": "Sorry, Category does not exist"}, result)

    def test_for_display_single_non_existing_category(self):
        """Test for non-existing display single category"""
        self.category.single_category(0)
        result = self.category.single_category(2)
        self.assertEqual({"status": "error", "message": "Category not available"}, result)


if __name__ == '__main__':
    unittest.main()
