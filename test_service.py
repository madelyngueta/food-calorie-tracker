from services.calorie_service import CalorieCalculator
from services.meal_logger import MealLogger


def test_calorie_calculation():

    assert CalorieCalculator.calculate("rice") == 200


def test_unknown_food():

    assert CalorieCalculator.calculate("unknownfood") == 150


def test_add_meal():

    logger = MealLogger()

    initial = len(logger.get_meals())

    logger.add_meal(
        "Lunch",
        "Burger",
        350
    )

    assert len(logger.get_meals()) == initial + 1


def test_total_calories():

    logger = MealLogger()

    logger.clear_all()

    logger.add_meal(
        "Breakfast",
        "Rice",
        200
    )

    logger.add_meal(
        "Lunch",
        "Burger",
        350
    )

    assert logger.get_total_calories() == 550


def test_clear_meals():

    logger = MealLogger()

    logger.clear_all()

    assert logger.get_meals() == []