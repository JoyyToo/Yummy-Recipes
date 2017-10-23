"""Recipe class"""


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

    def create_recipe(self, name, time, ingredients, direction, category_id, user_id):
        """create recipe"""
        if name and time and ingredients and direction and category_id and user_id:
            self.name = name
            self.time = time
            self.ingredients = ingredients
            self.direction = direction
            self.category_id = category_id
            self.user_id = user_id
            self.id = self.assign_id()

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

    def update_recipe(self, recipe_id, name, time, ingredients, direction, category_id, user_id):
        """update recipe"""
        recipe_id = int(recipe_id)
        if recipe_id and name and time and ingredients and direction and category_id and user_id:

            if recipe_id in self.rec.keys():
                self.rec[recipe_id] = {
                    "id": recipe_id,
                    "name": name,
                    "time": time,
                    "ingredients": ingredients,
                    "direction": direction,
                    "category_id": category_id,
                    "user_id": user_id
                }
                return {
                    "message": "Recipe updated successfully",
                    "status": "success",
                    "recipe": self.rec[recipe_id]
                }
            return {
                "message": "Recipe does not exist",
                "status": "error"
            }
        return {
            "message": "Fill all fields",
            "status": "error"
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

    def view_recipes(self):
        """view all recipes"""
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
            "user_id": self.user_id
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
