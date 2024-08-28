# Nested Restaurant Menu Dictionary
# Course = Appetizers, Entree, Dessert, Beverages
# Subcategories: Price, Ingredients, Dietary Restrictions (GF = Gluten Free V = Vegan)
# Appetizers = Breadsticks, Queso, Calamari
# Entree = Chicken, Beef, Shrimp
# Dessert = Cake, Pie, Ice Cream
# Beverages = Tea, Coke, Water 






menu = {
    "Appetizers": {
        "Breadsticks": {"Price": 10.0, "Ingredients": ["Bread", "Cheese", "Garlic"], "Dietary Restrictions": "GF/V"},
        "Queso": {"Price": 11.0, "Ingredients": ["Cheddar", "Swiss", "Pepper Jack"], "Dietary Restrictions": "V"}, 
        "Calamari": {"Price": 12.0, "Ingredients": ["Squid", "Panko", "Marinara"], "Dietary Restrictions": "GF"}
    },
    "Entree": {
        "Chicken": {"Price": 16.0, "Ingredients": ["Chicken", "Mushrooms", "Pasta"], "Dietary Restrictions": "GF"},
        "Beef": {"Price": 17.0, "Ingredients": ["Beef", "Onions"], "Dietary Restrictions": "GF"},
        "Shrimp": {"Price": 20.0, "Ingredients": ["Squid", "Panko", "Marinara"], "Dietary Restrictions": "GF"},
    },
    "Dessert":{
        "Cake": {"Price": 7.0, "Ingredients": ["Chocolate", "Sugar", "Milk"], "Dietary Restrictions": "GF/V"},
        "Pie": {"Price": 6.0, "Ingredients": ["Cherries", "Bluesberries", "Rasberries"], "Dietary Restrictions": "GF"},
        "Ice Cream": {"Price": 5.0, "Ingredients": ["Vanilla", "Chocolate", "Strawberry"], "Dietary Restrictions": "GF/V"},
        },
    "Beverages": {
        "Tea": {"Price": 2.0, "Ingredients": ["Black", "Green", "Peach"], "Dietary Retrictions": "GF/V"}, 
        "Coke": {"Price": 2.0, "Ingredients": ["Cup", "Ice", "Coke"], "Dietary Retrictions": "GF/V"},
        "Water": {"Price": 1.0, "Ingredients": ["Cup", "Ice", "Water"], "Dietary Retrictions": "GF/V"},
}
