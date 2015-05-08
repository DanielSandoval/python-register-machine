'''register machine'''
# Aqui escribe tu codigo

import os

def clearscreen():
    """Creates a function for clean the screen"""
    os.system('reset')

def option1():
    """The option number 1 of the Main Menu"""
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

    LIST_PRODUCT.append(product) #Adds the product to a list called "LIST_PRODUCT"
    MY_PRODUCTS[product] = price #
    print ""

def option_y(add):
    """Creates a function for if we want to add another item"""
    while add == "y":
        option1()
        #Ask if we want to add another item
        add = raw_input("Do you want to add another item? Write y or n: ")
        add = add.lower()
        if add == "y":
            print ""
        LIST_PRODUCT.append(add) #If we enter y, adds it to a list

        if "y" in LIST_PRODUCT or "n" in LIST_PRODUCT:
            LIST_PRODUCT.remove(add) #If we enter y or n removes it
        if add == "n":
            option_n() #If we enter n call the option n
        elif add == "y":
            pass
        while add != "y" and add != "n":
            print "INSERT Y OR N!!!"
            add = raw_input("Do you want to add another item? Write y or n: ")
            add = add.lower()
            if add == "y":
                print ""
            if add == "n":
                option_n() #If our option is n call option_n
                break

def option_n():
    """Starts a function to go to the Main Menu"""
    main_menu()

def option_different():
    """Starst a function if we do not enter y or n"""
    print "PLEASE ENTER \"y\" OR \"n\""

def option_add(add):
    """Starst a function to take a decision if we want to enter another item"""
    if add == "y": #If we enter y calls the function option_y
        option_y(add)
    elif add == "n": #If we enter n calls the function option_y
        option_n()
    #If we enter something different of y or n calls the function option_y
    elif add != "y" or add != "n":
        option_different()

def num_times(my_buy, list_product):
    """Starts a function for print the quantity of products we asked"""
    print "PRODUCTS PURCHASED"
    for each_product in list_product: #This is for to have every item of LIST_PRODUCT
        num_times_products_on_sale = my_buy.count(each_product)
        if num_times_products_on_sale >= 1:
            print num_times_products_on_sale, each_product, "a", ("%.2f" % MY_PRODUCTS[each_product])

def print_bill(my_buy, list_product, total, tax, subtotal, discount, final_total):
    """Makes the bill"""
    print ""
    num_times(my_buy, list_product)
    print ""
    print "The Total price of the products:", ("%.2f" % total)
    print "The Tax is:", ("%.2f" % tax)
    print "The subtotal is:", ("%.2f" % subtotal)
    print "The discount is:", ("%.2f" % discount)
    print "The Total Final is:", ("%.2f" % final_total)
    print "Thank you for shopping with us"
    enter = raw_input("PRESS ENTER")
    if enter == "":
        clearscreen()
        main_menu()
    while enter != "":
        enter = raw_input("PRESS ENTER")
        if enter == "":
            clearscreen()
            main_menu()

def my_total(buy, my_option, my_buy, my_products, total):
    """It is a function for make the calculates"""
    while buy != "done":
        if buy in my_products:
            total += my_products[buy]
        #Ask we enter a product we want to buy
        buy = raw_input("Do you want to buy another product?: ")
        buy = buy.lower()
        my_buy.append(buy) #Adds the item we entered to the list my_buy

        if buy == "gold" or buy == "silver" or buy == "done":
            my_option.append(buy)
            if buy == "gold":
                my_buy.remove(buy)
            elif buy == "silver":
                my_buy.remove(buy)

        if buy != "done" and buy in my_products:
            print "  ", buy, ("%.2f" % my_products[buy])

        if "done" in my_option:
            discount = 0
            subtotal = 0
            tax = total * 0.12
            final_total = total + (tax)

            #If we have silver card
            if "silver" in my_option and "gold" not in my_option:
                my_buy.remove(buy)
                target = False
                #if the user has only gold card
                if "gold" in my_option:
                    target = True
                elif target == False:
                    discount = final_total * 0.02
                    subtotal = total + tax
                    final_total -= discount

            #If we have gold card
            elif "gold" in my_option:
                my_buy.remove(buy)
                target = True
                #If the user has gold card and don't have silver card
                if "gold" in my_option and "silver" not in my_option:
                    discount = final_total * 0.05
                    subtotal = total + tax
                    final_total -= discount
                #If the user has gold card and silver card
                elif "gold" in my_option and "silver" in my_option:
                    discount = final_total * 0.05
                    subtotal = total + tax
                    final_total -= discount

            print_bill(my_buy, LIST_PRODUCT, total, tax, subtotal, discount, final_total)

        elif buy not in my_products and buy != "done" and buy != "gold" and buy != "silver":
            print "  ", "This is not registered"

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
                break
        except ValueError:
            pass
        if option < 1 or option > 3:
            print "Insert a valid option"
            print ""
    clearscreen()

    if option == 1:
        option1()
        add_condition = True
        while add_condition == True:
            add = raw_input("Do you want to add another item? Write y or n: ")
            add = add.lower()
            if add == "y": #If add is equals to y breaks the cycle
                break
            elif add == "n": #If add is equals to n breaks the cycle
                break
            else: #Else print the next code
                print "INSERT Y OR N!!!"
        print ""
        LIST_PRODUCT.append(add) #Add add to LIST_PRODUCT
        if "y" in LIST_PRODUCT or "n" in LIST_PRODUCT:
            LIST_PRODUCT.remove(add)
        option_add(add)

    elif option == 2:
        my_buy = [] #We make a list to save the products we want
        my_option = [] #It is a list to save the option gold/siver/done
        buy = raw_input("Which product you want to buy?: ")
        buy = buy.lower()
        my_buy.append(buy)
        if buy in MY_PRODUCTS:
            print "  ", buy, ("%.2f" % MY_PRODUCTS[buy])
        elif buy not in MY_PRODUCTS and buy != "done" and buy != "gold" and buy != "silver":
            print "  ", "This is not registered"
        while buy == "done" or buy == "gold" or buy == "silver":
            print "First adds a product"
            #Ask an item to buy
            buy = raw_input("Which product you want to buy?: ")
            buy = buy.lower()
            if buy in MY_PRODUCTS:
                print "  ", ("my_option%.2f" % buy, MY_PRODUCTS[buy])
                my_buy.append(buy)
        total = 0

        my_total(buy, my_option, my_buy, MY_PRODUCTS, total)

    elif option == 3: #If the input is equals to 3 makes the next code
        pass

MY_PRODUCTS = {} #This is a dictionary to have all product we have on sale
LIST_PRODUCT = [] #This a list to have the products we have sold
main_menu()
