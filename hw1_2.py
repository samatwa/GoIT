def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name.capitalize()] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    contacts[name.capitalize()] = phone
    return "Contact updated."

def show_phone(args,contacts):
    try:
        for i in args:
            i=i.capitalize()
            if i in contacts:
                return f'{i}: {contacts[i]}'
    except Exception:
            return "Are you sure? This name doesn\'t exist in contacts"

def show_all(args,contacts):
    for name, phone in contacts.items():
        print(name,':',phone)

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
            print(show_phone(args,contacts))
        elif command == "all":
            show_all(args, contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()