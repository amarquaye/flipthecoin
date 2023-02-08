"""
An interactive game which allows you to guess whether a coin will be flipped to display heads or tails
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER


class FlipTheCoin(toga.App):

    def startup(self):
        
        main_box = toga.Box(style=Pack(direction=COLUMN, alignment=CENTER, flex=1))

        box1 = toga.Box(style=Pack(padding=10, flex=1))
        self.lab1 = toga.Label("Welcome th Flip The Coin with Jesse 😎", style=Pack(alignment=CENTER))

        box1.add(self.lab1)

        box2 = toga.Box(style=Pack(padding=10, flex=1, direction=COLUMN))
        self.lab2 = toga.Label("Will the coin face a head or a tails?")
        self.lab3 = toga.Label("If you think it's a heads enter H or heads and T for tails")

        box2.add(self.lab2,self.lab3)

        box3 = toga.Box(style=Pack(padding=10, direction=ROW, flex=1))
        self.lab4 = toga.Label("H or T", style=Pack(padding=(0,0,0,5)))
        self.text1 = toga.TextInput(style=Pack(padding=(0,0,0,5)))

        box3.add(self.lab4,self.text1)

        box4 = toga.Box(style=Pack(padding=10, flex=1))

        but1 =toga.Button("Flip", style=Pack(padding=(10,0,0.5,0.5)))
        box4.add(but1)



        main_box.add(box1,box2,box3,box4)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return FlipTheCoin()
