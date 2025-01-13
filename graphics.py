import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("MyCaLcuLatoR")
        self.geometry("400x800")

        self.button = customtkinter.CTkButton(self, text="=", command=self.button_callbck)
        self.button.grid(row= 3, column = 3)
        
        for i in range(0,9):
            self.button = customtkinter.CTkButton(self, text=i+1, command=self.button_callbck)
            self.button.grid(row = i//3, column = i%3) #i%3 = 0 1 2 0 1 2 0 1 2      #i//3 = 0 0 0 1 1 1 2 2 2

    def button_callbck(self):
        print(self)

app = App()
app.mainloop()

