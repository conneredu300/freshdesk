import freshdesk
import requests

def main():
    api = freshdesk.Freshdesk(APIKEY,DOMINIO,SENHA)
    api.elastic()
    print("Tickets atualizados com sucesso!")


if __name__ == '__main__':
    main()
