"""Category class"""
import re

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
INVALID_CHAR = re.compile(r"[<>/{}[\]~`*!@#$%^&()=+]")


class Category(object):
    """class category"""
    category = {}
    last_id = None

    def __init__(self):
        """initialization"""
        self._id = None
        self.name = None
        self.description = None
        self.user_id = None
        self.image_url = None

    def create_category(self, name, description, user_id, image_url):
        """create category"""
        if name and description and user_id:
            if name.strip() and description.strip():
                if self.validate_input(name=name, description=description):
                    return {
                        "message": {
                            'type': '',
                            'msg': "{} contains invalid characters".format
                            (self.validate_input(name=name, description=description))
                        },
                        "status": "error"
                    }
                self.name = name
                self.description = description
                self._id = self.assign_id()
                self.user_id = user_id
                self.image_url = image_url

                image = None if not image_url else image_url.filename
                if image_url and not self.allowed_file(image_url.filename):
                    return {
                        "message": {
                            'type': 'image_error',
                            'msg': "File chosen is not allowed. Use jpg, png or jpeg."
                        },
                        "status": "error"
                    }
                if self.check_if_name_exists(name, user_id):
                    return {
                        "message": {
                            'type': 'name_error',
                            'msg': "Category already exists"
                        },
                        "status": "error"
                    }
                self.category[self._id] = {
                    "id": self._id,
                    "name": self.name,
                    "desc": self.description,
                    "user_id": self.user_id,
                    "image_url": image
                }
                return {
                    "message": "Category created successfully",
                    "status": "success",
                    "category": self.category[self._id]
                }
            return {
                "message": {
                    'type': '',
                    'msg': "Input cannot be empty"
                },
                "status": "error"
            }

        return {
            "message": {
                'type': '',
                'msg': "Fill all the fields"
            },
            "status": "error"
        }

    def update_category(self, category_id, name, description, user_id, image_url):
        """update category"""
        category_id = int(category_id)
        if category_id in self.category.keys():
            if name and description and user_id:
                if name.strip() and description.strip():
                    if self.validate_input(name=name, description=description):
                        return {
                            "message": {
                                'type': '',
                                'msg': "{} contains invalid characters".format
                                (self.validate_input(name=name, description=description))
                            },
                            "status": "error",
                            "category": self.category[category_id]
                        }
                    image = self.category[category_id]["image_url"] if not image_url \
                        else image_url.filename
                    if image_url and not self.allowed_file(image_url.filename):
                        return {
                            "message": {
                                'type': 'image_error',
                                'msg': "File chosen is not allowed. Use jpg, png or jpeg."
                            },
                            "status": "error",
                            "category": self.category[category_id]
                        }
                    if self.validate_update(name, user_id, category_id):
                        return {
                            "message": {
                             'type': 'name_error',
                             'msg': "Category already exists"
                            },
                            "status": "error",
                            "category": self.category[category_id]
                        }
                    self.category[category_id] = {
                        "id": category_id,
                        "name": name,
                        "desc": description,
                        "user_id": self.user_id,
                        "image_url": image
                    }
                    return {
                        "message": "Category updated successfully",
                        "status": "success",
                        "category": self.category[category_id]
                    }
                return {
                    "message": {
                     'type': '',
                     'msg': "Input cannot be empty"
                    },
                    "status": "error",
                    "category": self.category[category_id]

                }
            return {
                "message": {
                    'type': '',
                    'msg': "Fill all the fields"
                },
                "status": "error",
                "category": self.category[category_id]
            }
        return {
            "message": {
                'type': 'name_error',
                'msg': "Category does not exist"
            },
            "status": "error",
        }

    def delete_category(self, category_id):
        """delete category"""
        if int(category_id) in self.category.keys():
            del self.category[int(category_id)]
            return {
                "message": "Category deleted successfully",
                "status": "success"
            }
        return {
            "message": "Sorry, Category does not exist",
            "status": "error"
        }

    def all_categories(self, user_id):
        """display all categories"""
        categories = {}
        if self.category:
            for category in self.category:
                if self.category[category]['user_id'] == user_id:
                    categories[category] = {
                        "id": self.category[category]['id'],
                        "name": self.category[category]['name'],
                        "desc": self.category[category]['desc'],
                        "user_id": self.category[category]['user_id'],
                        "image_url": self.category[category]['image_url'],
                    }
            return categories

    def single_category(self, category_id):
        """display single category"""
        if int(category_id) in self.category.keys():
            return {
                "status": "success",
                "category": self.category[int(category_id)]
            }
        return {
            "message": "Category not available",
            "status": "error"
        }

    def assign_id(self):
        """assign id"""
        if len(self.category) == 0:
            _id = 1
            self.last_id = _id
        else:
            self.last_id = int(self.last_id) + 1
            _id = self.last_id
        return _id

    def check_if_exists(self, _id):
        """Check if user exists"""
        return True if int(_id) in self.category.keys() else False

    def allowed_file(self, file):
        """check if file is allowed"""
        return '.' in file and \
               file.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def check_if_name_exists(self, name, user_id):
        """Checking if category exists"""

        for category in self.category.values():
            if category['name'] == name and category['user_id'] == user_id:
                return True
        else:
            return False

    def validate_update(self, name, user_id, category_id):
        """validate update"""
        categories = []
        name = name.strip()
        for category in self.category.values():
            if category['name'] == name and category['user_id'] == user_id:
                categories.append(category)
        if len(categories) == 1:
            return False if self.category[category_id]['name'] == name else True
        if len(categories) > 1:
            return True
        return False

    def validate_input(self, **kwargs):
        if kwargs:
            for key in kwargs:
                if INVALID_CHAR.search(kwargs[key]):
                    return key
