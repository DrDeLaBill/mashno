import calendar
import datetime
from tkinter import *


class Calendar:
    def __init__(self):
        self.root = Tk()
        self.root.title('Calendar')
        self.days = []
        self.now = datetime.datetime.now()
        self.year = self.now.year
        self.month = self.now.month
        self.prew_button = None
        self.next_button = None
        self.info_label = None

    def initialize_buttons(self):
        self.prew_button = Button(self.root, text='<', command=self.prew)
        self.prew_button.grid(row=0, column=0, sticky='nsew')
        self.next_button = Button(self.root, text='>', command=self.next)
        self.next_button.grid(row=0, column=6, sticky='nsew')
        self.info_label = Label(self.root, text='0', width=1, height=1,
                           font=('Verdana', 16, 'bold'), fg='blue')
        self.info_label.grid(row=0, column=1, columnspan=5, sticky='nsew')

    def fill(self):
        self.info_label['text'] = calendar.month_name[self.month] + ', ' + str(self.year)
        month_days = calendar.monthrange(self.year, self.month)[1]
        if self.month == 1:
            prew_month_days = calendar.monthrange(self.year - 1, 12)[1]
        else:
            prew_month_days = calendar.monthrange(self.year, self.month - 1)[1]
        week_day = calendar.monthrange(self.year, self.month)[0]
        for n in range(month_days):
            self.days[n + week_day]['text'] = n + 1
            self.days[n + week_day]['fg'] = 'black'
            if self.year == self.now.year and self.month == self.now.month and n == self.now.day:
                self.days[n + week_day]['background'] = 'green'
            else:
                self.days[n + week_day]['background'] = 'lightgray'
        for n in range(week_day):
            self.days[week_day - n - 1]['text'] = prew_month_days - n
            self.days[week_day - n - 1]['fg'] = 'gray'
            self.days[week_day - n - 1]['background'] = '#f3f3f3'
        for n in range(6 * 7 - month_days - week_day):
            self.days[week_day + month_days + n]['text'] = n + 1
            self.days[week_day + month_days + n]['fg'] = 'gray'
            self.days[week_day + month_days + n]['background'] = '#f3f3f3'

    def prew(self):
        self.month -= 1
        if self.month == 0:
            self.month = 12
            self.year -= 1
        self.fill()

    def next(self):
        self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1
        self.fill()

    def run(self):
        for n in range(7):
            lbl = Label(self.root, text=calendar.day_abbr[n], width=1, height=1,
                        font=('Verdana', 10, 'normal'), fg='darkblue')
            lbl.grid(row=1, column=n, sticky='nsew')
        for row in range(6):
            for col in range(7):
                lbl = Label(self.root, text='0', width=4, height=2,
                            font=('Verdana', 16, 'bold'))
                lbl.grid(row=row + 2, column=col, sticky='nsew')
                self.days.append(lbl)
        self.fill()
        self.root.mainloop()


def main():
    calendar = Calendar()
    calendar.initialize_buttons()
    calendar.run()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# если бы вы знали как мне похуй, вы бы заплакали
