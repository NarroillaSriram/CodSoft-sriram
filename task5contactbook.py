class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email=None, address=None):
        self.contacts[name] = {
            "phone_number": phone_number,
            "email": email,
            "address": address
        }

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            print("Contact not found.")

    def update_contact(self, name, phone_number=None, email=None, address=None):
        if name in self.contacts:
            if phone_number:
                self.contacts[name]["phone_number"] = phone_number
            if email:
                self.contacts[name]["email"] = email
            if address:
                self.contacts[name]["address"] = address
        else:
            print("Contact not found.")

    def view_contacts(self):
        for name, details in self.contacts.items():
            print(f"{name}:")
            print(f"Phone Number: {details['phone_number']}")
            if details['email']:
                print(f"Email: {details['email']}")
            if details['address']:
                print(f"Address: {details['address']}")
            print("--------------------")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"{name}:")
            print(f"Phone Number: {self.contacts[name]['phone_number']}")
            if self.contacts[name]['email']:
                print(f"Email: {self.contacts[name]['email']}")
            if self.contacts[name]['address']:
                print(f"Address: {self.contacts[name]['address']}")
        else:
            print("Contact not found.")

def main():
    contact_book = ContactBook()
    while True:
        print("\n1. Add Contact")
        print("2. Delete Contact")
        print("3. Update Contact")
        print("4. View Contacts")
        print("5. Search Contact")
        print("6. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email (optional): ")
            address = input("Enter address (optional): ")
            contact_book.add_contact(name, phone_number, email, address)
        elif choice == "2":
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)
        elif choice == "3":
            name = input("Enter name to update: ")
            phone_number = input("Enter new phone number (optional): ")
            email = input("Enter new email (optional): ")
            address = input("Enter new address (optional): ")
            contact_book.update_contact(name, phone_number, email, address)
        elif choice == "4":
            contact_book.view_contacts()
        elif choice == "5":
            name = input("Enter name to search: ")
            contact_book.search_contact(name)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()