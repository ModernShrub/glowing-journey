from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.title("khiue")
root.geometry("600x400")

root.configure(background = "gold")

img=ImageTk.PhotoImage(Image.open("pokecard.jpg"))
img1=ImageTk.PhotoImage(Image.open("pokecard1.jpg"))
img2=ImageTk.PhotoImage(Image.open("pokecard2.jpg"))
img3=ImageTk.PhotoImage(Image.open("pokecard3.jpg"))
img4=ImageTk.PhotoImage(Image.open("pokecard4.jpg"))
img5=ImageTk.PhotoImage(Image.open("pokecard5.jpg"))
img6=ImageTk.PhotoImage(Image.open("pokecard6.jpg"))
img7=ImageTk.PhotoImage(Image.open("pokecard7.jpg"))
img8=ImageTk.PhotoImage(Image.open("pokecard8.jpg"))
img9=ImageTk.PhotoImage(Image.open("pokecard9.jpg"))
img0=ImageTk.PhotoImage(Image.open("pokecard0.jpg"))
img11=ImageTk.PhotoImage(Image.open("pokecard11.jpg"))

player1label = Label(root, text="Player 1", bg="cornflower blue",fg="white")
player1label.place(relx = 0.1,rely=0.3,anchor=CENTER)

player2label = Label(root, text="Player 2", bg="cornflower blue",fg="white")
player2label.place(relx = 0.9,rely=0.3,anchor=CENTER)

player1scorelabel = Label(root, text="Player 1 score : ", bg="cornflower blue",fg="white")
player1scorelabel.place(relx = 0.1,rely=0.4,anchor=CENTER)

player2scorelabel = Label(root, text="Player 1 score : ", bg="cornflower blue",fg="white")
player2scorelabel.place(relx = 0.9,rely=0.4,anchor=CENTER)

pokecardlabellabel = Label(root, bg="turquoise",fg="white")
pokecardlabellabel.place(relx = 0.5,rely=0.5,anchor=CENTER)

pokemonlist = ["Octillery", "Chimchar", "Embroar", "Mienshao", "Houndoom", "Tyranitar", "Empoleon", "Zeraora", "Articuno", "Cresselia", "Castform", "Zekrom"]

powerlist = [110, 50, 180, 90, 130, 230, 210, 210, 210, 120, 70, 130]

imglist = [img, img0, img1, img2, img3, img4, img5, img6, img7, img8, img9, img11]

player1score = 0

def player1() :
    global player1score
    rngno = random.randint(0,11)
    pokecardlabellabel["image"] = imglist[rngno]
    player1score = player1score + powerlist[rngno]
    player1scorelabel['text'] = str(player1score)
    
player2score = 0
def player2() : 
    global player2score
    rngno1 = random.randint(0,11)
    pokecardlabellabel["image"] = imglist[rngno1]
    player2score = player2score + powerlist[rngno1]
    player2scorelabel['text'] = str(player2score)
    
btnimg = ImageTk.PhotoImage(Image.open("btnimg.jpg"))

player1btn = Button(root, image=btnimg,command=player1)
player1btn.place(relx=0.1,rely=0.6,anchor=CENTER)

player2btn = Button(root, image=btnimg,command=player2)
player2btn.place(relx=0.9,rely=0.6,anchor=CENTER)

root.mainloop()
