import freshdesk
import requests

def main():
    api = freshdesk.Freshdesk('KBgglQ7Ef7h21DeSuVIg','universa','uBHEfXV?')
    api.elastic()
    print("Tickets atualizados com sucesso!")


if __name__ == '__main__':
    main()