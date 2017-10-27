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
        result = self.cat.create_category('', '', '')
        self.assertEqual({"status": "error", "message": "Fill all the fields"}, result)

    def test_for_empty_name_field(self):
        """Test for empty name field"""
        result = self.cat.create_category('', 'after dinner', 1)
        self.assertEqual({"status": "error", "message": "Fill all the fields"}, result)

    def test_for_empty_description_field(self):
        """Test for empty description field"""
        result = self.cat.create_category('dessert', '', 1)
        self.assertEqual({"status": "error", "message": "Fill all the fields"}, result)

    def test_for_non_existing_category(self):
        """Test for non-existing category"""
        self.cat.single_category(1)
        result = self.cat.single_category(2)
        self.assertEqual({"status": "error", "message": "Category not available"}, result)

    def test_for_missing_update_category(self):
        """Test for non-existing update category"""
        self.cat.update_category(1, 'Appetizers', 'a desc', 1)
        result = self.cat.update_category(2, 'App', 'available before', 1)
        self.assertEqual({"status": "error", "message": "Category does not exist"}, result)

    def test_for_delete_missing_category(self):
        """Test for non-existing delete category"""
        self.cat.delete_category(2)
        result = self.cat.delete_category(0)
        self.assertEqual({"status": "error", "message": "Sorry, Category does not exist"}, result)
