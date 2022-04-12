import sys
sys.path.append('../')

import tkinter as tk
import tkinter.font as tkFont 
from model.Lixeira import Lixeira

class LixeiraView:
    def __init__(self, window):
        self.lixeiraModel = None
        
        self.window = window
        #setting title
        self.window.title("Lixeira")
        #setting window size
        width=600
        height=500
        screenwidth = self.window.winfo_screenwidth()
        screenheight = self.window.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.window.geometry(alignstr)
        self.window.resizable(width=False, height=False)

        self.capacidadeLabel=tk.Label(self.window, name = "capacidadeLabel")
        self.capacidadeLabel.bind('<Enter>',self.bindCreateLixeirasEvent)
        self.capacidadeLabel["font"] = tkFont.Font(family='Times',size=10)
        self.capacidadeLabel["fg"] = "#333333"
        self.capacidadeLabel["justify"] = "center"
        self.capacidadeLabel["text"] = "Capacidade"
        self.capacidadeLabel.place(x=10,y=460,width=70,height=25)

        self.capacidadeInput=tk.Entry(self.window, name = "capacidadeInput")
        self.capacidadeInput.bind('<Enter>',self.bindCreateLixeirasEvent)
        self.capacidadeInput["bg"] = "#f8f8f8"
        self.capacidadeInput["borderwidth"] = "1px"
        self.capacidadeInput["font"] = tkFont.Font(family='Times',size=10)
        self.capacidadeInput["fg"] = "#333333"
        self.capacidadeInput["justify"] = "center"
        self.capacidadeInput["text"] = 0
        self.capacidadeInput.place(x=150,y=460,width=50,height=25)

        # Button that creates Lixeiras
        self.btnCreateLixeiras = tk.Button(self.window, name = "btnCreateLixeiras")
        self.btnCreateLixeiras.bind('<Enter>',self.bindCreateLixeirasEvent)
        self.btnCreateLixeiras["bg"] = "#efefef"
        self.btnCreateLixeiras["font"] = tkFont.Font(family='Times',size=10)
        self.btnCreateLixeiras["fg"] = "#000000"
        self.btnCreateLixeiras["justify"] = "center"
        self.btnCreateLixeiras["text"] = "Add Lixeira"
        self.btnCreateLixeiras.place(x=290,y=460,width=75,height=25)
        self.btnCreateLixeiras["command"] = self.btnCreateLixeiras_command
    
    def createLixeira(self):
        capacidade = int(self.capacidadeInput.get())
        self.lixeiraModel = Lixeira(capacidade)
        
        self.window.title("Lixeira - IP: " + str(self.lixeiraModel.getIP()))
        
        self.addButton=tk.Button(self.window)
        self.addButton.bind('<Enter>',self.bindAddButton)
        self.addButton.bind('<Leave>',self.bindAddButton)
        self.addButton.bind('<Button-1>',self.bindAddButton)
        self.addButton["bg"] = "#efefef"
        self.addButton["font"] = tkFont.Font(family='Times',size=10)
        self.addButton["fg"] = "#000000"
        self.addButton["justify"] = "center"
        self.addButton["text"] = "Adicionar Lixo"
        self.addButton.place(x=120,y=60,width=150,height=25)
        self.addButton["command"] = self.addButton_command

        self.removeButton=tk.Button(self.window)
        self.removeButton.bind('<Enter>',self.bindRemoveButton)
        self.removeButton.bind('<Leave>',self.bindRemoveButton)
        self.removeButton.bind('<Button-1>',self.bindRemoveButton)
        self.removeButton["bg"] = "#efefef"
        self.removeButton["font"] = tkFont.Font(family='Times',size=10)
        self.removeButton["fg"] = "#000000"
        self.removeButton["justify"] = "center"
        self.removeButton["text"] = "Remove Lixo"
        self.removeButton.place(x=120,y=100,width=150,height=25)
        self.removeButton["command"] = self.removeButton_command

        self.blockButton=tk.Button(self.window)
        self.blockButton.bind('<Enter>',self.bindBlockButton)
        self.blockButton.bind('<Leave>',self.bindBlockButton)
        self.blockButton.bind('<Button-1>',self.bindBlockButton)
        self.blockButton["bg"] = "#efefef"
        self.blockButton["font"] = tkFont.Font(family='Times',size=10)
        self.blockButton["fg"] = "#000000"
        self.blockButton["justify"] = "center"
        self.blockButton["text"] = "Bloquear"
        self.blockButton.place(x=120,y=140,width=150,height=25)
        self.blockButton["command"] = self.blockButton_command

        self.percentageLabel=tk.Label(self.window)
        self.percentageLabel["font"] = tkFont.Font(family='Times',size=10)
        self.percentageLabel["fg"] = "#333333"
        self.percentageLabel["justify"] = "center"
        self.percentageLabel["text"] = str(self.lixeiraModel.getPercentage() * 100) + " %" + " (" + str(self.lixeiraModel.getContent()) + " de " + str(self.lixeiraModel.getCapacity()) + ")"
        self.percentageLabel.place(x=320,y=80,width=85,height=25)

        self.ipLabel=tk.Label(self.window)
        self.ipLabel["font"] = tkFont.Font(family='Times',size=10)
        self.ipLabel["fg"] = "#333333"
        self.ipLabel["justify"] = "center"
        self.ipLabel["text"] = "127.0.0.1"
        self.ipLabel.place(x=320,y=130,width=70,height=25)

        # else:
        #     print('Insira um Numero')

    def btnCreateLixeiras_command(self):      
        self.createLixeira()

    def addButton_command(self):
        print('Add Lixo - ', self.lixeiraModel.toString())
        self.lixeiraModel.insertLixo()
        self.fetchLixerira()

    def removeButton_command(self):
        print('Remove Lixo - ', self.lixeiraModel.toString())
        self.lixeiraModel.removeLixo()
        self.fetchLixerira()

    def blockButton_command(self):
        if self.lixeiraModel.isLocked():
            print('Unlock Lixeira - ', self.lixeiraModel.toString())
            self.lixeiraModel.unlock()
            self.fetchLixerira()
        else:
            print('Lock Lixeira - ', self.lixeiraModel.toString())
            self.lixeiraModel.lock()
            self.fetchLixerira()

    def bindAddButton(self, event):
        if self.lixeiraModel.isLocked() or self.lixeiraModel.getPercentage() >= 1: self.addButton['state'] = 'disabled'
        elif not self.lixeiraModel.isLocked() and self.lixeiraModel.getPercentage() < 1: self.addButton['state'] = 'normal'
        
    def bindRemoveButton(self, event):
        if self.lixeiraModel.getContent() == 0 or self.lixeiraModel.isLocked() : self.removeButton['state'] = 'disabled'
        elif self.lixeiraModel.getContent() > 0 or not self.lixeiraModel.isLocked() : self.removeButton['state'] = 'normal'
        else : self.removeButton['state'] = 'normal'
    
    def bindBlockButton(self, event):
        if self.lixeiraModel.isLocked() : self.blockButton['text'] = 'Desbloquear'
        else : self.blockButton['text'] = 'Bloquear'

    def bindCreateLixeirasEvent(self,event):
        if self.capacidadeInput.get() == '': self.btnCreateLixeiras['state'] = 'disabled'
        elif self.capacidadeInput.get() != '': self.btnCreateLixeiras['state'] = 'normal'
        elif self.lixeiraModel != None: event.widget.place_forget()

    def fetchLixerira(self):
        self.percentageLabel["text"] = str(self.lixeiraModel.getPercentage() * 100) + " %" + " (" + str(self.lixeiraModel.getContent()) + " de " + str(self.lixeiraModel.getCapacity()) + ")"

if __name__ == "__main__":
    window = tk.Tk()
    app = LixeiraView(window)
    window.mainloop()
