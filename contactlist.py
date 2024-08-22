print("#"*100)
a = "CONTACT BOOK"
b = a.center(90)
print(b)
print("#"*100)
# Sample Contact List 
contacts = {}  

# Function to add new contacts (example, more details later)
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
   
    # Store the new entry in contacts 
    contacts[name] = { 'phone': phone, 'email': email,  } 

    print(f"Contact '{name}' added successfully.")  

# Function to view all contacts (example)
def display_contacts():
    if not contacts: 
        print("No contacts saved yet!")
    else:
        for name, details in contacts.items():
            print(f"- {name}: Phone: {details['phone']}, Email: {details['email']}")  

# Example function to search for a contact
def search_contact(keyword):
    matches = [] 
    for name, data in contacts.items(): 
        if keyword.lower() in name.lower():  # Case-insensitive searching
            matches.append((name, data['phone'])) # Add the match to list

    if matches:
        print("Found contacts:")
        for contact_info in matches:
            print(f"- Name: {contact_info[0]} Phone: {contact_info[1]}") 
    else: 
        print("No matches found.")  

# Main program loop 
while True: 
    print("\nChoose an option:")
    print("1. Add contact")
    print("2. View all contacts")
    print("3. Search contact")
    print("4. Update contact")  
    print("5. Delete contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ") 

    if choice == '1': 
        add_contact() 
    elif choice == '2': 
        display_contacts() 
    elif choice == '3': 
        search_contact(input("Search for: "))  
    elif choice == '4':
        # Update contact details (more complex to implement)
        pass # This is placeholder, you'll need the logic here!
    elif choice == '5': 
        if not contacts: 
            print("No contacts saved yet!") 
        else: 
            name = input("Enter name of contact to delete: ")  
            del contacts[name]  
            print("Contact deleted.")
    elif choice == '6':  
        break 