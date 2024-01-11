contacts={}
def AddContact(name,phone_number,email,address):
    contacts[name]={
        'phone_number':phone_number,
        'email':email,
       'address':address,

}
    print(f"Contact {name} has added successfully")
def viewContactList():
    print("\nContact List:")
    for name, details in contacts.items():
        print("-----------------------------------------------------")
        print(f"'name'{name}:\n 'phone_number'{details['phone_number']}\n'email:'{details['email']}\n'address:'{details['address']}")
def SearchContact(keyword):
    results = [(name, details) for name, details in contacts.items()
               if keyword.lower() in name.lower() or keyword in details['phone_number']]
    if results:
        print("\nSearch Results:")
        for name, details in results:
            print(f"{name}: {details['phone_number']}")
    else:
        print(f"No contacts found for '{keyword}'.")
def UpdateContact(name):
    if name in contacts:
        print(f"\nUpdating contact: {name}")
        new_phone_number = input("Enter new phone number: ")
        new_email = input("Enter new email: ")
        new_address = input("Enter new address: ")
        contacts[name] = {
            'phone_number': new_phone_number,
            'email': new_email,
            'address': new_address
        }
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"No contact found with the name '{name}'.")


def DeleteContact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"No contact found with the name '{name}'.")
def main():
    while True:
        print("\nContact  Book")
        print("1. Add new Contact")
        print("2. View your Contact List")
        print("3. Search Contact from list")
        print("4. Update your Contact list")
        print("5. Delete your  Contact list")
        print("6. Exit from contact list")
        user_choice = input("Enter your choice (1-6): ")

        if user_choice == '1':
            name = input("Enter the name which wont to add in your contact book  : ")
            phone_number = input("Enter the phone number: ")
            email = input("Enter the  email: ")
            address = input("Enter the address: ")
            AddContact(name, phone_number, email, address)

        elif user_choice == '2':
            viewContactList()

        elif user_choice == '3':
            keyword = input("Enter name or phone number to search: ")
            SearchContact(keyword)

        elif user_choice == '4':
            name = input("Enter the name of the contact to update: ")
            UpdateContact(name)

        elif user_choice == '5':
            name = input("Enter the name of the contact to delete: ")
            DeleteContact(name)

        elif user_choice == '6':
            print("Exiting Contact Management System.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()

