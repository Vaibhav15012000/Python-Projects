from tkinter import *
import tkinter.messagebox as tms
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os



if __name__ =='__main__':
    root=Tk()
    root.title("Dubeyji Ka Notepad")
    root.wm_iconbitmap("one.ico")
    root.geometry("400x400")
    

    #ADD TEXT AREA

    area=Text(root,font="lucida 13")
    file=None
    area.pack(fill=BOTH, expand=True)
    
    
    def newfile():
        global file
        root.title("Untitled_Notepad")
        file=None
        area.delete(1.0,END)           #deletes all value in text area(start point,end point)

    def savefile():
        global file
        if file==None:
            file=asksaveasfilename(initialfile="untitle.txt",
            defaultextension=".txt",
                                filetypes=[("All Files", "*.*"),
                                        ("Text Documents", "*.txt")])
        
            if file=="":
                file=NONE
            else:
                f=open(file,"w")
                f.write(area.get(1.0,END))
                f.close()
                root.title(os.pat.basename(file)+"-Notepad") 

        else:
            f=open(file,"w")
            f.write(area.get(1.0,END))
            f.close()
         


    def openfile():
        global file
        file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                    ("Text Documents", "*.txt")])
         
        if file=="":
            file=None
        else:
            root.title(os.path.basename(file)+ "-Notepad")
            area.delete(1.0,END)
            f=open(file,"r")
            area.insert(1.0,f.read())
            f.close()
   
    def exitfile():
        root.destroy()

    def cut():
        area.event_generate("<<Cut>>")

    def copy():
        area.event_generate("<<Copy>>")       

    def paste():
        area.event_generate("<<Paste>>")

    def about():
        tms.showinfo("About",message="This is a notepad 1.0.0. \n Made by Daibhav Dubey")        

    
    
    #MENU BAR
    mnu_bar=Menu(root)
    #file menu Starts
    file_menu=Menu(mnu_bar,tearoff=0)

    #TO open new File
    file_menu.add_command(label="New",command=newfile)

    #To open already created txt file:

    file_menu.add_command(label="Open",command=openfile)

    #TO save the current file

    file_menu.add_command(label="Save",command=savefile)
    file_menu.add_separator()

    file_menu.add_command(label="Exit",command=exitfile)

    mnu_bar.add_cascade(label="File",menu=file_menu)
    
  
    #file menu Ends

    #Edit menu Starts
    edit_mnu=Menu(mnu_bar,tearoff=0)

    #to give cut,copy,paste

    edit_mnu.add_command(label="Cut",command=cut)
    edit_mnu.add_command(label="Copy",command=copy)
    edit_mnu.add_command(label="Paste",command=paste)

    mnu_bar.add_cascade(label="Edit",menu=edit_mnu)

    
    

    #Edit menu Ends

    #HElp menu starts

    help_mnu=Menu(mnu_bar,tearoff=0)
    help_mnu.add_command(label="About",command=about)
    mnu_bar.add_cascade(label="Help",menu=help_mnu)
  
    root.configure(menu=mnu_bar)


    #adding scrollbar

    scroll_bar=Scrollbar(area)
    scroll_bar.pack(side=RIGHT,fill=Y)
    scroll_bar.config(command=area.yview)
    area.config(yscrollcommand=scroll_bar.set)












   











    root.mainloop() 