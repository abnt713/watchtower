from states import get_state


def main():
    next_state, arguments = get_state('tutorial').run()
    while True:
        return_state, return_arguments = get_state(next_state).run(arguments)
        next_state = return_state
        arguments = return_arguments


if __name__ == '__main__':
    main()
