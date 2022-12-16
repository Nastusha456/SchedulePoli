import tkinter as tk
from ConnectionAPI import ConnectionApi
from ClassData import Data
import customtkinter as ctk


class CreateFrame(Data):
    '''
    класс,который инициализирует фрейм в окне, который выводит описание пары
    '''
    day = ['Понедельник', "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]

    def __init__(self, window, data, number_lesson, weekday):
        """
        :param window: Окно где будет создан фрейм
        :param data: словарь преобразованный из json
        :param number_lesson: номер занятия
        :param weekday: день недели, где 0-Понедельник, 1 - Вторник и тд
        """
        # Добавить условие если данын пустые, то не создавать фрейм
        super().__init__(data, number_lesson, weekday)
        # получение от родительского класса Data данные из словаря
        self.frame = ctk.CTkFrame(window, )
        self.frame.grid(column=weekday, row=number_lesson, padx= 10 , pady=10)
        # Create LabelWeekday
        if not self.nameObj == '' and number_lesson < 1:
            self.label_weekday = ctk.CTkLabel(self.frame, text=CreateFrame.day[weekday])
            self.label_weekday.pack()
        # Create label with information of name subject
        self.label_name_obj = ctk.CTkLabel(self.frame, text=self.nameObj, width=50)
        self.label_name_obj.pack()
        # Create label with information of name Teacher
        self.label_name_teacher = ctk.CTkLabel(self.frame, text=self.nameTeach)
        self.label_name_teacher.pack()
        # Create label with information of time lesson
        self.label_time = ctk.CTkLabel(self.frame,  text=f'{self.time_start}-{self.time_end}')
        self.label_time.pack()
        # if self.time_end == '' and self.nameObj == '':
        #     self.frame.quit()



class App:
    day = ['Понедельник', "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]

    def __init__(self, window):

        self.wind = window
        self.wind.geometry(f'{250}x{200}')
        self.wind.title('Schedule politech')

        # Creating a Frame
        self.frame = ctk.CTkFrame(master=window, width=200, height=200, corner_radius=10)
        self.frame.pack()

        # Creating image
        # self.canvas = ctk.CTkCanvas(self.frame, height=100, width=370)
        # self.img = tk.PhotoImage(file='Headimage.png')
        # self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.img)
        # self.canvas.grid(row = 0, column=0)

        # Creating Entry
        self.entry = ctk.CTkEntry(self.frame, width=250)
        self.entry.grid(pady=50, row=1, column=0, sticky='n')

        # Creating Button
        self.button = ctk.CTkButton(self.frame, width=250, text='Найти группу', command=self.get_schedule)
        self.button.grid(pady=20, row=2, column=0, sticky='s')

    def get_schedule(self):

        # Connection API
        group_name = self.entry.get()
        if group_name == '':
            self.button.configure(text='Не введена группа')

        else:
            connect = ConnectionApi(group_name)
            self.data_json = connect.schedule_dict
            # Creating Window
            self.schedule = ctk.CTkToplevel()
            self.schedule.title = 'Schedule'
            # Creating Label Frame

            # Creating label of name weekday
            # for i in range(6):
            #     frame = ctk.CTkFrame(self.schedule)
            #     frame.grid(column=0, row=0)
            #     ctk.CTkLabel(frame, text=App.day[i]).grid(row=0, column=i)

            self.create_frame(self.schedule)

    def create_frame(self, window):
        for weekday in range(6):
            for number_lesson in range(6):
                try:
                    CreateFrame(window, self.data_json, number_lesson, weekday)
                except IndexError:  # if lesson in this day is empty cicle is break
                    break
