import tkinter as tk
import os
from tkinter.filedialog import askdirectory
import subprocess
import shlex


class allexefirewall_blockpy(tk.Frame):
    def __init__(self,master=None):
       # master.minsize(width=300, height=200)
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label=tk.Label(self,text='Please browse for the folder you want to block')
        self.label.pack(side="top")
        self.label = tk.Label(self, text='v 0.3')
        self.label.pack(side="bottom",expand=1)
        self.brs=tk.Button(self)
        self.brs["text"]="Browse"
        self.brs["command"]=self.browse
        self.brs.pack(side = "left",expand=1)


    def browse(self):
        filename= askdirectory()
        #print (filename)
        for exe in os.listdir(filename):
            if exe.endswith(".exe"):
             executabile=exe
             print (executabile)
             command='netsh advfirewall firewall add rule name="Block {}" dir=in action=block program="{}" enable=yes'.format(executabile,executabile)
             subprocess.call(command,shell=True)



root=tk.Tk()
app=allexefirewall_blockpy(master=root)
app.master.title("All Exe Firewall Blockpy")
app.master.maxsize(300,200)
app.mainloop()

