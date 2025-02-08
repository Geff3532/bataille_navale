import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation
import time
import tkinter as tk
import threading


class Feu_de_foret(tk.Tk):
    
    def __init__(self,n_foret):
        
        tk.Tk.__init__(self)
        self.n_foret = n_foret
        self.Map()

    def definir_foret(self):
        foret = np.empty((0,(self.n_foret+2))) #On creer un tableau vide de 10 colonnes et 0 lignes
        for i in range (self.n_foret+2):
            ligne= np.random.choice(2, size=(1,self.n_foret+2), p=[(10-self.a)/10,self.a/10])
            foret=np.concatenate((foret, ligne))
        foret[0,:]=0
        foret[:,0]=0
        foret[-1,:]=0
        foret[:,-1]=0
        self.temps = np.zeros((self.n_foret+2,self.n_foret+2))
        self.foret = foret
        return self.foret , self.temps
      
    def afficher_foret(self):
         
         self.root = tk.Tk()
         self.root.attributes("-fullscreen",True)
         self.root.title("Représentation d'une foret et simulation d'un feu")
         self.root.config(background="#F9E7D3")
         self.root.bind('<Delete>',lambda event:self.root.destroy())

         tk.Label(self.root, text="Représentation d'une forêt et simulation d'un feu", font=("Courrier",20), bg="#F9E7D3", fg="#50463C").place(x=300,y=50)
         
         self._fig = plt.figure()
         self._ax1 = self._fig.add_subplot(1,1,1)

         self._line = self._ax1.imshow(self.foret, cmap = ListedColormap(["black", "red", "white", "green"]), interpolation='nearest')
         plt.xticks(ha='right')
         plt.subplots_adjust(bottom=0.30)

         self._canvas = FigureCanvasTkAgg(self._fig, master=self.root) 
         self._canvas.get_tk_widget().place(x=500,y=300)
         self._canvas.draw()        
         self._animate = None
         
         self.toggleAnimate()

         self.root.mainloop()

    def toggleAnimate(self):
        if self._animate is None:
            self._canvas.draw_idle()
            self._animate = animation.FuncAnimation(self._fig, self.animate, fargs=(self._ax1, self._line), interval=100) 
    
    def animate(self,i, ax1, line):
        print(3)
        
        line.set_data(self.foret)

        ax1.relim()
        ax1.autoscale_view(True,True,True)

        return line
    
    def propagation1(self):
        i=self.ligne
        j=self.colonne
        self.arbres_brules=[]
        if i+1<len(self.foret) and j+1<len(self.foret) and i-1>0 and i+1>0 and self.foret[i,j]==-1:
            for x in range (-1,2):
                for y in range(-1,2):
                    if self.foret[i+x,j+y]==1:
                        self.foret[i+x,j+y]=-1
                        self.arbres_brules.append([i+x,j+y])
        self.foret[i,j]=-2
        
    def propagation(self):
        for h in range (len(self.arbres_brules)):
            i,j=self.arbres_brules[h]
            if i+1<len(self.foret) and j+1<len(self.foret) and i-1>0 and i+1>0 and self.foret[i,j]==-1:
                for x in range(-1,2):
                    for y in range(-1,2):
                        if self.foret[i+x,j+y]==1:
                            self.foret[i+x,j+y]=np.random.choice([-1,1], p=[(self.P/10),1-(self.P/10)])
                            self.arbres_brules.append([i+x,j+y])
            self.temps[i,j]-=1
            if self.temps[i,j]<-self.N:
                self.foret[i,j]=-2
            
        
    def afficher_propagation(self):
        
        Fin = False
        l=[1]
        while Fin is False:
            self.propagation()
            print(1)
            time.sleep(0.1)
            l.append(len(self.arbres_brules))
            if (l[-1] == l[-2]):
                Fin = True
                
    def lancer(self,event):
        
        self.P = int(self.entrée3.get())
        self.N = int(self.entrée2.get())
        self.a = int(self.entrée1.get())
        self.ligne = int(self.entrée4.get())
        self.colonne = int(self.entrée5.get())
        
        self.definir_foret()
        
        if self.foret[self.ligne,self.colonne] != 1:
            tk.messagebox.showinfo(title="Alerte",message="Il n'y a pas d'arbre ici")
            return
        self.foret[self.ligne,self.colonne] = -1
        
        self.propagation1()
        
        thread1 = threading.Thread(target=self.afficher_foret)
        self.destroy()
        thread1.start()
        thread2 = threading.Thread(target=self.afficher_propagation)
        thread2.start()
        
        thread2.join()
        thread1.join()

    def Map(self):
        
        self.attributes("-fullscreen",True)
        self.title("Représentation d'une foret et simulation d'un feu")
        self.config(background="#F9E7D3")
    
        tk.Label(self, text="Représentation d'une forêt et simulation d'un feu", font=("Courrier",20), bg="#F9E7D3", fg="#50463C").place(x=300,y=50)
        tk.Label(self, text="Cliquez sur un arbre pour lancer une météorite:", font=("Courrier",15), bg="#F9E7D3", fg="#50463C").place(x=300,y=100)
        tk.Label(self, text="Densité de la foret", font=("Courrier",15), bg="#F9E7D3", fg="#50463C").place(x=300,y=150)
        
        self.entrée1 = tk.Entry(self)
        self.entrée1.place(x=300,y=200)
        
        tk.Label(self, text="Unité de temps que met un arbre à bruler: ", font=("Courrier",15), bg="#F9E7D3", fg="#50463C").place(x=300,y=250)
        
        self.entrée2 = tk.Entry(self)
        self.entrée2.place(x=300,y=300)
        
        tk.Label(self, text="Probabilité qu'un arbre brule: ", font=("Courrier",15), bg="#F9E7D3", fg="#50463C").place(x=300,y=350)
        
        self.entrée3 = tk.Entry(self)
        self.entrée3.place(x=300,y=400)
        
        tk.Label(self, text="Entrer la ligne : ", font=("Courrier",15), bg="#F9E7D3", fg="#50463C").place(x=300,y=450)
        
        self.entrée4 = tk.Entry(self)
        self.entrée4.place(x=300,y=500)
        
        tk.Label(self, text="Entrer la colonne : ", font=("Courrier",15), bg="#F9E7D3", fg="#50463C").place(x=300,y=550)

        self.entrée5 = tk.Entry(self)
        self.entrée5.place(x=300,y=600)
        
        self.bind('<Return>',self.lancer)
        self.bind('<Delete>',lambda event: self.destroy())

        self.mainloop()


Feu_de_foret(100)