
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
def valid_order(course):
    while True:
        display_menu(course)
        order = input("Choice: ")
        for item in menu:
            if item["Course"] == course and item["Item"].lower() == order.lower():
                return item
        print(f"'{order}' is not a valid option. Please try again.")

# Function to calculate remaining budget
def calculate_budget(budget, items):
    for item in items:
        if budget - item["Price"] < 0:
            print("Sorry, it seems you have run out of money. You must change your order.")
            return None 
        budget -= item["Price"]
    return budget



while True:
    try:
        dateName = input("Hello, Welcome to our restaurant! What is your date's name tonight?:  ")
        initialBudget = float(input(f"Wow, {dateName} is a lovely name. What will be your budget for this evening's meal? Ex. 100 or 80.85: "))
        break  
    except ValueError:
        print("Invalid input. Please enter a valid amount.")

    remaining_budget = initialBudget

while True:
    #Choose app
    print(f"Ok, your budget is ${initialBudget:.2f}. Here are the Appetizer options. Pick one (1): ")
    appetizers = [valid_order("Appetizers")]
    remaining_budget = calculate_budget(initialBudget, appetizers)
    if remaining_budget is None:
        continue 
    
    print(f"Ok. Your budget is now ${remaining_budget:.2f}. Here are the Entree options. Please select your first choice: ")

    #Choose Entree 1
    first_entree = [valid_order("Entrees")]
    remaining_budget = calculate_budget(remaining_budget, first_entree)
    if remaining_budget is None:
        continue  
    
    print(f"Ok. Your budget is now ${remaining_budget:.2f}. Choose your second Entree: ")

    #Choose Entree 2
    second_entree = [valid_order("Entrees")]
    remaining_budget = calculate_budget(remaining_budget, second_entree)
    if remaining_budget is None:
        continue  

    print(f"Ok. Your budget is now ${remaining_budget:.2f}. Choose one (1) Dessert: ")

    #Choose Dessert
    desserts = [valid_order("Desserts")]
    remaining_budget = calculate_budget(remaining_budget, desserts)
    if remaining_budget is None:
        continue  

    print(f"Ok. Your budget is now ${remaining_budget:.2f}. Here are the Beverage options. Please select your first choice: ")

    #Choose Beverage 1
    first_beverage = [valid_order("Beverages")]
    remaining_budget = calculate_budget(remaining_budget, first_beverage)
    if remaining_budget is None:
        continue  
    
    print(f"Ok. Your budget is now ${remaining_budget:.2f}. Choose your second Beverage: ")

    #Choose Bevrage 2
    second_beverage = [valid_order("Beverages")]
    remaining_budget = calculate_budget(remaining_budget, second_beverage)
    if remaining_budget is not None:
        break

total_spent = initialBudget - remaining_budget

if remaining_budget is not None:
    total_spent = initialBudget - remaining_budget
else:
    total_spent = initialBudget  

orderConfirmation = input(f"Great choices for the both of you. The final total will be ${total_spent:.2f}. Will this be okay, yes or no?:  ")

if orderConfirmation.lower() == "yes":
    print("Thank you! Your food will be out shortly!")
else:
    print("OK, roll up those sleeves, the dishes are in the back. I'll let the manager know we've got another one.")