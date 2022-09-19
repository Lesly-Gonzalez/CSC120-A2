# Import a few useful containers from the typing module
from calendar import c
from typing import Dict, Union

# Import the functions we wrote in procedural_resale_shop.py
#from procedural_resale_shop import buy, update_price, sell, print_inventory, refurbish #Remember to comment out this line
from oo_resale_shop import ResaleShop
from computer import Computer


def main():

# MY CODE
#____________________________________________________________________

    # Create a new computer using the create.computer function from the class "Computer"
    new_computer = Computer.create_computer( "Mac Pro (Late 2013)",
              "3.5 GHc 6-Core Intel Xeon E5",
               1024, 64, "macOS Big Sur", 2013, 1500) 


    # Add the new computer to the resale store's inventory
    print("Buying", new_computer["description"])
    print("Adding to inventory...")
    theShop = ResaleShop()
    computer_id = theShop.buy(new_computer) 
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    inventory = ResaleShop.print_inventory(theShop)
    print(inventory)
    print("Done.\n")

    #Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    theShop.refurbish(computer_id, new_OS) #'Computer' object is not subscriptable
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    new_inventory = ResaleShop.print_inventory(theShop) #create new_inventory varible to access the inventory with the updates version of the computer
    print(new_inventory)
    #print(inventory)
    print("Done.\n")

    #Now, let's sell it!
    print("Selling Item ID:", computer_id)
    theShop.sell(computer_id)

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    theShop.print_inventory()
    print("Done.\n")

    #Testing to see whether the error message in the refurbish function works
    theShop.refurbish(computer_id)

#______________________________________________________________

    
# Calls the main() function when this file is run
if __name__ == "__main__": main()
