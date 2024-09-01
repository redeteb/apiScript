
from tabulate import tabulate

menu = [
    {"Item": "Breadsticks", "Course": "Appetizers", "Price": 10.0, "GF/V": "GF/V"},
    {"Item": "Queso", "Course": "Appetizers", "Price": 11.0, "GF/V": "V"},
    {"Item": "Calamari", "Course": "Appetizers", "Price": 12.0, "GF/V": "GF"},
    {"Item": "Chicken", "Course": "Entrees", "Price": 16.0, "GF/V": "GF"},
    {"Item": "Beef", "Course": "Entrees", "Price": 17.0, "GF/V": "GF"},
    {"Item": "Shrimp", "Course": "Entrees", "Price": 20.0, "GF/V": "GF"},
    {"Item": "Cake", "Course": "Desserts", "Price": 7.0, "GF/V": "GF/V"},
    {"Item": "Pie", "Course": "Desserts", "Price": 6.0, "GF/V": "GF"},
    {"Item": "Ice Cream", "Course": "Desserts", "Price": 5.0, "GF/V": "GF/V"},
    {"Item": "Tea", "Course": "Beverages", "Price": 2.0, "GF/V": "GF/V"},
    {"Item": "Coke", "Course": "Beverages", "Price": 2.0, "GF/V": "GF/V"},
    {"Item": "Water", "Course": "Beverages", "Price": 1.0, "GF/V": "GF/V"}
]


# Function to display a partial menu
def display_menu(course):
    filtered_menu = [item for item in menu if item["Course"] == course]
    print(tabulate(filtered_menu, headers="keys", tablefmt="fancy_grid"))


# Function to process orders
def valid_order(course, num_items):
    chosen_items = []
    while len(chosen_items) < num_items:
        display_menu(course)
        order = input().strip()
        for item in menu:
            if item["Course"] == course and item["Item"].lower() == order.lower():
                chosen_items.append(item)
                break  
    return chosen_items


# Function to calculate remaining budget
def calculate_budget(budget, items):
    for item in items:
        budget -= item["Price"]
    return budget



dateName = input("Hello, Welcome to our restaurant! What is your date's name tonight?:  ")

initialBudget = float(input(f"Wow, {dateName} is a lovely name. My next question is, what will be your budget for this evening's meal? Ex. 110.00:  "))

#Ask for app and entree 
print(f"Ok, your budget is ${initialBudget:.2f}. Here are the Appetizer options. Pick one (1) that you would like to start with:")
appetizers = valid_order("Appetizers", 1)
remaining_budget = calculate_budget(initialBudget, appetizers)
print(f"Ok. Your budget is now ${remaining_budget:.2f}. Here are the Entree options. Please choose two (2) Ex. Chicken, Chicken:")

#Enter entree and ask for dessert
entrees = valid_order("Entrees", 2)
remaining_budget = calculate_budget(remaining_budget, entrees)
print(f"Ok. Your budget is now ${remaining_budget:.2f}. Here are the Dessert options. Please choose one (1):")

#Enter dessert ask for beverage 
desserts = valid_order("Desserts", 1)
remaining_budget = calculate_budget(remaining_budget, desserts)
print(f"Ok. Your budget is now ${remaining_budget:.2f}. Here are the Beverage options. Please choose two (2). Ex. Coke, Coke:")

#Enter beverage and give final confirmation
beverages = valid_order("Beverages", 2)
remaining_budget = calculate_budget(remaining_budget, beverages)

total_spent = initialBudget - remaining_budget

orderConfirmation = input(f"Great choices for both of you. The final total will be ${total_spent:.2f}. Will this be okay, yes or no?:  ")

if orderConfirmation.lower() == "yes":
    print("Thank you! Your food will be out shortly!")
else:
    print("OK, roll up those sleeves, the dishes are in the back. I'll let the manager know we got another one")