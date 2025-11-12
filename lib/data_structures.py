spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def format_spicy_food(food):
    name = food["name"]
    cuisine = food["cuisine"]
    heat_level = food["heat_level"]
    chili_string = '🌶' * heat_level
    return f"{name} ({cuisine}) | Heat Level: {chili_string}"

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(format_spicy_food(food))

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    spiciest = get_spiciest_foods(spicy_foods)
    for food in spiciest:
        print(format_spicy_food(food))

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    new_list = list(spicy_foods)
    new_list.append(spicy_food)
    return new_list
