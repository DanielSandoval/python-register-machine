'''register machine'''
# Aqui escribe tu codigo

import os

def ClearScreen():
    os.system('reset')

def MainMenu():
    ClearScreen()
    print "1. Add an item" #Prints this in Main Menu
    print "2. Sell Articles" #Prints this in Main Menu
    print "3. Exit" #Prints this in Main Menu

def Option1():
    product = raw_input("Enter a product: ")
    price = int(raw_input("Enter a price: "))
    my_products[product] = price
    print my_products

def OptionY(add):
    #if add == "y":
    while add == "y":
        Option1()
        add = raw_input("Do you want to add another item?: ")
        add = add.lower()
        if add == "n":
            OptionN()

def OptionN():
    MainMenu()

def OptionDifferent():
    print "PLEASE ENTER \"y\" OR \"n\" OR \"done\""

def OptionDone(done):
    total = 0
    if buy in my_products:
        total += my_products[buy]
    print "Gracias por su compra, su total es: ", total
    ok = raw_input("PRESS ENTER")
    ClearScreen()
    MainMenu()

def OptionAdd(add):
    if add == "y":
        OptionY(add)
    elif add == "n":
        OptionN()
    elif add != "y" or add != "n":
        OptionDifferent()

OPTION_NUMBER = True #Declares a variable option
my_products = {}

while OPTION_NUMBER == True and OPTION_NUMBER != False: #Starts a cycle "while" option be zero
    print OPTION_NUMBER
    try: #Starts a Try
        MainMenu()
        OPTION = int(raw_input("Select the number of the action you want to perform: "))
        ClearScreen()
        if OPTION == 1:
            try:
                Option1()
                add = raw_input("Do you want to add another item?: ")
                add = add.lower()
                OptionAdd(add)
            except ValueError:
                print "ENTER TEXT"
        elif OPTION == 2:
            buy = raw_input("Which product you want to buy?: ")
            if buy != "done":
                print my_products[buy], buy
            total = 0
            while buy != "done":
                if buy in my_products:
                    total += my_products[buy]
                    buy = raw_input("Other product you want to buy? Or write \"done\": ")
                    if buy != "done":
                        print my_products[buy], buy
                    if buy == "done":
                        print "Gracias por su compra, su total es: ", total
                        ok = raw_input("PRESS ENTER")
                        ClearScreen()
                        MainMenu()
            if buy == "done":
                print "First write the product that you want to buy"
        elif OPTION == 3: #If the input is equals to 3 makes the next code
            OPTION_NUMBER = False
    except ValueError: #Makes an exception and name the exception
        print "ENTER A NUMBER BETWEEN 1 AND 3 TO CHOOSE" #Prints an instruction
