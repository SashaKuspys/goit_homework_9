# Функція-декоратор для обробки винятків вводу
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid input."
        except IndexError:
            return "Invalid command."
    return wrapper

# Словник для збереження контактів
contacts = {}

# Додати контакт до словника
@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"Contact {name} with phone {phone} has been added."

# Змінити номер телефону для існуючого контакту
@input_error
def change_contact(name, phone):
    contacts[name] = phone
    return f"Contact {name} phone has been changed to {phone}."

# Вивести номер телефону для зазначеного контакту
@input_error
def show_phone(name):
    return f"{name}'s phone number: {contacts[name]}"

# Вивести всі контакти
def show_all():
    if not contacts:
        return "Contact list is empty."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

# Головний цикл бота
def main():
    print("How can I help you?")
    while True:
        command = input("Enter a command: ").lower()

        if command == "good bye" or command == "close" or command == "exit":
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            _, name, phone = command.split()
            print(add_contact(name, phone))
        elif command.startswith("change"):
            _, name, phone = command.split()
            print(change_contact(name, phone))
        elif command.startswith("phone"):
            _, name = command.split()
            print(show_phone(name))
        elif command == "show all":
            print(show_all())
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()
