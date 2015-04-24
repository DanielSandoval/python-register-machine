'''register machine'''
# Aqui escribe tu codigo

print "1. Add an item" #Prints this in Main Menu
print "2. Sell Articles" #Prints this in Main Menu
print "3. Exit" #Prints this in Main Menu

OPCION = 0

while OPCION == 0:
    try: #Starts a Try
        #Asks to enter a number to choose
        OPCION = int(raw_input("Select the number of the action you want to perform: "))
        if OPCION == 3: #If the input is equals to 3 makes the next code
            pass #Exits the program
    except ValueError: #Makes an exception and name the exception
        OPCION = 0
        print "ENTER A NUMBER BETWEEN 1 AND 3 TO CHOOSE" #Prints an instruction
