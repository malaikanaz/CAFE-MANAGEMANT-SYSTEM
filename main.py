menu = {
    "pizza" : 120,
    "icecream" : 70,
    "pasta" : 150,
    "salad" : 90,
    "dessert" : 50,
    "coffee" : 90,
    "fries" : 100
}
print("WELCOME TO NAZ RESTURANT")
print(" Pizza:Rs120\n Icecream:Rs70\n Pasta:Rs150\n Salad:Rs90\n Dessert:Rs50\n Coffee:Rs90\n Fries:Rs100")
order_total = 0

while True:
    item = input("Please enter an item you want to order: ").lower()
    if item in menu:
        order_total += menu[item]
        print(f"Your item '{item}' has been added to your order.")
    else:
        print(f"Sorry, '{item}' is not available in the menu.")

    another_item = input("Do you want to add another item to your order? (yes/no): ").lower()
    if another_item != "yes":
        break

print(f"\nYour total order amount is: Rs{order_total}")
print("Thank you for ordering at Naz Restaurant!")

