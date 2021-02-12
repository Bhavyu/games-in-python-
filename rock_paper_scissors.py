import random
import tkinter as tk
stats=[]
def get_winner(call):
    global stats
    if random.random() <= (1 / 3):
        throw = "rock"
    elif (1 / 3) < random.random() <= (2 / 3):
        throw="scissors"
    else:
        throw = "paper"
    if(throw == "rock" and call == "paper") or (throw == "paper" and call == "scissors") or (throw == "scissors" and call == "rock"):
        stats.append('W')
        res="YOU WON!"
    elif throw == call:
        stats.append('D')
        res="its draw!"
    else:
        stats.append('L')
        res="YOU LOST!"
    global o
    o.config(text="Computer did  "+ throw +"\n "+ res)

def pass_s():
    get_winner("scissors")

def pass_r():
    get_winner("rock")

def pass_p():
    get_winner("paper")
window =tk.Tk()
s=tk.Button(window,text="scissors", bg="#ff9999",padx=10,pady=5,command=pass_s,width=20)
r=tk.Button(window,text="rock", bg="#ff8080",padx=10,pady=5,command=pass_r,width=20)
p=tk.Button(window,text="paper", bg="#ff1245",padx=10,pady=5,command=pass_p,width=20)

o=tk.Label(window,width=20,fg="red",bg="white",text="Whats your call?")

s.pack(side="left")
r.pack(side="left")
p.pack(side="left")
o.pack(side="right")

window.mainloop()
for i in stats:
    print(i, end="  ")
if stats.count('L')> stats.count('W'):
    res="\n you loose the series..."
if stats.count('L')== stats.count('W'):
    res="\n series ended with draw..."
else:
    res="\n you win the series..."
print(res)

        
