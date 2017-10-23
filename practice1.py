import tkinter as tk
lf = ("Verdana", 12)
class anpr(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        frame = StartPage(container, self)
        self.frames[StartPage] = frame

        frame.grid(row = 0, column = 0, sticky = "nsew")
        self.show_frame(StartPage)

        def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkrasie()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "welcome to bangla ANPR", font = lf)
        label.pack(pady = 10, padx = 10)

app = anpr()
app.mainloop()





