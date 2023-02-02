
from dataHandler import DataHandler
from contact import Contact
import itertools

contacts = []

#switch cases and main
def main():

    while True:
        selection = menuSelection()

        match selection:
            case 1:
                viewAllContacts()
            case 2:
                addNewContact()
            case 3:
                deleteContact()
            case 4:
                updateContact()
            case 5:
                searchForContact()
            case 6:

                print("--------------------------------------------------------")
                print("Thanks for using the contacts viewer, goodbye :)")
                print("--------------------------------------------------------")
                print()
            
                break





#menu selection

def menuSelection ():
    print("--------------------------------------------------------")
    print("Welcome to the contact list menu, what would you like to do?")
    print()

    print("1: View full list of contacts")
    print("2: Add new contact")
    print("3: Delete a contact")
    print("4: Update a contact")
    print("5: Search for a contact")
    print("6: Quit the application")
    print()
    
    while True:
        print("Enter a number corresponding to the above menu and then press ENTER")
        print()
        selection = input("")
        print()

        try:
            selectionToInt = int(selection)

            if selectionToInt < 7 and selectionToInt > 0:
                return selectionToInt
                break
            else:
                print ("Sorry that numbr does not exist in the above menu, pleas echoose again")
        except ValueError:
            print(f"sorry, {selection} is not a number. Please choose anumber from the menu")



def viewAllContacts ():
    print("--------------------------------------------------------")
    print("Full contacts list")
    print("--------------------------------------------------------")
    print("")

    contacts = DataHandler.getAll()

    if len(contacts) != 0:
        for contact in contacts:
            print(contact)
    else:
        print("You do not have any contacats yet!")
        print()

    print()
    

def addNewContact():
    print("--------------------------------------------------------")
    print("Add a new contact")
    print("--------------------------------------------------------")
    print("")

    while True:
        print("please enter a name and then press the ENTER key to submit")
        name = input("")
        print()

        if len(name) != 0:
            break
        else:
            print("Sorry, no name was entered, please enter a name of at least one character")
            print()
    
    print("Now please enter a phone number.")
    print("If you wish to leave the phone number empty, just press ENTER")
    phoneNumber = input()
    
    print()
    print("Now please enter an email address.")
    print("If you wish to leave the email address empty, just press ENTER")
    email = input()
    print()

    if email == "" and phoneNumber == "":
        contact = Contact(name, "no number supplied", "no email supplied")
    elif email == "" and phoneNumber !="":
        contact = Contact(name, phoneNumber, "no email supplied")
    elif email != "" and phoneNumber =="":
        contact = Contact(name, "no number supplied", email)
    else:
        contact = Contact(name,phoneNumber,email)

    DataHandler.addContact(contact)


def deleteContact():
    print("--------------------------------------------------------")
    print("Delete a contact")
    print("--------------------------------------------------------")
    print()

    contacts = DataHandler.getAll()

    for i,contact in zip(itertools.count(),contacts):
        print(f"{i}: {contact}")
    print("--------------------------------------------------------")
    print()

    print("Select the number of the contact you would like to delete and press ENTER")
    print()
    inputString = input("")
#need while loop to ensure int input

    selection = int(inputString)

    if selection >=0 and selection <= len(contacts):
        print("contact: " + contacts[selection].getName() + " has been deleted")
        DataHandler.deleteContact(selection)   
        print()
    else:
        print("selection invalid, no contacts have been deleted")
        print()


def updateContact ():
    print("--------------------------------------------------------")
    print("Update a contact")
    print("--------------------------------------------------------")
    print("")

    contacts = DataHandler.getAll()

    for i,contact in zip(itertools.count(),contacts):
        print(f"{i}: {contact}")
    print("--------------------------------------------------------")

    print()
    print("Select the number of the contact you would like to update and press ENTER")
    print()

    while True:
        inputString = input("")
        selection = int(inputString)

        if selection >-1 and selection <= len(contacts):
            contact = contacts[selection]
            print("contact to update is:")
            print(contact)
            print()
            
            print("Please enter a new name and press the ENTER key to submit")
            print("If you don't wish to change the name, just press ENTER")
            print()
            name = input("")
            print()

            if len(name) == 0:
                print("Ok, name will not be changed")
                print()
            else:
                print("Thanks, name will be changed to: " + name)
                print()
                contact.setName(name)

            print("Now please enter a phone number.")
            print("If you wish to leave the phone number empty, just press ENTER")
            print()
            phoneNumber = input()
            print()

            if len(phoneNumber) == 0:
                print("Ok, phone number will not be changed")
                print()
            else:
                print("Thanks, phone number will be changed to: " + phoneNumber)
                print()
                contact.setPhoneNumber(phoneNumber)

            print("Now please enter an email address.")
            print("If you wish to leave the email address empty, just press ENTER")
            print()
            email = input()
            print()

            if len(email) == 0:
                print("Ok, email will not be changed")
                print()
            else:
                print("Thanks, email will be changed to: " + email)
                print()
                contact.setEmail(email)


            DataHandler.updateContact(selection,contact)
            break

        else:
            print("selection invalid, please re-enter")
            print()


def searchForContact ():
    print("--------------------------------------------------------")
    print("Search for a contact")
    print("--------------------------------------------------------")
    print("")

    print("Please enter a name to search for")
    print()
    inputName = input("")
    print()

    contact = DataHandler.getSpecificContact(inputName)

    if contact is None:
        print("Sorry, no contacts exist with that name")
        print()
    else:
        print("Contact found! Here are their details:")
        print(contact)
        print()




#to run main
if __name__=="__main__":
    main()