from customtkinter import *
from helpers import create_error
import time, datetime


class Dates_converter():
    def __init__(self, canvas):
        self.canvas = canvas

        self.date_var = StringVar()
        self.date_var.set('datetotimestamp')

        self.date_to_timestamp_switch = CTkRadioButton(text='Date vers Timestamp', value='datetotimestamp',
                                                  variable=self.date_var, bg_color='gray12',
                                                  command=lambda: self.change_text_date_timestamp(
                                                      'Votre date (format JJ/MM/AAAA)'))
        self.canvas.create_window(100, 30, window=self.date_to_timestamp_switch)

        self.timestamp_to_date_switch = CTkRadioButton(text='Timestamp vers Date', value='timestamptodate',
                                                  variable=self.date_var, bg_color='gray12',
                                                  command=lambda: self.change_text_date_timestamp('Votre timestamp'))
        self.canvas.create_window(300, 30, window=self.timestamp_to_date_switch)

        self.date_or_timestamp_label = CTkLabel(text='Votre date (format JJ/MM/AAAA)', bg_color='gray12')
        self.canvas.create_window(200, 60, window=self.date_or_timestamp_label)

        self.date_or_timestamp_input = CTkEntry()
        self.canvas.create_window(200, 100, window=self.date_or_timestamp_input)

    def valid(self):
        value = self.date_or_timestamp_input.get()

        try:
            if self.date_var.get() == 'datetotimestamp':
                result = time.mktime(datetime.datetime.strptime(value, "%d/%m/%Y").timetuple())

            else:
                date = str(datetime.datetime.fromtimestamp(float(value)))
                date = date.replace('-', '/')
                dates = date.split(' ')
                date = ''.join(dates[0])
                dates = date.split('/')
                result = f'{dates[2]}/{dates[1]}/{dates[0]}'

            return result

        except:
            create_error()

    def change_text_date_timestamp(self, text):
        self.date_or_timestamp_label.configure(text=text)
