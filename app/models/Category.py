"""Category class"""
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


class Category(object):
    """class category"""
    cat = {}
    last_id = None

    def __init__(self):
        """initialization"""
        self.id = None
        self.name = None
        self.description = None
        self.user_id = None
        self.image_url = None

    def create_category(self, name, description, user_id, image_url):
        """create category"""
        if name and description and user_id:
            if name.strip() and description.strip():
                self.name = name
                self.description = description
                self.id = self.assign_id()
                self.user_id = user_id
                self.image_url = image_url
                if not image_url:
                    return {
                        "message": "No file chosen",
                        "status": "error"
                    }
                if not self.allowed_file(image_url.filename):
                    return {
                        "message": "File chosen is not allowed",
                        "status": "error"
                    }
                if self.check_if_name_exists(name, user_id):
                    return {
                        "message": "Category already exists",
                        "status": "error"
                    }
                if self.save():
                    return {
                        "message": "Category created successfully",
                        "status": "success",
                        "category": self.cat[self.id]
                    }
                return {
                    "message": "Category exists",
                    "status": "error"
                }
            return {
                "message": "Invalid character input",
                "status": "error"
            }

        return {
            "message": "Fill all the fields",
            "status": "error"
        }

    def update_category(self, cat_id, name, description, user_id, image_url):
        """update category"""
        cat_id = int(cat_id)
        if cat_id in self.cat.keys():
            if name and description and user_id:
                if name.strip() and description.strip():
                    image = self.cat[cat_id]["image_url"] if not image_url else image_url.filename
                    if image_url and not self.allowed_file(image_url.filename):
                            return {
                                "message": "File chosen is not allowed",
                                "status": "error",
                                "category": self.cat[cat_id]
                            }
                    if self.validate_update(name, user_id, cat_id):
                        return {
                            "message": "Category already exists",
                            "status": "error",
                            "category": self.cat[cat_id]
                        }
                    self.cat[cat_id] = {
                        "id": cat_id,
                        "name": name,
                        "desc": description,
                        "user_id": self.user_id,
                        "image_url": image
                    }
                    return {
                        "message": "Category updated successfully",
                        "status": "success",
                        "category": self.cat[cat_id]
                    }
                return {
                    "message": "Invalid character input",
                    "status": "error",
                    "category": self.cat[cat_id]

                }
            return {
                "message": "Fill all the fields",
                "status": "error",
                "category": self.cat[cat_id]
            }
        return {
            "message": "Category does not exist",
            "status": "error",
        }

    def delete_category(self, cat_id):
        """delete category"""
        if int(cat_id) in self.cat.keys():
            del self.cat[int(cat_id)]
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
        if self.cat:
            for category in self.cat:
                if self.cat[category]['user_id'] == user_id:
                    categories[category] = {
                        "id": self.cat[category]['id'],
                        "name": self.cat[category]['name'],
                        "desc": self.cat[category]['desc'],
                        "user_id": self.cat[category]['user_id'],
                        "image_url": self.cat[category]['image_url'],
                    }
            return categories

    def single_category(self, cat_id):
        """display single category"""
        if int(cat_id) in self.cat.keys():
            return {
                "status": "success",
                "category": self.cat[int(cat_id)]
            }
        return {
            "message": "Category not available",
            "status": "error"
        }

    def assign_id(self):
        """assign id"""
        if len(self.cat) == 0:
            _id = 1
            self.last_id = _id
        else:
            self.last_id = int(self.last_id) + 1
            _id = self.last_id
        return _id

    def save(self):
        """save data"""
        self.cat[self.id] = {
            "id": self.id,
            "name": self.name,
            "desc": self.description,
            "user_id": self.user_id,
            "image_url": self.image_url.filename
        }
        return True

    def check_if_exists(self, id):
        """Check if user exists"""
        return True if int(id) in self.cat.keys() else False

    def allowed_file(self, file):
        """check if file is allowed"""
        return '.' in file and \
               file.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def check_if_name_exists(self, name, user_id):
        """Checking if category exists"""

        for category in self.cat.values():
            if category['name'] == name and category['user_id'] == user_id:
                    return True
        else:
            return False

    def validate_update(self, name, user_id, cat_id):
        """validate update"""
        categories = []
        name = name.strip()
        for category in self.cat.values():
            if category['name'] == name and category['user_id'] == user_id:
                categories.append(category)
        if len(categories) == 1:
            return False if self.cat[cat_id]['name'] == name else True
        if len(categories) > 1:
            return True
        return False
