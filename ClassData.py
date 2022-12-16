import pprint


class Data:
    def __init__(self, data, number_lesson, weekday):
        """
        Инициализация класса Data который принимает данные из словаря и создает объект
        с атрибутами, которые сохраняют в себе данные о занятии

        :param data: Входной dict_file
        :param number_lesson: порядковый номер пары
        :param weekday: день недели начиная с понедельника

        """
        self.data = data
        self.number_lesson = number_lesson
        self.weekday = weekday+1
        self.date = ''
        self.time_start = ''
        self.time_end = ''
        self.typeObj = ''
        self.nameObj = ""
        self.nameTeach = ''
        self.auditories = ''
        self.get_all()

    def get_all(self):
        print('Connection')
        # get data in json

        for date in self.data['days']:
            if date['weekday'] == self.weekday:
                try:
                    self.date = date['date']
                    self.time_start = date['lessons'][self.number_lesson]['time_start']
                    self.time_end = date['lessons'][self.number_lesson]['time_end']
                    self.typeObj = date['lessons'][self.number_lesson]["typeObj"]["name"]
                    self.nameObj = date['lessons'][self.number_lesson]["subject"]
                    self.nameTeach = date['lessons'][self.number_lesson]["teachers"][0]["full_name"]
                    self.auditories = f'''
i{date["lessons"][self.number_lesson]["auditories"][0]["building"]["name"]} аудитория 
{date["lessons"][self.number_lesson]["auditories"][0]["name"]} '''
                except TypeError: # if any datas in json is empty, assignment will be missing
                    continue
