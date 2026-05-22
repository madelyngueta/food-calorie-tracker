class CalorieCalculator:

    food_db = {
        "rice": 200,
        "fried rice": 320,
        "burger": 350,
        "pizza": 285,
        "apple": 95,
        "banana": 105,
        "egg": 78,
        "chicken": 250,
        "fried chicken": 320,
        "spaghetti": 250,
        "bread": 80,
        "milk": 120,
        "coffee": 50,
        "fries": 365,
        "hotdog": 150,
        "fish": 220,
        "salad": 100,
        "juice": 110,
        "ice cream": 210,
        "noodles": 300
    }

    @staticmethod
    def calculate(food):

        return CalorieCalculator.food_db.get(
            food.lower(),
            150
        )