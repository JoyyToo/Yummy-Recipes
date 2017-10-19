"""Category class"""


class Category(object):
    cat = {}
    last_id = None

    def __init__(self):
        """initialization"""
        self.id = None
        self.name = None
        self.description = None
        self.user_id = None

    def create_category(self, name, description, user_id):
        """create category"""
        if name and description and user_id:
            self.name = name
            self.description = description
            self.id = self.assign_id()
            self.user_id = user_id

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
            "message": "Fill all the fields",
            "status": "error"
        }

    def update_category(self, cat_id, name, description, user_id):
        """update category"""
        cat_id = int(cat_id)
        if cat_id in self.cat.keys():
            if name and description and user_id:
                self.cat[cat_id] = {
                    "id": cat_id,
                    "name": name,
                    "desc": description,
                    "user_id": self.user_id
                }
                return {
                    "message": "Category updated successfully",
                    "status": "success",
                    "category": self.cat[cat_id]
                }
            return {
                "message": "Fill all the fields",
                "status": "error"
            }
        return {
            "message": "Category does not exist",
            "status": "error"
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

    def all_categories(self):
        """display all categories"""
        if self.cat:
            return self.cat

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
            "user_id": self.user_id
        }
        return True
