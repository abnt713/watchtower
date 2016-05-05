from colorama import Fore, Style


def header():
    print()
    print_data("Watchtower", Fore.MAGENTA)
    print_data("- The last stand against the unknow", Fore.CYAN)
    print()
    print()

    print_data("Welcome, hunter. Press enter to continue at any point")
    print_data("It is important to keep track of the creatures you discover")
    print_data("Use the codex to find out more about that creature")

    input("Press enter to continue...")


def print_data(string, color=Fore.GREEN):
    item = data(string, color)
    print(item)


def data(string, color=Fore.RED):
    return "%s %s%s" % (color, string, Fore.RESET)


def main():
    header()


if __name__ == '__main__':
    main()
