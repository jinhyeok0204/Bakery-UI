import tkinter
from tkinter import *


class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        window.title("고객: " + self.name)
        window.geometry('350x200')
        Label(window, text="샌드위치(5000원)").grid(column=0, row=0)
        Label(window, text="케이크(20000원)").grid(column=0, row=1)

        self.sandwich = StringVar()
        sandwich_entry = Entry(window, width=10, textvariable=self.sandwich).grid(column=1, row=0)
        self.cake = StringVar()
        cake_entry = Entry(window, width=10, textvariable=self.cake).grid(column=1, row=1)
        button = Button(window, text="주문하기", command=self.send_order).grid(column=0, row=2)

    def send_order(self):
        if "1" <= self.sandwich.get() <= "9" and "1"<= self.cake.get() <= "9":
            order_text = self.name + ": 샌드위치 (5000원) " + str(self.sandwich.get()) + "개, 케이크 (20000원) " + str(self.cake.get()) + "개"
        elif "1" <= self.sandwich.get() <= "9" and ("1" > self.cake.get() or self.cake.get() > "9"):
            order_text = self.name + ": 샌드위치 (5000원) " + str(self.sandwich.get()) + "개"
        elif "1" <= self.cake.get() <= "9" and ("1" > self.sandwich.get() or self.sandwich.get() > "9"):
            order_text = self.name + " : 케이크 (20000원) " + str(self.cake.get()) + "개"
        self.bakeryView.add_order(order_text)


if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
