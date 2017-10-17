"""Test for User class"""

import unittest

from app.models.Users import Users


class TestForUserClass(unittest.TestCase):
    """Test for user class"""
    def setUp(self):
        """Initializes test for user Class"""
        self.usr = Users()

    # tests for register
    def test_for_empty_fields(self):
        """Test for empty fields"""
        result = self.usr.register_user('', '', '', '')
        self.assertEqual({'status': 'error', 'message': 'Please fill in all fields'}, result,)

    def test_for_empty_username_field(self):
        """Test for empty username field"""
        result = self.usr.register_user('', 'user@gmail.com', 'pass', 'pass')
        self.assertEqual({"status": "error", "message": "Please fill in all fields"}, result)

    def test_for_empty_email_field(self):
        """Test for empty email field"""
        result = self.usr.register_user('user', '', 'pass', 'pass')
        self.assertEqual({"status": "error", "message": "Please fill in all fields"}, result)

    def test_for_non_matching_passwords(self):
        """Test for non-matching passwords"""
        result = self.usr.register_user('user', 'user@gmail.com', 'password', 'pass')
        self.assertEqual({"status": "error", "message": "Passwords do not match"}, result)

    def test_for_existing_user(self):
        """Test for existing user"""
        self.usr.register_user('user', 'user@gmail.com', 'pass', 'pass')
        result = self.usr.register_user('user', 'user@gmail.com', 'pass', 'pass')
        self.assertEqual({'status': 'error', 'message': 'User already exists'}, result)

    # tests for login
    def test_for_empty_login_fields(self):
        """Test for empty fields"""
        result = self.usr.login_user('', '')
        self.assertEqual({"status": "error", "message": "Please fill in all fields"}, result, )

    def test_for_empty_loginmail_field(self):
        """Test for empty email field"""
        result = self.usr.login_user('', 'pass')
        self.assertEqual({"status": "error", "message": "Please fill in all fields"}, result)

    def test_for_empty_password_field(self):
        """Test for empty password field"""
        result = self.usr.login_user('user@gmail.com', '')
        self.assertEqual({"status": "error", "message": "Please fill in all fields"}, result)

    def test_for_wrong_password_(self):
        """Test for wrong password"""
        self.usr.login_user('user@gmail.com', 'pass')
        result = self.usr.login_user('user@gmail.com', 'pt')
        self.assertEqual({'status': 'error', 'message': 'Invalid login credentials'}, result)

    # test for update user
    def test_for_update_non_existing_user(self):
        """Test for updating non-existing user"""
        self.usr.update_user(1, 'user', 'user@gmail.com', 'pass', 'pass')
        result = self.usr.update_user('', 'user', 'user@gmail.com', 'pass', 'pass')
        self.assertEqual({'status': 'error', 'message': 'Sorry, could not update user'}, result)

    # test for delete account
    def test_for_delete_non_existing_user(self):
        """Test for deleting non-existing user"""
        self.usr.delete_account(1)
        result = self.usr.delete_account('')
        self.assertEqual({'status': 'error', 'message': 'Sorry, could not delete User'}, result)


if __name__ == '__main__':
    unittest.main()
