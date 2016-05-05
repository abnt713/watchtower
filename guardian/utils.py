from colorama import Fore


def print_data(string, color=Fore.GREEN, end="\n"):
    item = data(string, color)
    print(item, end=end)


def data(string, color=Fore.RED):
    return "%s %s%s" % (color, string, Fore.RESET)
