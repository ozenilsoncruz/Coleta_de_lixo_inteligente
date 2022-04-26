import sys
sys.path.append('../')

import tkinter as tk
import tkinter.font as tkFont 
import random, string
from Lixeira import Lixeira

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
        self.capacidadeLabel["font"] = tkFont.Font(family='Times',size=10)
        self.capacidadeLabel["fg"] = "#333333"
        self.capacidadeLabel["justify"] = "center"
        self.capacidadeLabel["text"] = "Capacidade"
        self.capacidadeLabel.place(x=10,y=460,width=70,height=25)

        self.capacidadeInput=tk.Entry(self.window, name = "capacidadeInput")
        self.capacidadeInput.pack()
        self.capacidadeInput.bind('<Enter>',self.bindCreateLixeirasEvent)
        self.capacidadeInput.bind('<Enter>',self.bindCapacidadeInputButton)
        self.capacidadeInput.bind('<Leave>',self.bindCapacidadeInputButton)
        self.capacidadeInput.bind('<Button-1>',self.bindCapacidadeInputButton)
        self.capacidadeInput["bg"] = "#f8f8f8"
        self.capacidadeInput["borderwidth"] = "1px"
        self.capacidadeInput["font"] = tkFont.Font(family='Times',size=10)
        self.capacidadeInput["fg"] = "#333333"
        self.capacidadeInput["justify"] = "center"
        self.capacidadeInput["text"] = 0
        self.capacidadeInput.place(x=100,y=460,width=50,height=25)

        self.latitudeLabel=tk.Label(self.window, name = "latitudeLabel")
        self.latitudeLabel["font"] = tkFont.Font(family='Times',size=10)
        self.latitudeLabel["fg"] = "#333333"
        self.latitudeLabel["justify"] = "center"
        self.latitudeLabel["text"] = "Latitude"
        self.latitudeLabel.place(x=180,y=460,width=70,height=25)

        self.latitudeInput=tk.Entry(self.window, name = "latitudeInput")
        self.latitudeInput.pack()
        self.latitudeInput.bind('<Enter>',self.bindLatitudeInputButton)
        self.latitudeInput.bind('<Leave>',self.bindLatitudeInputButton)
        self.latitudeInput.bind('<Button-1>',self.bindLatitudeInputButton)
        self.latitudeInput["bg"] = "#f8f8f8"
        self.latitudeInput["borderwidth"] = "1px"
        self.latitudeInput["font"] = tkFont.Font(family='Times',size=10)
        self.latitudeInput["fg"] = "#333333"
        self.latitudeInput["justify"] = "center"
        self.latitudeInput["text"] = 1
        self.latitudeInput.place(x=260,y=460,width=50,height=25)

        self.longitudeLabel=tk.Label(self.window, name = "longitudeLabel")
        self.longitudeLabel["font"] = tkFont.Font(family='Times',size=10)
        self.longitudeLabel["fg"] = "#333333"
        self.longitudeLabel["justify"] = "center"
        self.longitudeLabel["text"] = "Longitude"
        self.longitudeLabel.place(x=350,y=460,width=70,height=25)
        
        self.longitudeInput=tk.Entry(self.window, name = "longitudeInput")
        self.longitudeInput.pack()
        self.longitudeInput.bind('<Enter>',self.bindLongitudeInputButton)
        self.longitudeInput.bind('<Leave>',self.bindLongitudeInputButton)
        self.longitudeInput.bind('<Button-1>',self.bindLongitudeInputButton)
        self.longitudeInput["bg"] = "#f8f8f8"
        self.longitudeInput["borderwidth"] = "1px"
        self.longitudeInput["font"] = tkFont.Font(family='Times',size=10)
        self.longitudeInput["fg"] = "#333333"
        self.longitudeInput["justify"] = "center"
        self.longitudeInput["text"] = 2
        self.longitudeInput.place(x=430,y=460,width=50,height=25)

        # Button that creates Lixeiras
        self.btnCreateLixeiras = tk.Button(self.window, name = "btnCreateLixeiras")
        self.btnCreateLixeiras.bind('<Enter>',self.bindCreateLixeirasEvent)
        self.btnCreateLixeiras.bind('<Enter>',self.bindCapacidadeInputButton)
        self.btnCreateLixeiras.bind('<Leave>',self.bindCapacidadeInputButton)
        self.btnCreateLixeiras.bind('<Button-1>',self.bindCapacidadeInputButton)
        self.btnCreateLixeiras["bg"] = "#efefef"
        self.btnCreateLixeiras["font"] = tkFont.Font(family='Times',size=10)
        self.btnCreateLixeiras["fg"] = "#000000"
        self.btnCreateLixeiras["justify"] = "center"
        self.btnCreateLixeiras["text"] = "Add Lixeira"
        self.btnCreateLixeiras.place(x=510,y=460,width=75,height=25)
        self.btnCreateLixeiras["command"] = self.btnCreateLixeiras_command
    
    def createLixeira(self):
        capacidade = int(self.capacidadeInput.get())
        latitude = int(self.latitudeInput.get())
        longitude = int(self.longitudeInput.get())
        identif = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4))
        
        self.lixeiraModel = Lixeira(identif, latitude, longitude, capacidade, False)
        
        self.window.title("Lixeira " + identif)
        
        self.addButton=tk.Button(self.window)
        self.addButton.bind('<Enter>',self.bindAddButton)
        self.addButton.bind('<Leave>',self.bindAddButton)
        self.addButton.bind('<Button-1>',self.bindAddButton)
        self.addButton["bg"] = "#efefef"
        self.addButton["font"] = tkFont.Font(family='Times',size=10)
        self.addButton["fg"] = "#000000"
        self.addButton["justify"] = "center"
        self.addButton["text"] = "Adicionar Lixo"
        self.addButton.place(x=100,y=340,width=150,height=25)
        self.addButton["command"] = self.addButton_command

        # self.removeButton=tk.Button(self.window)
        # self.removeButton.bind('<Enter>',self.bindRemoveButton)
        # self.removeButton.bind('<Leave>',self.bindRemoveButton)
        # self.removeButton.bind('<Button-1>',self.bindRemoveButton)
        # self.removeButton["bg"] = "#efefef"
        # self.removeButton["font"] = tkFont.Font(family='Times',size=10)
        # self.removeButton["fg"] = "#000000"
        # self.removeButton["justify"] = "center"
        # self.removeButton["text"] = "Remove Lixo"
        # self.removeButton.place(x=120,y=100,width=150,height=25)
        # self.removeButton["command"] = self.removeButton_command

        self.blockButton=tk.Button(self.window)
        self.blockButton.bind('<Enter>',self.bindBlockButton)
        self.blockButton.bind('<Leave>',self.bindBlockButton)
        self.blockButton.bind('<Button-1>',self.bindBlockButton)
        self.blockButton["bg"] = "#efefef"
        self.blockButton["font"] = tkFont.Font(family='Times',size=10)
        self.blockButton["fg"] = "#000000"
        self.blockButton["justify"] = "center"
        self.blockButton["text"] = "Bloquear"
        self.blockButton.place(x=360,y=340,width=150,height=25)
        self.blockButton["command"] = self.blockButton_command

        self.idLabel=tk.Label(self.window)
        self.idLabel["font"] = tkFont.Font(family='Times',size=10)
        self.idLabel["fg"] = "#333333"
        self.idLabel["justify"] = "center"
        self.idLabel["text"] = "Lixeira " + str(self.lixeiraModel.getId())
        self.idLabel.place(x=230,y=50,width=140,height=25)

        self.latitudeLabelLixeira=tk.Label(self.window)
        self.latitudeLabelLixeira["font"] =  tkFont.Font(family='Times',size=10)
        self.latitudeLabelLixeira["fg"] = "#333333"
        self.latitudeLabelLixeira["justify"] = "center"
        self.latitudeLabelLixeira["text"] = "Latitude: " + str(self.lixeiraModel.getLatitude())
        self.latitudeLabelLixeira.place(x=230,y=100,width=140,height=25)

        self.longitudeLabelLixeira=tk.Label(self.window)
        self.longitudeLabelLixeira["font"] = tkFont.Font(family='Times',size=10)
        self.longitudeLabelLixeira["fg"] = "#333333"
        self.longitudeLabelLixeira["justify"] = "center"
        self.longitudeLabelLixeira["text"] = "Longitude: " + str(self.lixeiraModel.getLongitude())
        self.longitudeLabelLixeira.place(x=230,y=140,width=140,height=25)

        self.statusLabel=tk.Label(self.window)
        self.statusLabel["font"] = tkFont.Font(family='Times',size=10)
        self.statusLabel["fg"] = "#333333"
        self.statusLabel["justify"] = "center"
        self.statusLabel["text"] = "Status: Bloqueada" if self.lixeiraModel.getBloqueado() else "Status: Desbloqueada"
        self.statusLabel.place(x=230,y=180,width=140,height=25)

        self.lixoLabel=tk.Label(self.window)
        self.lixoLabel["font"] = tkFont.Font(family='Times',size=10)
        self.lixoLabel["fg"] = "#333333"
        self.lixoLabel["justify"] = "center"
        self.lixoLabel["text"] = "Lixo: " + str(self.lixeiraModel.getLixo())
        self.lixoLabel.place(x=230,y=220,width=140,height=25)

        self.capacidadeLabelLixeira=tk.Label(self.window)
        self.capacidadeLabelLixeira["font"] = tkFont.Font(family='Times',size=10)
        self.capacidadeLabelLixeira["fg"] = "#333333"
        self.capacidadeLabelLixeira["justify"] = "center"
        self.capacidadeLabelLixeira["text"] = "Capacidade: " + str(self.lixeiraModel.getCapacidade())
        self.capacidadeLabelLixeira.place(x=230,y=260,width=140,height=25)

        self.percentageLabel=tk.Label(self.window)
        self.percentageLabel["font"] = tkFont.Font(family='Times',size=10)
        self.percentageLabel["fg"] = "#333333"
        self.percentageLabel["justify"] = "center"
        self.percentageLabel["text"] = "Porcentagem: " +  str(self.lixeiraModel.getPorcentagem()) + " %"
        self.percentageLabel.place(x=230,y=300,width=140,height=25)


    def btnCreateLixeiras_command(self):      
        self.createLixeira()

    def addButton_command(self):
        self.lixeiraModel.addLixo(1)
        print('Add Lixo - ', self.lixeiraModel.dadosLixeira())
        self.fetchLixerira()

    # def removeButton_command(self):
    #     print('Remove Lixo - ', self.lixeiraModel.dadosLixeira())
    #     self.lixeiraModel.esvaziarLixeira()
    #     self.fetchLixerira()

    def blockButton_command(self):
        if self.lixeiraModel.getBloqueado():
            self.lixeiraModel.desbloquear()
            self.fetchLixerira()
        else:
            self.lixeiraModel.bloquear()
            self.fetchLixerira()
            
    def bindAddButton(self, event):
        self.fetchLixerira()
        if self.lixeiraModel.getBloqueado() or self.lixeiraModel.getPorcentagem() >= 1: self.addButton['state'] = 'disabled'
        elif not self.lixeiraModel.getBloqueado() and self.lixeiraModel.getPorcentagem() < 1: self.addButton['state'] = 'normal'
        
    # def bindRemoveButton(self, event):
    #     if self.lixeiraModel.getLixo() == 0 or self.lixeiraModel.getBloqueado() : self.removeButton['state'] = 'disabled'
    #     elif self.lixeiraModel.getLixo() > 0 or not self.lixeiraModel.getBloqueado() : self.removeButton['state'] = 'normal'
    #     else : self.removeButton['state'] = 'normal'
    
    def bindBlockButton(self, event):
        self.fetchLixerira()
        if self.lixeiraModel.getBloqueado() : self.blockButton['text'] = 'Desbloquear'
        else : self.blockButton['text'] = 'Bloquear'

    def bindCreateLixeirasEvent(self,event):
        self.fetchLixerira()
        if self.capacidadeInput.get() == '' or self.latitudeInput.get() == '' or self.longitudeInput.get() =='': 
            self.btnCreateLixeiras['state'] = 'disabled'
            
        elif self.capacidadeInput.get() != '' and self.latitudeInput.get() != '' and self.longitudeInput.get() !='': 
            self.btnCreateLixeiras['state'] = 'normal'
            
        elif self.lixeiraModel != None: event.widget.place_forget()

    def bindCapacidadeInputButton(self,event):
        self.fetchLixerira()
        if self.lixeiraModel != None: 
            self.capacidadeInput['state'] = 'disabled'; self.btnCreateLixeiras['state'] = 'disabled'
            self.latitudeInput['state'] = 'disabled'; self.longitudeInput['state'] = 'disabled'; 
        else: 
            self.capacidadeInput['state'] = 'normal'; self.btnCreateLixeiras['state'] = 'normal'
            self.latitudeInput['state'] = 'normal'; self.longitudeInput['state'] = 'normal'; 

    def bindLongitudeInputButton(self, event):
        self.fetchLixerira()
        if self.lixeiraModel != None: 
            self.capacidadeInput['state'] = 'disabled'; self.btnCreateLixeiras['state'] = 'disabled'
            self.latitudeInput['state'] = 'disabled'; self.longitudeInput['state'] = 'disabled'; 
            
        else: 
            self.capacidadeInput['state'] = 'normal'; self.btnCreateLixeiras['state'] = 'normal'
            self.latitudeInput['state'] = 'normal'; self.longitudeInput['state'] = 'normal'; 

    def bindLatitudeInputButton(self, event):
        self.fetchLixerira()
        if self.lixeiraModel != None: 
            self.capacidadeInput['state'] = 'disabled'; self.btnCreateLixeiras['state'] = 'disabled'
            self.latitudeInput['state'] = 'disabled'; self.longitudeInput['state'] = 'disabled'; 
            
        else: 
            self.capacidadeInput['state'] = 'normal'; self.btnCreateLixeiras['state'] = 'normal'
            self.latitudeInput['state'] = 'normal'; self.longitudeInput['state'] = 'normal'; 

    def fetchLixerira(self):
        if self.lixeiraModel != None:
            self.idLabel["text"] = "Lixeira " + str(self.lixeiraModel.getId())
            self.latitudeLabelLixeira["text"] = "Latitude: " + str(self.lixeiraModel.getLatitude())
            self.longitudeLabelLixeira["text"] = "Longitude: " + str(self.lixeiraModel.getLongitude())
            self.statusLabel["text"] = "Status: Bloqueada" if self.lixeiraModel.getBloqueado() else "Status: Desbloqueada"
            self.lixoLabel["text"] = "Lixo: " + str(self.lixeiraModel.getLixo())
            self.capacidadeLabelLixeira["text"] = "Capacidade: " + str(self.lixeiraModel.getCapacidade())
            self.percentageLabel["text"] = "Porcentagem: " + str(self.lixeiraModel.getPorcentagem() * 100) + " %"


if __name__ == "__main__":
    window = tk.Tk()
    app = LixeiraView(window)
    window.mainloop()