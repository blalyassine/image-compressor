from tkinter import font
import PIL
from PIL import  Image
from  tkinter import *
from tkinter.filedialog import *

def ImageCompressor():
    file_patch=askopenfilename()
    img=PIL.Image.open(file_patch)
    myHeight,myWidth=img.size   
    img=img.resize((myHeight,myWidth), PIL.Image.ANTIALIAS)
    save_path=asksaveasfilename()
    img.save(save_path + "Comp.png",quality=50)
    
root=Tk()
root.title("image compressor")
root.geometry("300x300")


Button(root,text="select Image",
       font="Helvetic 16 bold",
       bg="black",fg="white",
       command= ImageCompressor).place(relx=.5,rely=.5, anchor=CENTER)



root.mainloop()
