import pprint
class Data:
    # я просто очень устала)
    time_dict = {
        0: '8:00', 1: '10:00',
        2: '12:00', 3: '14:00',
        4: '16:00', 5: '18:00'
    }

    def __init__(self, data, number_lesson, weekday):
        """
        :param data: Входной json file
        :param number_lesson: порядковый номер пары
        :param weekday: день недели начиная с понедельника
        т.е 8:00 - 9:40 - 0 Пара
        10:00 - 11:49 1 пара и т.д.
        """
        self.data = data
        self.number_lesson = number_lesson
        self.weekday = weekday
        self.date = ''
        self.time_start = ''
        self.time_end = ''
        self.typeObj = ''
        self.nameObj = ''
        self.nameTeach = ''
        self.auditories = ''
        self.get_all()

    def get_all(self):
        pprint.pprint(self.data)
        # get  date
        for i in self.data['days']:
            if i['weekday'] == self.weekday:
                self.date = i['date']
                if i['lessons']['time_start'] == Data.time_dict[self.number_lesson]:
                    self.time_start = i['lessons']['time_start']
                    self.time_end = i['lessons']['time_end']
                    self.typeObj = i['lessons']["typeObj"]["name"]
                    self.nameObj = i['lessons']["subject"]
                    self.nameTeach = i['lessons']["teachers"]["full_name"]
                    self.auditories = f'i{i["lessons"]["auditories"]["building"]["name"]} аудитория {i["lessons"]["auditories"]["name"]}'
