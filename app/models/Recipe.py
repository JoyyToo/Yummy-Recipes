"""Recipe class"""
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


class Recipe(object):
    rec = {}
    last_id = None

    def __init__(self):
        self.id = None
        self.name = None
        self.time = None
        self.ingredients = None
        self.direction = False
        self.category_id = None
        self.user_id = None
        self.image_url = None

    def create_recipe(self, name, time, ingredients, direction, category_id, user_id, image_url):
        """create recipe"""
        if name and time and ingredients and direction and category_id and user_id:
            self.name = name
            self.time = time
            self.ingredients = ingredients
            self.direction = direction
            self.category_id = category_id
            self.user_id = user_id
            self.id = self.assign_id()
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
                    "message": "Recipe already exists",
                    "status": "error"
                }
            if self.save():
                return {
                    "message": "Recipe added successfully",
                    "status": "success",
                    "recipe": self.rec[self.id]
                }
            return {
                "message": "Recipe exists",
                "status": "error"
            }
        return {
            "message": "Fill all fields",
            "status": "error"
        }

    def update_recipe(self, recipe_id, name, time, ingredients, direction, category_id, user_id, image_url):
        """update recipe"""
        recipe_id = int(recipe_id)
        if int(recipe_id) in self.rec.keys():
            if recipe_id and name and time and ingredients and direction and category_id and user_id:

                image = self.rec[recipe_id]["image_url"] if not image_url else image_url.filename
                if image_url and not self.allowed_file(image_url.filename):
                        return {
                            "message": "File chosen is not allowed",
                            "status": "error",
                            "recipe": self.rec[recipe_id]
                        }
                if self.validate_update(name, user_id, recipe_id):
                    return {
                        "message": "Recipe already exists",
                        "status": "error",
                        "recipe": self.rec[recipe_id]
                    }
                self.rec[recipe_id] = {
                    "id": recipe_id,
                    "name": name,
                    "time": time,
                    "ingredients": ingredients,
                    "direction": direction,
                    "category_id": category_id,
                    "user_id": user_id,
                    "image_url": image
                }
                return {
                    "message": "Recipe updated successfully",
                    "status": "success",
                    "recipe": self.rec[recipe_id]
                }

            return {
                "message": "Fill all fields",
                "status": "error",
                "recipe": self.rec[recipe_id]
            }
        return {
            "message": "Recipe does not exist",
            "status": "error",
        }

    def delete_recipe(self, recipe_id):
        """delete recipe"""
        recipe_id = int(recipe_id)
        if recipe_id in self.rec.keys():
            del self.rec[recipe_id]
            return {
                "message": "Recipe deleted successfully",
                "status": "success"
            }
        return {
            "message": "Recipe does not exist",
            "status": "error"
        }

    def single_recipe(self, recipe_id):
        """view single recipe"""
        recipe_id = int(recipe_id)
        if recipe_id in self.rec.keys():
            return {
                "status": "success",
                "recipe": self.rec[recipe_id]
            }
        return {
            "message": "Recipe does not exist",
            "status": "error"
        }

    def all_recipe(self):
        """view all recipe"""
        if len(self.rec):
            return {
                "status": "success",
                "recipe": self.rec
            }
        return {
            "message": "Sorry, Recipe not available at the moment",
            "status": "error"
        }

    def view_recipes(self, user_id):
        """view all recipes"""
        recipes = {}
        if self.rec:
            for recipe in self.rec:
                if self.rec[recipe]['user_id'] == user_id:
                    recipes[recipe] = {
                        "id": self.rec[recipe]['id'],
                        "name": self.rec[recipe]['name'],
                        "time": self.rec[recipe]['time'],
                        "ingredients": self.rec[recipe]['ingredients'],
                        "direction": self.rec[recipe]['direction'],
                        "category_id": self.rec[recipe]['category_id'],
                        "user_id": self.rec[recipe]['user_id'],
                        "image_url": self.rec[recipe]['image_url'],
                    }
            return recipes
        return self.rec

    def save(self):
        """save data"""
        self.rec[self.id] = {
            "id": self.id,
            "name": self.name,
            "time": self.time,
            "ingredients": self.ingredients,
            "direction": self.direction,
            "category_id": self.category_id,
            "user_id": self.user_id,
            "image_url": self.image_url.filename
        }
        return True

    def assign_id(self):
        """assign id"""

        if len(self.rec) == 0:
            _id = 1
            self.last_id = _id
        else:
            self.last_id = int(self.last_id) + 1
            _id = self.last_id
        return _id

    def allowed_file(self, file):
        return '.' in file and \
               file.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def check_if_name_exists(self, name, user_id):
        """Checking if recipe exists"""

        for recipe in self.rec.values():
            if recipe['name'] == name and recipe['user_id'] == user_id:
                    return True
        else:
            return False

    def validate_update(self, name, user_id, rec_id):
        recipes = []
        name = name.strip()
        for recipe in self.rec.values():
            if recipe['name'] == name and recipe['user_id'] == user_id:
                recipes.append(recipe)
        if len(recipes) == 1:
            return False if self.rec[rec_id]['name'] == name else True
        if len(recipes) > 1:
            return True
        return False