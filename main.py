from tkinter import *
window = Tk()
window.title("Tic Tac Toa")

def Button_click(bu):
    pass

bu1 = Button(window, text="", font=("courrier", 15), height=3, width=6, bg="SystemButtonFace", command=lambda:Button_click(bu1))
bu2 = Button(window, text="", font=("courrier", 15), height=3, width=6, bg="SystemButtonFace", command=lambda:Button_click(bu2))
bu3 = Button(window, text="", font=("courrier", 15), height=3, width=6, bg="SystemButtonFace", command=lambda:Button_click(bu3))

bu4 = Button(window, text="", font=("courrier", 15), height=3, width=6, bg="SystemButtonFace", command=lambda:Button_click(bu4))
bu5 = Button(window, text="", font=("courrier", 15), height=3, width=6, bg="SystemButtonFace", command=lambda:Button_click(bu5))
bu6 = Button(window, text="", font=("courrier", 15), height=3, width=6, bg="SystemButtonFace", command=lambda:Button_click(bu6))

bu7 = Button(window, text="", font=("courrier", 15), height=3, width=6, bg="SystemButtonFace", command=lambda:Button_click(bu7))
bu8 = Button(window, text="", font=("courrier", 15), height=3, width=6, bg="SystemButtonFace", command=lambda:Button_click(bu8))
bu9 = Button(window, text="", font=("courrier", 15), height=3, width=6, bg="SystemButtonFace", command=lambda:Button_click(bu9))

bu1.grid(row=0, column=0)
bu2.grid(row=0, column=1)
bu3.grid(row=0, column=2)

bu4.grid(row=1, column=0)
bu5.grid(row=1, column=1)
bu6.grid(row=1, column=2)

bu7.grid(row=2, column=0)
bu8.grid(row=2, column=1)
bu9.grid(row=2, column=2)

window.mainloop()