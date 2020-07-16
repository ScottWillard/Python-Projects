import tkinter as tk

Rock = "Rock"
Paper = "Paper"
Scissors = "Scissors"


class GUI(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.Rock = tk.Button(self, text = Rock, fg = "red",
                              command = print("You chose " + Rock))
        self.Paper = tk.Button(self, text = Paper, fg = "green",
                               command = print("You chose " + Paper))
        self.Scissors = tk.Button(self, text = Paper, fg = "blue",
                                  command = print("You chose " + Scissors))

        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.Rock["text"] = Rock
        self.Rock["command"] = self.printRock
        self.Rock.pack(side = "left")

        self.Paper.pack(side = "bottom")
        self.Paper["text"] = Paper
        self.Paper["command"] = self.printPaper

        self.Scissors.pack(side = "right")
        self.Scissors["text"] = Scissors
        self.Scissors["command"] = self.printScissors

    def printRock(self):
        print(Rock)

    def printPaper(self):
        print(Paper)

    def printScissors(self):
        print(Scissors)


root = tk.Tk()
app = GUI(master = root)
app.mainloop()