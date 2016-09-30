import os
import json

class AddressBook(object):
# private methods

    def __init__(self, filename):
        self.filename = filename
        self.contacts = []

        try:
            if os.path.isfile(self.filename):
                # try to read the contacts list from file
                with open(self.filename, 'r') as f:
                    self.contacts = json.load(f)
            else:
                # creating new database file
                with open(self.filename, 'w') as f:
                    pass
        except:
            pass

    def __saveToFile(self):
        with open(self.filename, 'w') as f:
            json.dump(self.contacts, f)

# public methods
    def returnContacts(self):
        return self.contacts

    def searchContact(self, criteria, search_phrase):
        for element in self.contacts:
            if element[criteria] == search_phrase:
                return element

    def addContact(self, name, surname, mail, phone_number):
        self.contacts.append({'name':name, 'surname':surname, 'mail':mail, 'phone_number':phone_number})
        self.__saveToFile()

    def deleteContact(self, index):
        self.contacts.pop(index)
        self.__saveToFile()

    def editContact(self, index, key, value):
        self.contacts[index][key] = value
        self.__saveToFile()
    
    
