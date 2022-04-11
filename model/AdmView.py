import sys
sys.path.append('../')

import tkinter as tk
import tkinter.font as tkFont 
from model.Lixeira import Lixeira
from model.Adm import Administrador

class View:
    def __init__(self, window):
        self.window = window
        self.lixeiras = []; self.index = 0
        self.adm = Administrador(85063990096, 'admadmadm')
        
        # Variables to control itens placement
        self.widthButton = 55; self.heightButton = 25;
        self.xImg = 70; self.yImg = 40; self.widthImg = 106; self.heightImg = 84;
        self.xAddButton = 10; self.yAddButton = 40;
        self.xRemoveButton = 10; self.yRemoveButton = 70;
        self.xBlockButton = 10; self.yBlockButton = 100;
        self.xPercentage = 90; self.yPercentage = 10; self.widthPercentage=70; self.heightPercentage=25
        
        #setting title
        self.window.title("ADM - Coleta de Lixo")
        #setting self.window size
        width=600; height=500
        screenwidth = self.window.winfo_screenwidth()
        screenheight = self.window.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.window.geometry(alignstr)
        self.window.resizable(width=False, height=False)

        self.getAllLixeiras()
    
    def createLixeira(self, IP, capacidade):
        if len(self.lixeiras) == 0:
            self.widthButton = 55; self.heightButton = 25;
            self.xAddButton = 10; self.yAddButton = 40;
            self.xRemoveButton = 10; self.yRemoveButton = 70;
            self.xBlockButton = 10; self.yBlockButton = 100;
            self.xPercentage = 70; self.yPercentage = 50; self.widthPercentage=70; self.heightPercentage=25
            self.xIp = 70; self.yIp = 90; self.widthIp = 70; self.heightIp = 25;
        
        else:
            self.xAddButton = self.xAddButton + 190;
            self.xRemoveButton = self.xRemoveButton + 190;
            self.xBlockButton = self.xBlockButton + 190;
            self.xPercentage = self.xPercentage + 190;
            self.xIp = self.xIp + 190;

        # Add Lixo Button
        addButton=tk.Button(self.window, name = "addButton" + str(self.index))
        addButton.bind('<Button-1>', self.addButtonCommand(IP,  hash(IP + str(self.index)) ) )
        addButton["bg"] = "#efefef"
        addButton["font"] = tkFont.Font(family='Times',size=10)
        addButton["fg"] = "#000000"
        addButton["justify"] = "center"
        addButton["text"] = "Add"
        addButton.place(x = self.xAddButton, y = self.yAddButton, width = self.widthButton, height =self.heightButton)

        # Remove Lixo BUtton
        removeButton=tk.Button(self.window, name = "removeButton" + str(self.index))
        removeButton["bg"] = "#efefef"
        removeButton["font"] = tkFont.Font(family='Times',size=10)
        removeButton["fg"] = "#000000"
        removeButton["justify"] = "center"
        removeButton["text"] = "Remover"
        removeButton.place(x=self.xRemoveButton, y=self.yRemoveButton, width=self.widthButton, height=self.heightButton)
        # removeButton["command"] = self.GButton_311_command

        # Bloquear Lixeira Button
        blockButton=tk.Button(self.window, name = "blockButton" + str(self.index))
        blockButton["bg"] = "#efefef"
        blockButton["font"] = tkFont.Font(family='Times',size=10)
        blockButton["fg"] = "#000000"
        blockButton["justify"] = "center"
        blockButton["text"] = "Bloquear"
        blockButton.place(x=self.xBlockButton, y=self.yBlockButton, width=self.widthButton, height=self.heightButton)
        # blockButton["command"] = self.GButton_519_command

        ipLabel=tk.Label(self.window)
        ipLabel["font"] = tkFont.Font(family='Times',size=10)
        ipLabel["fg"] = "#333333"
        ipLabel["justify"] = "center"
        ipLabel["text"] = IP
        ipLabel.place(x= self.xIp, y=self.yIp, width= self.widthIp, height= self.heightIp)

        # Percentage Label
        percentage=tk.Label(self.window, name = "percentage" + str(self.index))
        percentage["font"] = tkFont.Font(family='Times',size=10)
        percentage["fg"] = "#333333"
        percentage["justify"] = "center"
        percentage["text"] = str(0) + " % (" + str(capacidade) + ")"
        percentage["relief"] = "flat"
        percentage.place(x=self.xPercentage, y=self.yPercentage, width=self.widthPercentage, height=self.heightPercentage)        
        
        
    def getAllLixeiras(self):
        self.adm.verificarEstadoLixeiras()
        # self.lixeiras = self.adm.receberDados()
        print('11111111', self.lixeiras)

    # def btnCreateLixeiras_command(self):      
    #     self.createLixeira(self.ipInput.get(),self.capacidadeInput.get())

    # def bindCreateLixeirasEvent(self,event):
    #     if self.ipInput.get() == '' or self.capacidadeInput.get() == '': self.btnCreateLixeiras['state'] = 'disabled'
    #     elif self.ipInput.get() != '' and self.capacidadeInput.get() != '': self.btnCreateLixeiras['state'] = 'normal'

    # def addButtonCommand(self, lixeiraIp, lixeiraId):
    #     self.central.addLixo(lixeiraIp, lixeiraId)
    #     self.central.getLixeira(lixeiraIp, lixeiraId)

if __name__ == "__main__":
    window = tk.Tk()
    app = View(window)
    window.mainloop()
