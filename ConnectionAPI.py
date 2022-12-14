import http.client
import json
from pprint import pprint
import collections


class ConnectionApi:
    def __init__(self, group_name):
        self.schedule_dict = None
        self.group_id = None
        self.group_name = group_name
        self.ans_dict = None
        self.get_group_id_by_name()
        self.get_schedule_by_id()


    def get_group_id_by_name(self):
        server_address = "ruz.spbstu.ru"
        request = f'/api/v1/ruz/search/groups?&q={self.group_name}'
        connection = http.client.HTTPSConnection(server_address)
        connection.request('GET', request)
        response = connection.getresponse()
        ans = response.read()
        connection.close()
        self.group_id = json.loads(ans)['groups'][1]['id']


    def get_schedule_by_id(self):
        server_address = "ruz.spbstu.ru"
        request = f'https://ruz.spbstu.ru/api/v1/ruz/scheduler/{self.group_id}'
        connection = http.client.HTTPSConnection(server_address)
        connection.request('GET', request)
        response = connection.getresponse()
        self.schedule_dict = json.loads(response.read())
        connection.close()

