
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

dateName = input("Hello, welcome back to our restaurant. What is your date's name tonight?  ")

initialBudget = float(input(f"Wow, {dateName} is a lovely name. Next question is, what will be your budget for tonight's meal? Ex. 15.0  "))

print(f"Ok, your budget is ${initialBudget}. Here is our menu.") 


from tabulate import tabulate
print(tabulate(menu, headers="keys", tablefmt="fancy_grid"))



dateOrder = input("What would your date like this evening?"  )
#Create order input with counter of budget going down 



myOrder = input("Excellent choice. And for you?"  )
#Order input again with counter 


orderConfirmation = input("Great choices for both of you. The final total will be 1.0. Will this be okay, yes or no?"  )

if orderConfirmation.lower() == "yes":
    print("Thank you! Your food will be out shortly!")
else:
    print("OK, roll up those sleeves, the dishes are in the back. I'll let the manager know we got another one")
