import freshdesk

def main():
    api = freshdesk.Freshdesk('KBgglQ7Ef7h21DeSuVIg','universa','uBHEfXV?')
    tickets = api.returnAllTickets()


if __name__ == '__main__':
    main()