'''register machine'''
# Aqui escribe tu codigo

import os

def ClearScreen():
    os.system('reset')

def MainMenu():
    print "1. Add an item" #Prints this in Main Menu
    print "2. Sell Articles" #Prints this in Main Menu
    print "3. Exit" #Prints this in Main Menu

def Option1():
    product = raw_input("Enter a product: ")
    price = int(raw_input("Enter a price: "))
    Option2(product,price)
    #ClearScreen()

def Option2(product,price):
    my_products[product] = price
    print my_products
    #ClearScreen()

def Option3():
    OPTION = False
    #pass #Leaves the program
    #ClearScreen()

def OptionY(product):
    #if product == "y":
    while product == "y":
        Option1()
        product = raw_input("Do you want to add another item?: ")
        product = product.lower()
        if product == "n":
            MainMenu()
    OptionDone(product)
    #ClearScreen()

def OptionN(product):
    #if product == "n":
    MainMenu()
    #ClearScreen()

def OptionDifferent(product):
    #if product != "y" or product != "n" or product != "done":
    print "PLEASE ENTER \"y\" OR \"n\" OR \"done\""
    #ClearScreen()

def OptionDone(product):
    #if product == "done":
    total = 0
    for elements in my_products:
        total += my_products[elements]
    print "Gracias por su compra, su total es: ", total
    ok = raw_input("PRESS ANY BUTTON")
    MainMenu()
    #ClearScreen()

def OptionsProducts(product):
    if product == "y":
        OptionY(product)
    elif product == "n":
        OptionN(product)
    elif product != "y" or product != "n" or product != "done":
        OptionDifferent(product)
    elif product == "done":
        OptionDone(product)
    #ClearScreen()

MainMenu()

OPTION = True #Declares a variable option
my_products = {}

while OPTION == True: #Starts a cycle "while" option be zero
    try: #Starts a Try
        #Asks to enter a number to choose
        OPTION = int(raw_input("Select the number of the action you want to perform: "))
        ClearScreen()
        if OPTION == 3: #If the input is equals to 3 makes the next code
            #OPTION = False
            Option3()
        elif OPTION == 1:
            Option1()
            try:
                product = raw_input("Do you want to add another item?: ")
                product = product.lower()
                OptionsProducts(product)
                OPTION = True #If the exception is true makes option equals to zero
            except:
                print "ENTER TEXT"
        elif OPTION == 2:
            OptionDone(product)
            #OPTION = True #If the exception is true makes option equals to zero
    except ValueError: #Makes an exception and name the exception
        print "ENTER A NUMBER BETWEEN 1 AND 3 TO CHOOSE" #Prints an instruction
