from tkinter import *
import random

def click0():
    answer = ''
    choices = ["ROCK", "PAPER", "SCISSOR"]
    player = "ROCK"
    computer = random.choice(choices)
    if computer == player:
        answer = "it is a draw "+player+" = "+computer
    elif computer == "SCISSOR":
        answer = "YOU WON " + computer + "<" + player
    else:
        answer = "YOU LOST "+ computer+">"+ player

    returnAnswer(answer)

def click1():
    answer = ""
    choices = ["ROCK", "PAPER", "SCISSOR"]
    player = "PAPER"
    computer = random.choice(choices)
    if computer == player:
        answer = "it is a draw "+player+" = "+computer
    elif computer == "ROCK":
        answer = "YOU WON " + computer + "<" + player
    else:
        answer = "YOU LOST " + computer+ ">" + player

    returnAnswer(answer)
def click2():
    answer = ""
    choices = ["ROCK", "PAPER", "SCISSOR"]
    player = "SCISSOR"
    computer = random.choice(choices)
    if computer == player:
        answer = "it is a draw "+player+" = "+computer
    elif computer == "PAPER":
        answer = "YOU WON " + computer + "<" + player
    else:
        answer = "YOU LOST " + computer+ ">" + player

    returnAnswer(answer)


window = Tk()
window.title("Game  Rock, Paper, Scissors")
photo0 = PhotoImage(file='rock.png')
photo1 = PhotoImage(file='paper.png')
photo2 = PhotoImage(file='scissors.png')
frame = Frame(window,relief=RAISED)

frame.pack(side=BOTTOM)

Button(frame,text="ROCK",command=click0,font=("Consolas", 25),image=photo0).pack(side=LEFT)
Button(frame,text="PAPER",command=click1,font=("Consolas", 25),image=photo1).pack(side=LEFT)
Button(frame,text="SCISSORS",command=click2,font=("Consolas", 25),image=photo2).pack(side=LEFT)
etykieta = Label(window)
labels = []
def returnAnswer(answer):
    # utworzenie nowego Label
    new_label = Label(window, text=answer)
    new_label.pack()

    # dodanie nowego Label do listy
    labels.append(new_label)

    # ukrycie wszystkich Labeli oprócz ostatniego
    for label in labels[:-1]:
        label.pack_forget()

window.mainloop()
