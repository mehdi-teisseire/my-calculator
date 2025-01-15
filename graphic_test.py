import customtkinter

class OperatorFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)



class NumbersFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("MyCaLcuLatoR")
        self.geometry("400x400")

        self.operator_frame = OperatorFrame(self)
        self.operator_frame.grid(row = 1, column = 4, columnspan = 3, rowspan = 3, sticky="nes")

        self.numbers_frame = NumbersFrame(self)
        self.numbers_frame.grid(row = 1, column = 0, rowspan = 3, sticky="nws")

        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)
        self.columnconfigure(3, weight = 1)
        self.columnconfigure(4, weight = 1)
        
        self.rowconfigure(0, weight = 3)
        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)
        self.rowconfigure(3, weight = 1)


app = App()
app.mainloop()