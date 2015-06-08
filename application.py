'''register machine'''
# Aqui escribe tu codigo

import os
import sys

MY_PRODUCTS = {} #This is a dictionary to have all product we have on sale
EXISTENCE_PRODUCT = [] #This a list to have the products we have sold
PRODUCTS_SOLD = [] #We make a list to save the products we want
MY_DISCOUNT = [] #It is a list to save the option gold/siver/done


def clearscreen():
    """Creates a function for clean the screen"""
    os.system('reset')

#-------------------------OPCION 1-------------------------

def option_different():
    """Starst a function if we do not enter y or n"""
    print "PLEASE ENTER \"y\" OR \"n\""

def option_n():
    """Starts a function to go to the Main Menu"""
    main_menu()

def question_add(add = ""):
    """It asks if we want to add another item"""
    if __name__ == '__main__':
        add = raw_input("Do you want to add another item?: ")
    add = add.lower()
    return add

def select_option(product):
    if product.isdigit():
        print "PLEASE WRITE TEXT!!!\n"
        return True
    elif product.isalpha():
        return False
    elif product.isalnum():
        print "PLEASE WRITE TEXT!!!\n"
        return True

def the_product(product = ""):
    if __name__ == '__main__':
        my_input = True
        while my_input == True:
            product = raw_input("Enter a product: ") #This is the item entered
            product = product.lower()
            my_input = select_option(product)
    return product

#def the_price(price = 0):
def the_price(product,price = 0):
    if __name__ == '__main__':
        my_input = True
        while my_input == True:
            try:
                price = raw_input("Enter a price: ") #Ask the price of the product
                price = float(price)
                my_input = False
            except ValueError:
                #print """PLEASE WRITE NUMBERS!!!\n"""
                print """PLEASE WRITE NUMBERS!!!\n\nProducto:""", product
    return price

def enter_product():
    """This function asks a product and a price"""
    product = the_product()
    price = the_price(product)

    EXISTENCE_PRODUCT.append(product) #Adds the product to a list called "EXISTENCE_PRODUCT"
    MY_PRODUCTS[product] = price
    print "Product added correctly"

def option1():
    """The option number 1 of the Main Menu"""
    clearscreen()
    enter_product()
    add = question_add()
    my_input = True #It is only to help to the cycle
    while my_input == True:
        if add == "y":
            print ""
            enter_product()
            add = question_add()
        elif add == "n":
            my_input = False
            option_n()
        elif add != "y" or add != "n":
            option_different()
            add = question_add()

#-------------------------OPCION 2-------------------------

def num_times():
    """Starts a function for print the quantity of products we asked"""
    print "PRODUCTS PURCHASED"
    for each_product in EXISTENCE_PRODUCT: #This is for to have every item of EXISTENCE_PRODUCT
        num_products_on_sale = PRODUCTS_SOLD.count(each_product)
        if num_products_on_sale >= 1:
            print num_products_on_sale, each_product, "a", ("%.2f" % MY_PRODUCTS[each_product])

def print_bill(total, tax, discount, subtotal, final_total):
    """Makes the bill"""
    if __name__ == '__main__':
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
        while enter != "":
            enter = raw_input("PRESS ENTER")
            if enter == "":
                pass

    return final_total

def silver_card(subtotal):
    discount = subtotal * 0.02
    return discount

def gold_card(subtotal):
    discount = subtotal * 0.05
    return discount

def mySubtotal(total,tax):
    subtotal = total + tax
    return subtotal

def myFinalTotal(subtotal,discount):
    final_total = subtotal - discount
    return final_total

def my_total(total,subtotal = 0,discount = 0):
    """It is a function for make the calculates"""
    tax = total * 0.12
    subtotal = mySubtotal(total,tax)
    final_total = 0

    #If we have only silver card
    if "silver" in MY_DISCOUNT and "gold" not in MY_DISCOUNT:
        discount = silver_card(subtotal)
        final_total = myFinalTotal(subtotal,discount)

    #If we have gold card
    elif "gold" in MY_DISCOUNT:
        discount = gold_card(subtotal)
        final_total = myFinalTotal(subtotal,discount)

    else:
        final_total = myFinalTotal(subtotal,discount)

    print_bill(total, tax, discount, subtotal, final_total)

def buy_product(buy = ""):
    """It asks the product that we want to buy"""
    if __name__ == '__main__':
        buy = raw_input("Enter the product you want to buy: ")
    buy = buy.lower()
    PRODUCTS_SOLD.append(buy)
    return buy

def option2():
    """Makes the process of option 2"""
    clearscreen()

    total = 0
    while True:
        buy = buy_product()

        if buy in MY_PRODUCTS:
            #If buy is in MY_PRODUCTS
            print "  ", buy, ("%.2f" % MY_PRODUCTS[buy])
            total += MY_PRODUCTS[buy]
        elif buy not in MY_PRODUCTS and buy != "done" and buy != "gold" and buy != "silver":
            #If buy is not in MY_PRODUCTS
            PRODUCTS_SOLD.remove(buy)
            print "  ", "This is not registered"

        if buy == "gold" or buy == "silver":
            MY_DISCOUNT.append(buy)
            PRODUCTS_SOLD.remove(buy)

        if buy == "done":
            PRODUCTS_SOLD.remove(buy)
            my_total(total)

            del MY_DISCOUNT[:]
            del PRODUCTS_SOLD[:]

            break
    main_menu()

#------------------------MAIN MENU------------------------

def less_or_greater(option):
    message = "VALID OPTION!!!"
    if (option < 1 or option > 3) and type(option) == int:
        message = "INSERT A VALID OPTION!!!"
        if __name__ == "__main__":
            print "\n" + message
            enter = raw_input("PRESS ENTER")
            while enter != "":
                enter = raw_input("PRESS ENTER")
    return message

def my_option(option):
    if option == 1:
        option1()
    elif option == 2:
        option2()
    elif option == 3:
        clearscreen()
        sys.exit()
    else:
        less_or_greater(option)

def myTry(option):
    try:
        word = "NUMBERS"
        option = int(option)
        return option

    except ValueError:
        word = "INSERT ONLY NUMBERS!!!"
        if __name__ == '__main__':
            print "\n" + word
            enter = raw_input("PRESS ENTER")
            while enter != "":
                enter = raw_input("PRESS ENTER")
    return word

def main_menu(option = 0):
    """Prints the Manin Menu"""
    if __name__ == '__main__':

        while True:
            clearscreen()
            print "1. Add an item" #Prints this in Main Menu
            print "2. Sell Articles" #Prints this in Main Menu
            print "3. Exit" #Prints this in Main Menu

            option = raw_input("Select the number of the action you want to perform: ")
            option = myTry(option)
            my_option(option)

    return option

if __name__ == '__main__':
    main_menu()
