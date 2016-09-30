from AddressBook.AddressBook import AddressBook
import sys



def print_menu():
    print """
    1. show contacts
    2. search contact
    3. add contact
    4. delete contact
    5. edit contact
    6. exits
    """
#####
def take_criteria_to_search():
    print "Please, select your search criteria:"
    print "a) Name\nb) Surname\nc) Mail\nd) Phone number"
    
    while True:
        letter = raw_input("Your choice: ").lower()
        if letter == 'a':
          criteria = "name"
          break
        elif letter == 'b':
          criteria = "surname"
          break
        elif letter == 'c':
          criteria = "mail"
          break
        elif letter == 'd':
          criteria = "phone_number"
          break
        else:
          print "Please, choose a, b, c or d..."

    return criteria

def take_phrase_to_search():
    search_for = raw_input("Please, specify phrase to search: ")
    return search_for

def print_contacts(contacts):
    print "-"*30
    for i in range(1, len(contacts)+1):
        print "%d. Name: %-15s Surname: %-15s email: %-20s phone: %s" % (i, contacts[i-1]['name'], contacts[i-1]['surname'], contacts[i-1]['mail'], contacts[i-1]['phone_number'])
    print "-"*30
def input_number():
    number = ""
    while True:
        try:
            number = int(raw_input("Please, give a number of contact: "))
        except ValueError:
            pass
        number -= 1
        if number >= 0 and number < len(b.returnContacts()): 
            break
        else:    
            print "There's no such contact"
    return number
#############################################
    

if __name__ == "__main__":
    b = AddressBook('./db.json')

    print "Welcome to you personal super awesome Contact Book or so whatevah"
    
    while True:
        print_menu()
        
        try:
            choice = int(raw_input("Choose option: "))
        except ValueError:
            pass
            
        
        if choice == 1:
            print_contacts(b.returnContacts())
        elif choice == 2:
            criteria = take_criteria_to_search()
            phrase = take_phrase_to_search()
            search_result = b.searchContact(criteria, phrase)
            if search_result:
                print "Contact found"
                print "Name: %-25s\tSurname: %-25s\tMail: %-15s\tPhone: %-12s" %  (search_result['name'], search_result['surname'], search_result['mail'], search_result['phone_number'])
            else:
                print "Unfortunately, contact not found..."
        elif choice == 3:
            name = raw_input("Please, specify contact's name: ")
            surname = raw_input("Please, specify contact's surname: ")
            mail = raw_input("Please, specify contact's mail: ")
            phone_number = raw_input("Please, specify contact's phone number: ")
            b.addContact(name, surname, mail, phone_number)
        elif choice == 4:
            print_contacts(b.returnContacts())
            index = input_number()
            b.deleteContact(index)
        elif choice == 5:
            print_contacts(b.returnContacts())
            index = input_number()
            print "Please, select your search criteria:"
            print "a) Name\nb) Surname\nc) Mail\nd) Phone number"
            letter = raw_input("Your choice: ").lower()
            if letter == 'a':
                criteria = "name"
            elif letter == 'b':
                criteria = "surname"
            elif letter == 'c':
                criteria = "mail"
            elif letter == 'd':
                criteria = "phone_number"
            
            value = raw_input("Please, specify new value for %s: " % criteria)
            b.editContact(index, criteria, value)
        elif choice == 6:
            sys.exit(0)
        else:
            print "You can choose between 1-6."  
            continue  
            
            
            