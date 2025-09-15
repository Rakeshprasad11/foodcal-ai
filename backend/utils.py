FOOD_DATABASE = {
    'apple': {"calories": 52, "protein": 0.3, "carbs": 14, "fat": 0.2},
    'banana': {"calories": 89, "protein": 1.1, "carbs": 23, "fat": 0.3},
    'pizza': {"calories": 266, "protein": 11, "carbs": 33, "fat": 10},
    'burger': {"calories": 295, "protein": 17, "carbs": 24, "fat": 17},
    'salad': {"calories": 20, "protein": 1.8, "carbs": 3.6, "fat": 0.2},
    'rice': {"calories": 130, "protein": 2.7, "carbs": 28, "fat": 0.3},
    'chicken breast': {"calories": 165, "protein": 31, "carbs": 0, "fat": 3.6},
    'pasta': {"calories": 131, "protein": 5, "carbs": 25, "fat": 1.1},
    'sandwich': {"calories": 250, "protein": 12, "carbs": 30, "fat": 8},
    'cake': {"calories": 350, "protein": 4, "carbs": 55, "fat": 12},
    'orange': {"calories": 47, "protein": 0.9, "carbs": 12, "fat": 0.1},
    'bread': {"calories": 265, "protein": 9, "carbs": 49, "fat": 3.2}
}

PORTION_MULTIPLIER = {"small": 0.7, "medium": 1.0, "large": 1.4}

def calculate_calories(food_name, portion="medium"):
    food = FOOD_DATABASE.get(food_name)
    if not food:
        return None

    multiplier = PORTION_MULTIPLIER.get(portion, 1.0)
    return {
        "calories": round(food["calories"] * multiplier),
        "protein": round(food["protein"] * multiplier, 1),
        "carbs": round(food["carbs"] * multiplier, 1),
        "fat": round(food["fat"] * multiplier, 1),
        "portion": portion
    }
