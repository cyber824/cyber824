import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Sample Calculator")

        self.display = tk.Entry(master, width=16, font=('Arial', 24), borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        row = 1
        col = 0

        for button in buttons:
            command = lambda b=button: self.on_button_click(b)
            tk.Button(self.master, text=button, width=5, height=2, font=('Arial', 18), command=command).grid(row=row, column=col)

            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, button):
        if button == 'C':
            self.display.delete(0, tk.END)
        elif button == '=':
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, 'Error')
        else:
            current = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, current + button)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

