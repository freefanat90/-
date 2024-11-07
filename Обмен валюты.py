import requests
import json
import pprint
from tkinter import *
from tkinter import messagebox as mb

window = Tk()
window.title('Курсы валют')
window.geometry(360x180)

Label(text='Введите код валюты').pack(padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)

Button(text='Получить курс обмена к долллару', command=exchage).pack(padx=10, pady=10)

window.mainloop()








#result = requests.get('http://open.er-api.com/v6/latest/USD')
#data = json.loads(result.text)
#p = pprint.PrettyPrinter(indent=4)
#p.pprint(data)