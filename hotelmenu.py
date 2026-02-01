# HOTEL-MENU
# define the menu of resturant
menu={
    'pizza':40,
    'pasta':90,
    'tea':30,
    'coffee':45,
    'burger':90,
    'dosa':130

}
# greet
print("Welcome to the Resturant")
print("pizza:Rs40\npasta:Rs90\ntea:Rs30\ncoffee:Rs45\nburger:Rs90\ndosa:Rs130")
order_total= 0
# 50+45=95
item_1=input("Enter the name of the item you want to order=")
if item_1 in menu:
    order_total+=menu[item_1] 
    print(f"your item{item_1} has been added to your order")
    

else:
    print(f"orderd item{item_1} is not available yet please choose another item in our list")

another_order=("do you want to another item ?(yes/no)")
if another_order =="yes":
    item_2=input("enter the name of second item =")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"item{item_2}has been added to order")
    else:
        print(f"orderd item{item_2} is not available!")

print(f"the total amount of item to pay is {order_total}")
