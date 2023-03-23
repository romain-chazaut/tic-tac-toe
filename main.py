from tkinter import *
window = Tk()
window.title("Tic Tac Toa")
from tkinter import messagebox

def Button_click(bu):
    pass

bu1 = Button(window, text="", font=("courrier", 30), height=3, width=7, bg="SystemButtonFace", command=lambda:Button_click(bu1))
bu2 = Button(window, text="", font=("courrier", 30), height=3, width=7, bg="SystemButtonFace", command=lambda:Button_click(bu2))
bu3 = Button(window, text="", font=("courrier", 30), height=3, width=7, bg="SystemButtonFace", command=lambda:Button_click(bu3))

bu4 = Button(window, text="", font=("courrier", 30), height=3, width=7, bg="SystemButtonFace", command=lambda:Button_click(bu4))
bu5 = Button(window, text="", font=("courrier", 30), height=3, width=7, bg="SystemButtonFace", command=lambda:Button_click(bu5))
bu6 = Button(window, text="", font=("courrier", 30), height=3, width=7, bg="SystemButtonFace", command=lambda:Button_click(bu6))

bu7 = Button(window, text="", font=("courrier", 30), height=3, width=7, bg="SystemButtonFace", command=lambda:Button_click(bu7))
bu8 = Button(window, text="", font=("courrier", 30), height=3, width=7, bg="SystemButtonFace", command=lambda:Button_click(bu8))
bu9 = Button(window, text="", font=("courrier", 30), height=3, width=7, bg="SystemButtonFace", command=lambda:Button_click(bu9))

bu1.grid(row=0, column=0)
bu2.grid(row=0, column=1)
bu3.grid(row=0, column=2)

bu4.grid(row=1, column=0)
bu5.grid(row=1, column=1)
bu6.grid(row=1, column=2)

bu7.grid(row=2, column=0)
bu8.grid(row=2, column=1)
bu9.grid(row=2, column=2)

player_turn = True  

def Button_click(bu):
    global player_turn

    if bu["text"] == "" and player_turn:
        bu["text"] = "X"
        player_turn = not player_turn
    elif bu["text"] == "" and not player_turn:
        bu["text"] = "O"
        player_turn = not player_turn

    check_winner()

def check_winner():
    winner = None
    winning_combinations = [
        [bu1, bu2, bu3],
        [bu4, bu5, bu6],
        [bu7, bu8, bu9],
        [bu1, bu4, bu7],
        [bu2, bu5, bu8],
        [bu3, bu6, bu9],
        [bu1, bu5, bu9],
        [bu3, bu5, bu7]
    ]

    for combination in winning_combinations:
        if combination[0]["text"] == combination[1]["text"] == combination[2]["text"] != "":
            winner = combination[0]["text"]
            break

    if winner:
        messagebox.showinfo("Tic Tac Toe", f"Le joueur {winner} a gagné !")
        window.quit()

    else:
        is_full = True
        for button in [bu1, bu2, bu3, bu4, bu5, bu6, bu7, bu8, bu9]:
            if button["text"] == "":
                is_full = False
                break

        if is_full:
            messagebox.showinfo("Tic Tac Toe", "Match nul !")
            window.quit()



window.mainloop()
