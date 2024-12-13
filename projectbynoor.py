from gtts import gTTS 
from playsound import playsound
from tkinter import*
root=Tk()
root.title("Text to Speach")
mylabel1=Label(root,text="Text to speach",font="Tahoma 10 bold").pack(pady=10)
mylabel2=Label(root,text="Enter your Text",font="Tahoma 10 bold").pack(padx=5,pady=20,side=LEFT,anchor="nw")
myentry=Entry(root,width=40)
myentry.pack(pady=20)
def myfunc():
    text1=myentry.get()
    myobj= gTTS(text=text1)
    myobj.save("f{text1}.mp3")
    playsound("f{text1}.mp3")

button1=Button(root,text="Play",command=myfunc).pack(pady=20,padx=10,side=LEFT,anchor="nw")
def close():
    root.destroy()
button2=Button(root,text="Exit",bg="red",command=close)
button2.pack(pady=20,padx=10,side=LEFT)
def deletetextbox():
    myentry.delete(0,'end')
button3=Button(root,text="Set",bg="blue",command=deletetextbox).pack(pady=20,padx=10,side=LEFT)
root.mainloop()