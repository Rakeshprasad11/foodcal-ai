import random

FOOD_DATABASE = [
    "apple", "banana", "pizza", "burger",
    "salad", "rice", "chicken breast",
    "pasta", "sandwich", "cake", "orange", "bread"
]

def analyze_food_image(image_file):
    """
    Mock AI food recognition function.
    Replace this with a real ML model or API later.
    """
    detected_food = random.choice(FOOD_DATABASE)
    confidence = round(random.uniform(0.85, 0.99), 2)

    return {
        "food": detected_food,
        "confidence": confidence
    }
