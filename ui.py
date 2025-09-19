import tkinter as tk
from tkinter import ttk, messagebox
from converter import get_exchange_rate

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Moedas")
        self.root.geometry('400x250')

        self.build_interface()

    def build_interface(self):
        tk.Label(self.root, text='Valor: ').pack()
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack()

        tk.Label(self.root, text='De (Moeda): ').pack()
        self.from_currency = tk.Entry(self.root)
        self.from_currency.pack()

        tk.Label(self.root, text='Para (Moeda): ').pack()
        self.to_currency = tk.Entry(self.root)
        self.to_currency.pack()

        tk.Button(self.root, text='Converter', command=self.convert).pack(pady=10)
        self.result_label = tk.Label(self.root, text='')
        self.result_label.pack()

    def convert(self):
        try:
            amount = float(self.amount_entry.get())
            from_cur = self.from_currency.get().upper()
            to_cur = self.to_currency.get().upper()
            rate = get_exchange_rate(from_cur, to_cur)
            result = amount * rate
            self.result_label.config(text=f'{amount: .2f} {from_cur} = {result: .2f} {to_cur}')
        
        except Exception as e:
            messagebox.showerror("Erro", str(e))