
from contact import Contact

# contacts = []

class DataHandler(object):
    contacts = []
    with open ('contacts.txt', encoding="utf- 8") as fp:
            for line in fp:
                name, phoneNumber,email = line.split('|')
                contact = Contact(name,phoneNumber,email.removesuffix('\n'))
                contacts.append(contact)


    def __init__(self):
        pass

    #get all
    def getAll ():
        DataHandler.contacts.clear()
        #read in contacts
        with open ('contacts.txt', encoding="utf- 8") as fp:
            for line in fp:
                name, phoneNumber,email = line.split('|')
                contact = Contact(name,phoneNumber,email.removesuffix('\n'))
                DataHandler.contacts.append(contact)
                
        return DataHandler.contacts

  
    def addContact(contact):
        DataHandler.contacts.append(contact)
        #write to file
        with open('contacts.txt','w', encoding="utf-8") as fp:
            for contact in DataHandler.contacts:
                fp.write(f"{contact.name}|{contact.phoneNumber}|{contact.email}\n")


   
    def getSpecificContact (searchName):
        for contact in DataHandler.contacts:
            if contact.getName().lower().strip() == searchName.lower().strip():
                return contact

    #verifyName? for duplicate?
    def checkIfNameExists (name):
        for contact in DataHandler.contacts:
            if contact.getName == name:
                return "exists"
            else:
                return "ok"

    def deleteContact(selection):
        del DataHandler.contacts[selection]
        with open('contacts.txt','w', encoding="utf-8") as fp:
            for contact in DataHandler.contacts:
                fp.write(f"{contact.name}|{contact.phoneNumber}|{contact.email}\n")

    def updateContact(selection, contact):
        contactToUpdate = DataHandler.contacts[selection]
        contactToUpdate.setName(contact.getName())
        contactToUpdate.setPhoneNumber(contact.getPhoneNumber())
        contactToUpdate.setEmail(contact.getEmail())

        with open('contacts.txt','w', encoding="utf-8") as fp:
            for contact in DataHandler.contacts:
                fp.write(f"{contact.name}|{contact.phoneNumber}|{contact.email}\n")
