def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Give me name and phone please"
        except KeyError:
            return "Contact not found"
    return inner

@input_error
def parse_input(user_input):
    if not user_input:
        return None, None
    cmd, *args = user_input.split()
    cmd = cmd.lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        raise ValueError
    name, phone = args
    contacts[name.lower()] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        raise ValueError
    name, phone = args
    if name.lower() in contacts:
        contacts[name.lower()] = phone
        return "Contact changed."
    raise KeyError

@input_error
def phone_contact(args, contacts):
    if len(args) < 1:
        raise ValueError
    username = args[0].lower()
    if username in contacts:
        return contacts[username]
    raise KeyError

@input_error
def show_all_contacts(contacts):
    if not contacts:
        return "No contacts found."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}:{phone}")  # Формат "name:phone" без пробілу
    return "\n".join(result)

def main():
    contacts = {}
    while True:
        command_input = input("Enter a command: ").strip()
        cmd, *args = parse_input(command_input)
        if cmd in ["exit", "close"]:
            print("Good bye!")
            break
        elif cmd == "hello":
            _ = input("Enter the argument for the command ")
        elif cmd == "add":
            if len(args) < 2:  # Якщо аргументів менше 2, просимо ввести ще
                _ = input("Enter the argument for the command ")
            else:
                print(add_contact(args, contacts))
        elif cmd == "change":
            if len(args) < 2:
                _ = input("Enter the argument for the command ")
            else:
                print(change_contact(args, contacts))
        elif cmd == "phone":
            if len(args) < 1:
                _ = input("Enter the argument for the command ")
            else:
                print(phone_contact(args, contacts))
        elif cmd == "all":
            print(show_all_contacts(contacts))
        else:
            _ = input("Enter the argument for the command ")

if __name__ == "__main__":
    main()