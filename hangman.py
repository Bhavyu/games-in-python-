#HANGMAN GAME
#Q.1 IF OCCURENCES IS MORE
#Q.2 IF LETTER IS REPEATE 

l=['a','l','p','h','a','b','e','t','s']
length=len(l)
l2= ['_']*length
#print(len(l2))
#print(l)
t=length

while(t>0):
    if l==l2:
        print("you won!!!")
        exit()
    else:
        x=input('enter the character: ')
        if x in l:
            n=l.count(x)
            if n == 1:
                i=l.index(x)
                l2[i]=x
                #s1=l2[:i]
                #le1=len(s1)
                #s2=l2[i+1:]
                #le2=len(s2)
                #print("_ "*le1," ",l2[i],"_ "*le2)
                print(l2)
            if n>1:
                i=l.index(x)
                b=l.index(x,i+1)
                l2[i]=x
                l2[b]=x
                print(l2)
                n=n-1
        else:
            print('absent, now you left with '+str(t-1)+' chances ')
            print('you missed one chance...')
    t=t-1
if t == 0:
    print("you LOSE!!!!!")
    print('The word is',l)
    
