from container import Container


ALL_FUNCTIONS = '''
* add <key> [key, …] – add one or more elements to the container (if the element is already in therea then don’t add);
* remove <key> – delete key from container;
* find <key> [key, …] – check if the element is presented in the container, print each found or “No such elements” if nothing is;
* list – print all elements of container;
* grep <regex> – check the value in the container by regular expression, print each found or “No such elements” if nothing is;
* save - save container to file;
* switch – switches to another user;
* exit - leave from program;
* help - show all commands;
* load - loads container from file.
'''


def parse_command():
    user_input = input('> ').split(maxsplit=1)

    if len(user_input) == 0:
        print('Input must be not empty!')

    command = user_input[0]
    arguments = ''
    if len(user_input) > 1:
        arguments = user_input[1]
    return command, arguments


def ask_save_container(storage: Container):
    answer = input('Do you want to save container?(y/n): ')
    if answer == 'y':
        storage.save()


def greeting(username: str):
    print(f'Hello, {username}!')


def exec_command(command: str, arguments: str, storage: Container) -> bool:
    match command:
        case 'add':
            arguments_list = arguments.split()
            for el in arguments_list:
                storage.add(el)
        case 'remove':
            storage.remove(arguments)
        case 'list':
            print(storage.list())
        case 'find':
            if len(arguments) != 0:
                arguments_list = arguments.split()
                for el in arguments_list:
                    found = storage.find(el)
                    print(f'{el} found' if found else f'{el} not found')
        case 'grep':
            res = storage.grep(arguments)
            if len(res) != 0:
                print('Found values: ' + str(res))
        case 'save':
            storage.save(arguments)
            print('Container was saved successfully!')
        case 'help':
            print(ALL_FUNCTIONS)
        case 'exit':
            ask_save_container(storage)
            return False
        case 'switch':
            ask_save_container(storage)
            storage.switch(arguments)
            greeting(arguments)
        case 'load':
            storage.load(arguments)
        case _:
            print('Such command not supported')
    return True


def main():
    print('Welcome to storage for unique elements!')
    username = input('Enter your username: ')
    storage = Container(username)
    print(f'Hello, {username}!')
    print('Type command or \'help\' to get info about available commands.')
    is_working = True
    while is_working:
        command, args = parse_command()
        is_working = exec_command(command, args, storage)


if __name__ == "__main__":
    main()



