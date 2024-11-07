import requests
import json
import pprint
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

def exchange():
    code = combobox.get()

    if code:
        try:
            response = requests.get('http://open.er-api.com/v6/latest/USD')
            response.raise_for_status()
            data = response.json()
            if code in data ['rates']:
                exchange_rates = data['rates'][code]
                mb.showinfo('Курс обмена', f'Курс: {exchange_rates:.2f} {code} за один $')
            else:
                mb.showerror('Ошибка', f'Валюта {code} не найдена')
        except Exception as e:
            mb.showerror('Ошибка', f'Произошла ошибка: {e}.')
    else:
        mb.showwarning('Внимание', f'Введите код валюты!')



window = Tk()
window.title('Курсы валют')
window.geometry('360x180')

Label(text='Выберете код валюты').pack(padx=10, pady=10)

cur = ['RUB', 'EUR', 'GBP', 'JPY', 'CNY', 'KZT', 'UZS', 'CHF', 'AED', 'CAD']
combobox = ttk.Combobox(values=cur)
combobox.pack(padx=10, pady=10)

#entry = Entry()
#entry.pack(padx=10, pady=10)

Button(text='Получить курс обмена к доллару', command=exchange).pack(padx=10, pady=10)

window.mainloop()








#result = requests.get('http://open.er-api.com/v6/latest/USD')
#data = json.loads(result.text)
#p = pprint.PrettyPrinter(indent=4)
#p.pprint(data)