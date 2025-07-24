import tkinter as tk
from tkinter import Toplevel

def story1(win):
    def final(tl: Toplevel, name, sports, City, Playername, drinkname, snacks):

        text = f'''
        One day me and my friend {name} decided to play a {sports} game
        in {City}. 
        We wanted to watch {Playername}.
        We drank {drinkname} and also are some {snacks}.
        We really enjoyed! We are looking forward to go again and enjoy'''

        
        tk.Label(tl, text='Story:',  wraplength=tl.winfo_width()).place(x=160, y=310)
        tk.Label(tl, text=text,wraplength=tl.winfo_width()).place(x=0, y=330)
# Create the input window
    NewScreen = Toplevel(win, bg='yellow')
    NewScreen.title("A memorable day")
    NewScreen.geometry('500x500')

    tk.Label(NewScreen, text='Memorable Day').place(x=100, y=0)
    tk.Label(NewScreen, text='Name:').place(x=0, y=35)
    tk.Label(NewScreen, text='Enter a game:').place(x=0, y=70)
    tk.Label(NewScreen, text='Enter a city:').place(x=0, y=110)
    tk.Label(NewScreen, text='Enter the name of a player:').place(x=0, y=150)
    tk.Label(NewScreen, text='Enter the name of a drink:').place(x=0, y=190)
    tk.Label(NewScreen, text='Enter the name of a snack:').place(x=0, y=230)

    Name = tk.Entry(NewScreen, width=17).place(x=250, y=35)

    game = tk.Entry(NewScreen, width=17).place(x=250, y=70)
   
    city = tk.Entry(NewScreen, width=17).place(x=250, y=105)
    
    player = tk.Entry(NewScreen, width=17).place(x=250, y=150)
    
    drink = tk.Entry(NewScreen, width=17).place(x=250, y=190)
    
    snack = tk.Entry(NewScreen, width=17).place(x=250, y=220)
    
    SubmitButton = tk.Button(NewScreen, text="Submit", background="Blue", font=('Times', 12), command=lambda:final(NewScreen, Name.get(), game.get(), city.get(), player.get(), drink.get(), snack.get()))
    SubmitButton.place(x=150, y=270)

    exit_button = tk.Button(NewScreen,text="close", bg="Black", command=NewScreen.destroy).place(x=200, y=450)
    
    tk.Label(NewScreen, text='Memorable Day').place(x=100, y=0)
    tk.Label(NewScreen, text='Name:').place(x=0, y=35)
    tk.Label(NewScreen, text='Enter a game:').place(x=0, y=70)
    tk.Label(NewScreen, text='Enter a city:').place(x=0, y=110)
    tk.Label(NewScreen, text='Enter the name of a player:').place(x=0, y=150)
    tk.Label(NewScreen, text='Enter the name of a drink:').place(x=0, y=190)
    tk.Label(NewScreen, text='Enter the name of a snack:').place(x=0, y=230)
    Name = tk.Entry(NewScreen, width=17)
    Name.place(x=250, y=35)
    game = tk.Entry(NewScreen, width=17)
    game.place(x=250, y=70)
    city = tk.Entry(NewScreen, width=17)
    city.place(x=250, y=105)
    player = tk.Entry(NewScreen, width=17)
    player.place(x=250, y=150)
    drink = tk.Entry(NewScreen, width=17)
    drink.place(x=250, y=190)
    snack = tk.Entry(NewScreen, width=17)
    snack.place(x=250, y=220)
    SubmitButton = tk.Button(NewScreen, text="Submit", background="Blue", font=('Times', 12), command=lambda:final(NewScreen, Name.get(), game.get(), city.get(), player.get(), drink.get(), snack.get()))
    SubmitButton.place(x=150, y=270)
    NewScreen.mainloop()
def story2(win):
    def final(tl: Toplevel, profession, noun, feeling, emotion,verb):

        text = f'''
            I want to be this {profession} ans yes my name is {noun}. I'm feeling {feeling}
            super califragilistic and i don't care about {emotion} i have i'm striving for {verb}.
'''
        tk.Label(tl, text="Story: ", font = ("Times New Roman", 13), wraplength=tl.winfo_width()).place(x=160,y=310)
        tk.Label(tl, text=text, font = ("Times New Roman", 13), wraplength=tl.winfo_width()).place(x=0,y=330)

    Newscreen = Toplevel(win, bg='green')
    Newscreen.title("Ambitions")
    Newscreen.geometry("500x550")

    
    tk.Label(Newscreen, text='Ambition').place(x=100, y=0)
    tk.Label(Newscreen, text='Profession:').place(x=0, y=35)
    tk.Label(Newscreen, text='Enter a name:').place(x=0, y=70)
    tk.Label(Newscreen, text='how do you feel: ').place(x=0, y=110)
    tk.Label(Newscreen, text='enter your emotion: ').place(x=0, y=150)
    tk.Label(Newscreen, text='what is your purpose:').place(x=0, y=190)

    Profession = tk.Entry(Newscreen, width=17)
    Profession.place(x=250, y=35)
    Name = tk.Entry(Newscreen, width=17)
    Name.place(x=250, y=70)
    Feeling = tk.Entry(Newscreen, width=17)
    Feeling.place(x=250, y=105)
    Emotion = tk.Entry(Newscreen, width=17)
    Emotion.place(x=250, y=150)
    purpose = tk.Entry(Newscreen, width=17)
    purpose.place(x=250, y=190)
    
    SubmitButton = tk.Button(Newscreen, text="Submit", background="Blue", font=('Times', 12), command=lambda:final(Newscreen, Profession.get(), Name.get(), Feeling.get(), Emotion.get(), purpose.get()))
    SubmitButton.place(x=150, y=270)

    exit_button = tk.Button(Newscreen,text="close", bg="Black", command=Newscreen.destroy).place(x=200, y=450)
    

    Newscreen.mainloop()
def exit_program():
    screen.destroy()

screen = tk.Tk()
screen.title("Mad Libs Generator",)
screen.geometry("400x400")
screen.config(bg="pink")

tk.Label(screen, text = "Mad Libs Generator").place(x=100, y=20)

#creating the buttons

story1Button = tk.Button(screen, text = "A memorable, commable day", font = ("Times New Roman", 13),command=lambda: story1(screen), bg="Blue")

story1Button.place(x = 140, y = 90)

story2Button = tk.Button(screen, text = "Ambitions", font = ("Times New Roman", 13),command=lambda: story2(screen), bg = "Blue")
story2Button.place(x=150, y=150)

exit_button = tk.Button(screen, text="Exit", command=exit_program).place(x=150, y=350)

screen.update()
screen.mainloop()



