"""Test for category class"""

import unittest
from app.models.Category import Category


class TestForClassCategory(unittest.TestCase):
    """Test for category class"""
    def setUp(self):
        """Initializes test for user Class"""
        self.cat = Category()

    def test_for_empty_fields(self):
        """Test for empty fields"""
        result = self.cat.create_category('', '', '', '')
        self.assertEqual({"status": "error", "message": "Fill all the fields"}, result)

    def test_for_empty_name_field(self):
        """Test for empty name field"""
        result = self.cat.create_category('', 'after dinner', 1, 'file.png')
        self.assertEqual({"status": "error", "message": "Fill all the fields"}, result)

    def test_for_empty_description_field(self):
        """Test for empty description field"""
        result = self.cat.create_category('dessert', '', 1, 'file.png')
        self.assertEqual({"status": "error", "message": "Fill all the fields"}, result)

    def test_for_empty_image_url_field(self):
        """Test for empty image url field"""
        result = self.cat.create_category('dessert', 'after dinner', 1, '')
        self.assertEqual({"status": "error", "message": 'No file chosen'}, result)

    def test_for_non_existing_category(self):
        """Test for non-existing category"""
        self.cat.single_category(1)
        result = self.cat.single_category(2)
        self.assertEqual({"status": "error", "message": "Category not available"}, result)

    def test_for_missing_update_category(self):
        """Test for non-existing update category"""
        self.cat.update_category(1, 'Appetizers', 'a desc', 1, 'file.png')
        result = self.cat.update_category(2, 'App', 'available before', 1, 'file.png')
        self.assertEqual({"status": "error", "message": "Category does not exist"}, result)

    def test_for_delete_missing_category(self):
        """Test for non-existing delete category"""
        self.cat.delete_category(2)
        result = self.cat.delete_category(0)
        self.assertEqual({"status": "error", "message": "Sorry, Category does not exist"}, result)

    def test_for_display_single_non_existing_category(self):
        """Test for non-existing display single category"""
        self.cat.single_category(0)
        result = self.cat.single_category(2)
        self.assertEqual({"status": "error", "message": "Category not available"}, result)


if __name__ == '__main__':
    unittest.main()

