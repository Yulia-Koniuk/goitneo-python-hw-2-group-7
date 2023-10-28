# parser
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# decorator for managing mistakes
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as ve:
            if func.__name__ in ['add_contact', 'change_contact']:
                return "Give me name and phone please."
            elif func.__name__ == 'show_phone':
                return "Enter user name."
            else:
                return str(ve)
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid command."

    return inner

# adding new contact
@input_error
def add_contact(args, contacts):
    if len(args) != 2:  
        raise ValueError # adding error
    name, phone = args
    name = name.lower()
    contacts[name] = phone
    return "Contact added."

# rewriting new phone
@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError # adding error
    name, new_phone = args
    name = name.lower()
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        raise KeyError # adding error

# show phone number
@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise ValueError # adding error
    name = args[0].lower()
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError # adding error

# get all contacts
@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    else:
        contacts_list = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
        return contacts_list

# request-response cycle
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all" and not args:
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


    