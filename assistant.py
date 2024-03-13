def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args[1:], **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."

@input_error
def show_all(contacts):
    return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()
        if user_input.lower() in ["close", "exit"]:
            print("Good bye!")
            break
        elif user_input.lower() == "hello":
            print("How can I help you?")
        elif user_input.lower().startswith("add "):
            _, name, phone = user_input.split(maxsplit=2)
            print(add_contact(contacts, name, phone))  # Pass both name and phone
        elif user_input.lower().startswith("change "):
            _, name, phone = user_input.split(maxsplit=2)
            print(change_contact(contacts, name, phone))
        elif user_input.lower().startswith("phone "):
            _, name = user_input.split(maxsplit=1)
            print(show_phone(contacts, name))
        elif user_input.lower() == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
