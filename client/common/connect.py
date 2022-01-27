import requests
import json


    

class get_inform(object):
    def __init__(self, method, schema,token):
        self.token=token
        self.method=method
        self.schema=schema



    def get_inform(self):  # Получение данных
        
        host = 'https://invest-public-api.tinkoff.ru/rest/'
        head = {'Authorization': f'Bearer {self.token}', 'Content-Type': 'application/json', 'accept': 'application/json'}
        response = json.loads(requests.post(host + self.method, headers=head, data=f'{self.schema}').text)
        # print(requests.post(host + name, headers=head, data=f'{schema}'))
        return response
