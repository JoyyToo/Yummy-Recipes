"""Class Users"""


class Users(object):

    users = {}
    last_id = None

    def __init__(self):
        self.username = None
        self.email = None
        self.password = None
        self.password_again = None
        self.id = None

    def register_user(self, username, email, password, password_again):
        """Register user"""
        if username and email and password and password_again:
            if password == password_again:
                self.username = username
                self.email = email
                self.password = password
                self.password_again = password_again
                self.id = self.assign_id()

                if self.check_if_user_exists():
                    return {
                        "message": "User already exists",
                        "status": "error"
                    }

                if self.save():
                    return {
                        "message": "User created successfully",
                        "status": "success",
                        "user": self.users[self.id]
                    }

            return {
                'message': 'Passwords do not match',
                'status': 'error'
            }

        else:
            return {
                'message': 'Please fill in all fields',
                'status': 'error'
            }

    def login_user(self, email, password):
        """Login User"""
        if email and password:
            if self.check_if_user_exists():
                return {
                    "message": "Login successful",
                    "status": "success",
                    "user": self.users[self.check_if_user_exists()]
                }

            return {
                "message": "Invalid login credentials",
                "status": "error"
            }

        return {
            'message': 'Please fill in all fields',
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
        self.users[self.id] = {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "password_again": self.password_again,
            "email": self.email
        }
        return True

    def check_if_user_exists(self):
        """Checking if user exists"""
        for user in self.users.values():
            if user['email'] == self.email:
                return user['id']
        else:
            return False
