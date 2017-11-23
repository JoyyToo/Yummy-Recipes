"""Class Users"""
import re
INVALID_CHAR = re.compile(r"[<>/{}[\]~`*!@#$%^&()=+]")


class Users(object):
    """Users class"""
    users = {}
    last_id = None

    def __init__(self):
        """Initialization"""
        self.username = None
        self.email = None
        self.password = None
        self.password_again = None
        self._id = None

    def register_user(self, username, email, password, password_again):
        """Register user"""
        if username and email and password and password_again:

            if username.strip() and email.strip() and password.strip() and password_again.strip():

                if INVALID_CHAR.search(username):
                    return {
                        "message": {
                            "type": "username_error",
                            "msg": "Username contains invalid characters"
                        },
                        "status": "error"
                    }

                if not self.valid_email(email):
                    return {
                        "message": {
                            'type': 'email_error',
                            'msg': "Invalid Email address"
                        },
                        "status": "error"
                    }

                if password == password_again:
                    if len(password) < 6:
                        return {
                            "message": {
                                'type': "password_error",
                                'msg': "Password must be more than 6 characters"
                            },
                            "status": "error"
                        }
                    self.username = username
                    self.email = email
                    self.password = password
                    self.password_again = password_again
                    self._id = self.assign_id()

                    if self.check_if_user_exists(email):
                        return {
                            "message": {
                                'type': '',
                                'msg': "User already exists. Please login"
                            },
                            "status": "error"
                        }

                    if self.save():
                        return {
                            "message": "You have registered successfully. Please login",
                            "status": "success",
                            "user": self.users[self._id]
                        }

                return {
                    'message': {
                        'type': 'password_error',
                        'msg': 'Passwords do not match'
                    },
                    'status': 'error'
                }
            return {
                "message": {
                    'type': '',
                    'msg': "Input cannot be empty"
                },
                "status": "error"
            }

        else:
            return {
                'message': {
                    'type': '',
                    'msg': 'Please fill in all fields'
                },
                'status': 'error'
            }

    def login_user(self, email, password):
        """Login User"""
        if email and password:

            if not self.valid_email(email):
                return {
                    "message": {
                        'type': 'email_error',
                        'msg': "Invalid Email address"
                    },
                    "status": "error"
                }

            if len(password) < 6:
                return {
                    "message": {
                                'type': "password_error",
                                'msg': "Password must be more than 6 characters"
                            },
                    "status": "error"
                }
            if self.check_if_user_exists(email):
                if self.users[self.check_if_user_exists(email)]['password'] == password:
                    return {
                        "message": "You logged in successfully",
                        "status": "success",
                        "user": self.users[self.check_if_user_exists(email)]
                    }
            return {
                "message": {
                    'type': '',
                    'msg': "Invalid password or email address"
                },
                "status": "error"
            }
        return {
            'message': {
                'type': '',
                'msg': 'Please fill in all fields'
            },
            'status': 'error'
        }

    def update_user(self, user_id, username, email, password, password_again):
        """Update user"""
        if self.update(user_id, username, email, password, password_again):
            return {
                "message": "User updated successfully",
                "status": "success",
                "user": self.users[user_id]
            }
        return {
            "message": "Sorry, could not update user",
            "status": "error"
        }

    def delete_account(self, user_id):
        """Delete user account"""
        if user_id in self.users.keys():
            del self.users[user_id]
            return {
                "message": "User deleted successfully",
                "status": "success"
            }
        return {
            "message": "Sorry, could not delete User",
            "status": "error"
        }

    def assign_id(self):
        """Assign id"""
        if len(self.users) == 0:
            _id = 1
            self.last_id = _id
        else:
            self.last_id = int(self.last_id) + 1
            _id = self.last_id
        return _id

    def update(self, user_id, username, email, password, password_again):
        """Update data"""
        if user_id and username and email and password and password_again:
            if user_id in self.users.keys():
                self.users[user_id] = {
                    "id": user_id,
                    "username": username,
                    "email": email,
                    "password": password,
                    "password_again": password_again
                }
                return True

    def save(self):
        """save date"""
        self.users[self._id] = {
            "id": self._id,
            "username": self.username,
            "password": self.password,
            "password_again": self.password_again,
            "email": self.email
        }
        return True

    def check_if_user_exists(self, email):
        """Checking if user exists"""
        for user in self.users.values():
            if user['email'] == email:
                return user['id']
        else:
            return False

    def valid_email(self, email):
        return bool(re.search(r"^[\wg\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email))

