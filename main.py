''' БОТ - ТЕЛЕФОННА КНИГА '''

#створюємо словник для запису контактів
contacts = {}

def input_error(func):
    # Декоратор для обробки помилок введення користувача.
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter a valid name"  # Обробляє помилку відсутності ключа.
        except ValueError:
            return "Invalid input. Please provide valid name and phone"  # Обробляє неправильний формат вводу.
        except IndexError:
            return "Invalid input format. Use 'add', 'change', or 'phone' followed by name and phone"  # Обробляє неправильний формат команди.
    return wrapper

@input_error
def add_contact(name, phone):
    # Перевірка: чи є контакт в базі
    if name in contacts:
        raise ValueError
    # Додаємо контакт у словник
    contacts[name] = phone
    return f'Contact {name} with number {phone} in base now'

@input_error
def change_phone(name, new_phone):
    # Змінюємо номер телефону для існуючого контакту.
    if name not in contacts:
        raise KeyError
    else:
        contacts[name] = new_phone
        return f"Phone number of {name} has been changed {new_phone}."

@input_error
def get_phone(name):
    # Отримуємо номер телефону за ім'ям контакту.
    if name not in contacts:
        raise KeyError 
    else:
        return f"Contact '{name} has number {contacts[name]}"

@input_error
def show_all_contacts(contacts):
    # Виводимо всі збережені контакти у консоль.
    if not contacts:
        raise IndexError
    
    for name, phone in contacts.items():
        print(f"{name}: {phone}")


def handle(com):                            #Обробка заглавних і строкових букв
    split_command = ''
    for char in com:
        if char != ' ':
            split_command += char.lower()
        else:
            break
    return split_command


def split_com(com):
    return com.split()

def main():
       
    print('Hello!')                            #Старт
    print("How can I help you?")
    
    def hello_function():                      #Вітання
        print('How can I help you? \n')

    def add_function():
        if len(command) < 3:                   #Перевірка на кількість букв в імені
            print('Error: input correct name and phone number')
        else:
            print(add_contact(command[1], command[2]))
    
    def change_function():
        if len(command) < 3:                   #Перевірка на кількість букв в імені
            print('Error: input correct name and phone number')
        else:
            print(change_phone(command[1], command[2]))
    
    def phone_function():
        if len(command) < 2:                   #Перевірка на кількість цифр в номері
            print('Error: input correct name')
        else:
            print(get_phone(command[1]))
    
    def show_all_function():
        print(show_all_contacts(contacts))

    while True:
        do_command = input(f'Write command :')

        command = split_com(do_command)

        split_command = handle(do_command)

        all_commands = {
            'hello': hello_function,
            'add': add_function,
            'change': change_function,
            'phone': phone_function,
            'show all': show_all_function,
            'good bye': lambda: print("Good bye!"),
            'close': lambda: print("Good bye!"),
            'exit': lambda: print("Good bye!")
        }

        if do_command in all_commands:
            all_commands[do_command]()
            if do_command.lower() in ('good bye', 'close', 'exit'):
                break
        
        elif split_command in all_commands:
            all_commands[split_command]()

        else:
            print("Unknown command. Use: 'hello', 'add', 'change', 'phone', 'show all', 'good bye', 'close' or 'exit'")

if __name__ == "__main__":
    # Запускаємо бота
    main()
