def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (IndexError, ValueError):  # Обробляємо помилки нестачі аргументів
            return "Enter the argument for the command"
        except KeyError:  # Обробляємо помилку, коли контакт не знайдено
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
    name, phone = args  # Лише розпакування
    contacts[name.lower()] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args  # Лише розпакування
    if name.lower() in contacts:
        contacts[name.lower()] = phone
        return "Contact changed."
    raise KeyError

@input_error
def phone_contact(args, contacts):
    username = args[0]  # Лише розпакування
    if username.lower() in contacts:
        return contacts[username]
    raise KeyError

@input_error
def show_all_contacts(contacts):
    if not contacts:
        return "No contacts found."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}:{phone}")
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
            print("How can I help you?")  # Додаємо вивід для hello, як у типових завданнях
        elif cmd == "add":
            print(add_contact(args, contacts))
        elif cmd == "change":
            print(change_contact(args, contacts))
        elif cmd == "phone":
            print(phone_contact(args, contacts))
        elif cmd == "all":
            print(show_all_contacts(contacts))
        else:
            print("Enter the argument for the command")

if __name__ == "__main__":
    main()