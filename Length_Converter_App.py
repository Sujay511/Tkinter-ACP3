from tkinter import *

root=Tk()
root.title("Length Converter App")
root.geometry("500x500")

frame=Frame(master=root,bg="white",height=70,width=70)
lbl=Label(frame,fg="black",text="Enter the length in inches")
entry=Entry(frame)



def length_conversion():
    try:
        global cm
        a=entry.get()
        b=float(a)
        cm=b*2.54
        print("The length in centimeters is:",cm)
    except ValueError:
        print("Please enter the length in integers!")


button=Button(text="Click to convert!",bg="light blue",command=length_conversion,relief=RAISED)
button.place(x=198,y=60)


frame.pack()
lbl.pack()
entry.pack()

root.mainloop()