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
        self.assertEqual({'status': 'error', 'message': {
                    'type': '',
                    'msg': 'Please fill in all fields'
                }}, result,)

    def test_for_empty_username_field(self):
        """Test for empty username field"""
        result = self.usr.register_user('', 'user@gmail.com', 'pass', 'pass')
        self.assertEqual({"status": "error", 'message': {
                    'type': '',
                    'msg': 'Please fill in all fields'
                }}, result)

    def test_for_invalid_name_characters(self):
        """Test for invalid characters in name"""
        result = self.usr.register_user('user%&#', 'user@gmail.com', 'password', 'password')
        self.assertEqual({"status": "error", "message": {
                            "type": "username_error",
                            "msg": "Username contains invalid characters"
                        }}, result)

    def test_for_invalid_email_address(self):
        """Test for invalid email address"""
        result = self.usr.register_user('user', 'user@gmail.com.com', 'password', 'password')
        self.assertEqual({"status": "error",  "message": {
                            'type': 'email_error',
                            'msg': "Invalid Email address"
                        }}, result)

    def test_for_empty_email_field(self):
        """Test for empty email field"""
        result = self.usr.register_user('user', '', 'pass', 'pass')
        self.assertEqual({"status": "error", 'message': {
                    'type': '',
                    'msg': 'Please fill in all fields'
                }}, result)

    def test_for_non_matching_passwords(self):
        """Test for non-matching passwords"""
        result = self.usr.register_user('user', 'user@gmail.com', 'password', 'pass')
        self.assertEqual({"status": "error",
                          'message': {'type': 'password_error', 'msg': 'Passwords do not match'}}, result)

    def test_for_reg_password_less_than_6_characters(self):
        """Test for reg password less than 6 characters"""
        self.usr.register_user('user', 'user@gmail.com', 'pass', 'pass')
        result = self.usr.login_user('user@gmail.com', 'mypas')
        self.assertEqual({"status": "error", "message": {
                                'type': "password_error",
                                'msg': "Password must be more than 6 characters"
                            }}, result)

    def test_for_existing_user(self):
        """Test for existing user"""
        self.usr.register_user('user', 'user@gmail.com', 'password', 'password')
        result = self.usr.register_user('user', 'user@gmail.com', 'password', 'password')
        self.assertEqual({"message": {
                                'type': '',
                                'msg': "User already exists. Please login"
                            }, 'status': 'error'}, result)

    # tests for login
    def test_for_empty_login_fields(self):
        """Test for empty fields"""
        result = self.usr.login_user('', '')
        self.assertEqual({"status": "error", 'message': {
                    'type': '',
                    'msg': 'Please fill in all fields'
                }}, result, )

    def test_for_empty_login_mail_field(self):
        """Test for empty email field"""
        result = self.usr.login_user('', 'pass')
        self.assertEqual({"status": "error", 'message': {
                    'type': '',
                    'msg': 'Please fill in all fields'
                }}, result)

    def test_for_empty_password_field(self):
        """Test for empty password field"""
        result = self.usr.login_user('user@gmail.com', '')
        self.assertEqual({"status": "error", 'message': {
                    'type': '',
                    'msg': 'Please fill in all fields'
                }}, result)

    def test_for_password_less_than_6_field(self):
        """Test for password les than 6 characters"""
        self.usr.login_user('user@gmail.com', 'pass')
        result = self.usr.login_user('user@gmail.com', 'mypas')
        self.assertEqual({"status": "error", "message": {
                                'type': "password_error",
                                'msg': "Password must be more than 6 characters"
                            }}, result)

    def test_for_wrong_password_(self):
        """Test for wrong password"""
        self.usr.login_user('user@gmail.com', 'password')
        result = self.usr.login_user('user@gmail.com', 'mypassword')
        self.assertEqual({'status': 'error', "message": {
                    'type': '',
                    'msg': "Invalid password or email address"
                }}, result)

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
