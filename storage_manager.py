from datetime import datetime
from storage_manager import StorageManager


class MealLogger:

    def __init__(self):

        self.meals = StorageManager.load_data()

    def add_meal(self, meal_type, food, calories):

        self.meals.append({
            "date": datetime.now().strftime("%Y-%m-%d"),
            "meal_type": meal_type,
            "food": food,
            "calories": calories
        })

        StorageManager.save_data(self.meals)

    def get_meals(self):

        return self.meals

    def get_total_calories(self):

        return sum(
            meal["calories"]
            for meal in self.meals
        )

    def clear_all(self):

        self.meals = []

        StorageManager.save_data(self.meals)