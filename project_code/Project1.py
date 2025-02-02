menu = {
    "Pizza" :250,
    "Burger" :350,
    "Pasta" :170,
    "Taccos" :210,
    "Ramen" :500,
    "Espresso" :300,
}
print("Welcome to PYTHON Restaurant!")
print("Pizza    : 250 tk\nBurger   : 350 tk\nPasta    : 170 tk\nTaccos   : 210 tk\nRamen    : 500 tk\nEspresso : 300 tk")

order_total = 0

item_1 = input("What would you like to order first? ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
else:
    print("Sorry ! The item is not available now.")
another_val = input("Would you like to order anything else ? (Yes/No)")
if another_val == "Yes" :
    item_2 = input("Enter the name of your other order :")
    if item_2 in menu :
        order_total += menu[item_2]
        print(f"Your item {item_2} also added in your order .")
    else:
        print(f"The selected item {item_2} is not available .")
print(f"Thanks for your order!\nThe total amount of items to pay is {order_total}")
   