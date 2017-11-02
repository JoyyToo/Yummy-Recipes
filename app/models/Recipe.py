"""Recipe class"""
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


class Recipe(object):
    """class recipe"""
    allrecipes = {}
    last_id = None

    def __init__(self):
        self._id = None
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
            if name.strip() and time.strip() and ingredients.strip() and direction.strip():
                self.name = name
                self.time = time
                self.ingredients = ingredients
                self.direction = direction
                self.category_id = category_id
                self.user_id = user_id
                self._id = self.assign_id()
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
                if self.check_if_name_exists(name, user_id, category_id):
                    return {
                        "message": "Recipe already exists",
                        "status": "error"
                    }
                if self.save():
                    return {
                        "message": "Recipe added successfully",
                        "status": "success",
                        "recipe": self.allrecipes[self._id]
                    }
            return {
                "message": "Input cannot be empty",
                "status": "error"
            }
        return {
            "message": "Fill all fields",
            "status": "error"
        }

    def update_recipe(self, recipe_id, name, time, ingredients,
                      direction, category_id, user_id, image_url):
        """update recipe"""
        recipe_id = int(recipe_id)
        if int(recipe_id) in self.allrecipes.keys():
            if recipe_id and name and time and ingredients \
                    and direction and category_id and user_id:
                if name.strip() and time.strip() and ingredients.strip()\
                        and direction.strip():

                    image = self.allrecipes[recipe_id]["image_url"] \
                        if not image_url else image_url.filename
                    if image_url and not self.allowed_file(image_url.filename):
                                return {
                                    "message": "File chosen is not allowed",
                                    "status": "error",
                                    "recipe": self.allrecipes[recipe_id]
                                }
                    if self.validate_update(name, user_id, recipe_id, category_id):
                        return {
                            "message": "Recipe already exists",
                            "status": "error",
                            "recipe": self.allrecipes[recipe_id]
                        }
                    self.allrecipes[recipe_id] = {
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
                        "recipe": self.allrecipes[recipe_id]
                    }
                return {
                    "message": "Input cannot be empty",
                    "status": "error"
                }

            return {
                "message": "Fill all fields",
                "status": "error",
                "recipe": self.allrecipes[recipe_id]
            }
        return {
            "message": "Recipe does not exist",
            "status": "error",
        }

    def delete_recipe(self, recipe_id):
        """delete recipe"""
        recipe_id = int(recipe_id)
        if recipe_id in self.allrecipes.keys():
            del self.allrecipes[recipe_id]
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
        if recipe_id in self.allrecipes.keys():
            return {
                "status": "success",
                "recipe": self.allrecipes[recipe_id]
            }
        return {
            "message": "Recipe does not exist",
            "status": "error"
        }

    def view_recipes(self, user_id, category_id):
        """view all recipes"""
        recipes = {}
        if self.allrecipes:

            for recipe in self.allrecipes:
                if self.allrecipes[recipe]['user_id'] == user_id \
                        and self.allrecipes[recipe]['category_id'] == category_id:
                    recipes[recipe] = {
                        "id": self.allrecipes[recipe]['id'],
                        "name": self.allrecipes[recipe]['name'],
                        "time": self.allrecipes[recipe]['time'],
                        "ingredients": self.allrecipes[recipe]['ingredients'],
                        "direction": self.allrecipes[recipe]['direction'],
                        "category_id": self.allrecipes[recipe]['category_id'],
                        "user_id": self.allrecipes[recipe]['user_id'],
                        "image_url": self.allrecipes[recipe]['image_url'],
                    }
            return recipes
        return self.allrecipes

    def save(self):
        """save data"""
        self.allrecipes[self._id] = {
            "id": self._id,
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

        if len(self.allrecipes) == 0:
            _id = 1
            self.last_id = _id
        else:
            self.last_id = int(self.last_id) + 1
            _id = self.last_id
        return _id

    def allowed_file(self, file):
        """defining allowed files"""
        return '.' in file and \
               file.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    def check_if_name_exists(self, name, user_id, category_id):
        """Checking if recipe exists"""
        for recipe in self.allrecipes.values():
            if recipe['name'] == name and recipe['user_id'] == user_id \
                    and recipe['category_id'] == category_id:
                return True
        else:
            return False

    def validate_update(self, name, user_id, recipe_id, category_id):
        """validate update function"""
        recipes = []
        name = name.strip()
        for recipe in self.allrecipes.values():
            if recipe['name'] == name and recipe['user_id'] == user_id \
                    and recipe['category_id'] == category_id:
                recipes.append(recipe)
        if len(recipes) == 1:
            return False if self.allrecipes[recipe_id]['name'] == name else True
        if len(recipes) > 1:
            return True
        return False
