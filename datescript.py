
from tabulate import tabulate

menu = [
    {"Item": "Breadsticks", "Course": "Appetizers", "Price": 10.0, "GF/V": "GF/V"},
    {"Item": "Queso", "Course": "Appetizers", "Price": 11.0, "GF/V": "V"},
    {"Item": "Calamari", "Course": "Appetizers", "Price": 12.0, "GF/V": "GF"},
    {"Item": "Chicken", "Course": "Entree", "Price": 16.0, "GF/V": "GF"},
    {"Item": "Beef", "Course": "Entree", "Price": 17.0, "GF/V": "GF"},
    {"Item": "Shrimp", "Course": "Entree", "Price": 20.0, "GF/V": "GF"},
    {"Item": "Cake", "Course": "Dessert", "Price": 7.0, "GF/V": "GF/V"},
    {"Item": "Pie", "Course": "Dessert", "Price": 6.0, "GF/V": "GF"},
    {"Item": "Ice Cream", "Course": "Dessert", "Price": 5.0, "GF/V": "GF/V"},
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



dateName = input("Hello, welcome to our restaurant! What is your date's name tonight?:  ")

initialBudget = float(input(f"Wow, {dateName} is a lovely name. My next question is, what will be your budget for this evening's meal? Ex. 110.00:  "))

#Ask for app and entree 
print(f"Ok, your budget is ${initialBudget:.2f}. Here are the Appetizer options. Pick one (1) that you would like to start with.")
appetizers = valid_order("Appetizers", 1)
remaining_budget = calculate_budget(initialBudget, appetizers)
print(f"Ok. Your budget is now ${remaining_budget:.2f}. Here are the Entree options. Please choose two (2).")

#Enter entree and ask for dessert
entrees = valid_order("Entree", 2)
remaining_budget = calculate_budget(remaining_budget, entrees)
print(f"Ok. Your budget is now ${remaining_budget:.2f}. Here are the Dessert options. Please choose one (1).")

#Enter dessert ask for beverage 
desserts = valid_order("Dessert", 1)
remaining_budget = calculate_budget(remaining_budget, desserts)
print(f"Ok. Your budget is now ${remaining_budget:.2f}. Here are the Beverage options. Please choose two (2).")






















    
#Accept one app as input 
#anything else just reasks the question
#Print "Ok. Your budget is now 123. Here are the entrees, choose two.
#print partial menu 
#OK your budget is now 123. Here are the desserts, choose one.
#print partial menu 
##OK your budget is now 123. Here are the beverages, choose two.


orderConfirmation = input("Great choices for both of you. The final total will be 3.147896325]. Will this be okay, yes or no?"  )

if orderConfirmation.lower() == "yes":
    print("Thank you! Your food will be out shortly!")
else:
    print("OK, roll up those sleeves, the dishes are in the back. I'll let the manager know we got another one")

print(tabulate(menu, headers="keys", tablefmt="fancy_grid"))









# # Function to find item price
# def item_price(order):
#     for item in menu:
#         if item["Item"].lower() == order.lower():
#             return item["Price"]
#     return None


# split menu into 4 courses 
# print(tabulate(menu, headers="keys", tablefmt="fancy_grid"))

# dateOrder = input("What would your date like to order this evening? Enter the items one at a time. ")
# myOrder = input("Excellent choice. And for you?"  )