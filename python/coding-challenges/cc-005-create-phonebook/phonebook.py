def entry():
    global entry
    choice = input ("Welcome to the phonebook application\n\
    1. Find phone number\n\
    2. Insert a phone number\n\
    3. Delete a person from the phonebook\n\
    4. Terminate\n\
    Select operation on Phonebook App (1/2/3) : ")
    if choice not in ["1", "2", "3", "4"]:
        print ("Invalid input format, please try again!")
    return choice

def one():
    global ph_book
    name = input("Find the phone number of: ")
    for i in ph_book:
        if name == i:
            return print(ph_book[i])
    return print(f"Couldn't find phone number of {name}")
    
def two():
    global ph_book
    name = input("Insert name of the person: ")
    num = input("Insert phone number of the person")
    if not num.isdigit():
        return print("Invalid input format, cancelling operation..")
    else:
        ph_book[name] = int(num)
    return print(f"Phone number of {name} is inserted into the phonebook")

def three():
    global ph_book
    name = input("Whom to delete from phonebook: ")
    if name not in ph_book:
        return print(f"Couldn't find phone number of {name}")
    else:
        ph_book.pop(name)
        return print(f"{name} is deleted from the phonebook")
    
choice = ""
ph_book = {}

while choice != '4':
    choice = entry()

    if choice == "1":
        one()
    elif choice == "2":
        two()
    elif choice == "3":
        three()

print ("Exiting Phonebook")