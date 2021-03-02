from tkinter import *

def call(r,c):
    global player
    if player=='x' and s[r][c]==0 and state==False:
        m[r][c].configure(text="X",bg="yellow",fg="red")
        s[r][c]='x'
        player='o'
    if player=='o' and s[r][c]==0 and state==False:
        m[r][c].configure(text="O",bg="green",fg="powder blue")
        s[r][c]='o'
        player='x'

    winner()

def winner():
    global state
    for i in range(3):
        if s[i][0]==s[i][1]==s[i][2]!= 0:
            m[i][0].configure(bg="black")
            m[i][1].configure(bg="black")
            m[i][2].configure(bg="black")         
            state= True
    for i in range(3):
        if s[0][i]==s[1][i]==s[2][i]!=0:
            m[0][i].configure(bg="black")
            m[1][i].configure(bg="black")
            m[2][i].configure(bg="black")
            state= True 
    if s[0][0]==s[1][1]==s[2][2]!=0:
        m[0][0].configure(bg="black")
        m[1][1].configure(bg="black")
        m[2][2].configure(bg="black")
        state= True
    if s[2][0]==s[1][1]==s[0][2]!=0:
        m[2][0].configure(bg="black")
        m[1][1].configure(bg="black")
        m[0][2].configure(bg="black")
        state= True

root=Tk()
f=Frame()

m=[[0,0,0],
   [0,0,0],
   [0,0,0]]

s=[[0,0,0],
   [0,0,0],
   [0,0,0]]

for i in range(3):
    for j in range(3):
        m[i][j]=Button(f,width=20,height=10,bg='blue',command=lambda r=i,c=j:call(r,c))
        m[i][j].grid(row=i,column=j)
        
f.grid(row=0,column=0)
player='x'
state=False

root.mainloop()


