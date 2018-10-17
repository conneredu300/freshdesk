import requests
from elasticsearch import Elasticsearch
import json

class Freshdesk:
    api_key = ""
    domain = ""
    password = ""
    es = False

    def __init__(self,apikey,domain,password):
        self.api_key = apikey
        self.domain = domain
        self.password = password
        self.es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


    def returnAllTickets(self):
        r = requests.get("https://"+ self.domain +".freshdesk.com/api/v2/tickets?", auth = (self.api_key, self.password))
        if r.status_code == 200:
          return r.json()

        print("x-request-id : " + r.headers['x-request-id'])
        print("Código : " + str(r.status_code))


    def elastic(self):
        data = self.returnAllTickets()

        for i in range(0, len(data)):
            try:
                self.es.index(index='sw', doc_type='people', id=i, body=data[i])
            except:
                print("Não tenho a menor ideia")
