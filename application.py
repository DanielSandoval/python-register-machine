'''register machine'''
# Aqui escribe tu codigo

import os
import sys

MY_PRODUCTS = {} #This is a dictionary to have all product we have on sale
EXISTENCE_PRODUCT = [] #This a list to have the products we have sold
PRODUCTS_SOLD = [] #We make a list to save the products we want
MY_OPTION = [] #It is a list to save the option gold/siver/done


def clearscreen():
    """Creates a function for clean the screen"""
    os.system('reset')

'''-------------------------OPCION 1-------------------------'''
def option1():
    """The option number 1 of the Main Menu"""
    clearscreen()
    enter_product()
    add = question_add()
    while True:
        if add == "y":
            print ""
            enter_product()
            add = question_add()
        elif add == "n":
            option_n()
            break
        elif add != "y" or add != "n":
            option_different()
            add = question_add()

def enter_product():
    """This function asks a product and a price"""
    product = raw_input("Enter a product: ") #This is the item entered
    product = product.lower()
    while product.isdigit(): #While product is number makes the mext code
        print "PLEASE WRITE TEXT!!!"
        print ""
        product = raw_input("Enter a product: ")
        product = product.lower()

    while True:
        try:
            price = raw_input("Enter a price: ") #Ask the price of the product
            price = float(price)
            break
        except ValueError:
            print "PLEASE WRITE NUMBERS!!!"
            print ""
            print "Producto:", product

    EXISTENCE_PRODUCT.append(product) #Adds the product to a list called "EXISTENCE_PRODUCT"
    MY_PRODUCTS[product] = price
    print "Product added correctly"
    print ""

def question_add():
    """It asks if we want to add another item"""
    add = raw_input("Do you want to add another item?: ")
    add = add.lower()
    return add

def option_n():
    """Starts a function to go to the Main Menu"""
    main_menu()

def option_different():
    """Starst a function if we do not enter y or n"""
    print "PLEASE ENTER \"y\" OR \"n\""

'''-------------------------OPCION 2-------------------------'''

def option2():
    """Makes the process of option 2"""
    clearscreen()
    total = 0
    while True:
        buy = buy_product()
        if buy in MY_PRODUCTS:
            print "  ", buy, ("%.2f" % MY_PRODUCTS[buy])
            total += MY_PRODUCTS[buy]
        elif buy not in MY_PRODUCTS and buy != "done" and buy != "gold" and buy != "silver":
            PRODUCTS_SOLD.remove(buy)
            print "  ", "This is not registered"

        if buy == "gold" or buy == "silver":
            MY_OPTION.append(buy)
            PRODUCTS_SOLD.remove(buy)

        if buy == "done":
            PRODUCTS_SOLD.remove(buy)
            my_total(total)

            if "gold" in MY_OPTION:
                MY_OPTION.remove("gold")
            if "silver" in MY_OPTION:
                MY_OPTION.remove("silver")
            del PRODUCTS_SOLD[:]

            break
    main_menu()

def buy_product():
    """It asks the product that we want to buy"""
    buy = raw_input("Enter the product you want to buy: ")
    buy = buy.lower()
    PRODUCTS_SOLD.append(buy)
    return buy

def my_total(total):
    """It is a function for make the calculates"""
    discount = 0
    subtotal = 0
    tax = total * 0.12
    subtotal = total + tax
    final_total = total + (tax)

    #If we have silver card
    if "silver" in MY_OPTION and "gold" not in MY_OPTION:
        target = False
        #if the user has only gold card
        if "gold" in MY_OPTION:
            target = True
        elif target == False:
            discount = final_total * 0.02
            subtotal = total + tax
            final_total -= discount

    #If we have gold card
    if "gold" in MY_OPTION:
        target = True
        #If the user has gold card and don't have silver card
        if "gold" in MY_OPTION and "silver" not in MY_OPTION:
            discount = final_total * 0.05
            subtotal = total + tax
            final_total -= discount
        #If the user has gold card and silver card
        elif "gold" in MY_OPTION and "silver" in MY_OPTION:
            discount = final_total * 0.05
            subtotal = total + tax
            final_total -= discount

    print_bill(total, tax, discount, subtotal, final_total)

def print_bill(total, tax, discount, subtotal, final_total):
    """Makes the bill"""
    print ""
    num_times()
    print ""
    print "The Total price of the products:", ("%.2f" % total)
    print "The Tax is:", ("%.2f" % tax)
    print "The subtotal is:", ("%.2f" % subtotal)
    print "The discount is:", ("%.2f" % discount)
    print "The Final Total is:", ("%.2f" % final_total)
    print "Thank you for shopping with us"
    enter = raw_input("PRESS ENTER")
    if enter == "":
        clearscreen()
    while enter != "":
        enter = raw_input("PRESS ENTER")
        if enter == "":
            clearscreen()

def num_times():
    """Starts a function for print the quantity of products we asked"""
    print "PRODUCTS PURCHASED"
    for each_product in EXISTENCE_PRODUCT: #This is for to have every item of EXISTENCE_PRODUCT
        num_products_on_sale = PRODUCTS_SOLD.count(each_product)
        if num_products_on_sale >= 1:
            print num_products_on_sale, each_product, "a", ("%.2f" % MY_PRODUCTS[each_product])

'''------------------------MAIN MENU------------------------'''

def main_menu():
    """Prints the Manin Menu"""
    clearscreen()
    while True:
        print "1. Add an item" #Prints this in Main Menu
        print "2. Sell Articles" #Prints this in Main Menu
        print "3. Exit" #Prints this in Main Menu

        option = raw_input("Select the number of the action you want to perform: ")
        try:
            option = int(option)
            if option > 0 and option <= 3:
                if option == 1:
                    option1()
                elif option == 2:
                    option2()
                elif option == 3:
                    clearscreen()
                    sys.exit()
                break
        except ValueError:
            pass
        if option < 1 or option > 3:
            print "INSERT A VALID OPCION"
            print ""
    clearscreen()

main_menu()
