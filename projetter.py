"""
Mini-projet
Sujet 13
"""

import numpy as np
import random as rd
import tkinter as tk
import time
import mysql.connector as mysql
import json

class Naval(tk.Tk):
    
    def __init__(self,n=10):
        tk.Tk.__init__(self)
        
        self.n = n
        self.plateau = [[0 for i in range(self.n)] for j in range(self.n)]
        self.attaque = [[0 for i in range(self.n)] for j in range(self.n)]
        self.Hplateau = [[0 for i in range(self.n)] for j in range(self.n)]
        self.Hattaque = [[0 for i in range(self.n)] for j in range(self.n)]
        self.placer_bateaux()
        self.nettoyage()
        self.listes_positions_bateaux()
        self.mode = "recherche"
        self.level = "direction"
        
        self.liste = [4,64,124,184,244,304,364,424,484,544,604]
        self.longueur = [2,3,3,4,5]
        self.map = []
        self.bateau = []
        self.json = {}
        self.create()
        
        if rd.randint(0,1) == 1:
            self.Botattaque()
        
    def create(self):
        self.attributes('-fullscreen',True)
        self.title("Bataille Navale")
        tk.Label(self, text="Préparation", font=("Helvetica", 30)).place(relx=0.4180,rely=0.0278)
        
        "Canv defini un nouveau referentiel pour le carre"
        self.canv = tk.Canvas(self, bg='light gray', height=604, width=604)
        self.canv.create_rectangle(0,0,604,604,fill='white')
        for x in self.liste:
            self.canv.create_line(0,x,610,x,fill='black',width=4)
            self.canv.create_line(x,0,x,610,fill='black',width=4)
        self.canv.bind('<Button-1>', self.find_coord)
        
        self.canv.place(relx=0.2625,rely=0.1264)
        
        tk.Button(self,text="Effacer",font=("Helvetica", 20),command=self.effacer_bateau).place(relx=0.8,rely=0.5833)
        tk.Button(self,text="Valider",font=("Helvetica", 20),command=self.valider_bateau).place(relx=0.8,rely=0.6667)
        tk.Button(self,text="Recommencer",font=("Helvetica", 20),command=self.effacer_map).place(relx=0.8,rely=0.75)
        tk.Button(self,text="Quitter",font=("Helvetica", 20),command=self.destroy).place(relx=0.8,rely=0.8333)
        self.affichage = tk.Label(self,text=f"Longeur restante :\n {' '.join([str(i) for i in self.longueur])}",font=("Helvetica", 20))
        self.affichage.place(relx=0.7813,rely=0.4167)
        
        self.mainloop()
        
    def find_coord(self,click):
        x,y = 0,0
        for index,elt in enumerate(self.liste):
            if click.x <= elt+60 and click.x >= elt:
                x = (index,elt)
            if click.y <= elt+60 and click.y >= elt:
                y = (index,elt)
        self.bateau.append([x[0],y[0]])
        self.trace_croix(x[1]+30, y[1]+30)
    
    def trace_croix(self,x,y):
        self.canv.create_line(x-25,y-25,x+25,y+25,width=3,fill="black")
        self.canv.create_line(x-25,y+25,x+25,y-25,width=3,fill="black")
        
    def effacer_bateau(self):
        self.bateau = []
        for i in self.canv.find_all():
            self.canv.delete(i)
        self.canv.create_rectangle(0,0,604,604,fill='white')
        for x in self.liste:
            self.canv.create_line(0,x,610,x,fill='black',width=4)
            self.canv.create_line(x,0,x,610,fill='black',width=4)
        self.canv.bind('<Button-1>', self.find_coord)
        self.canv.place(relx=0.2625,rely=0.1264)
        for bateau in self.map:
            for x,y in bateau:
                self.trace_croix(self.liste[x]+30, self.liste[y]+30)
                
    def effacer_map(self):
        self.bateau = []
        self.map = []
        for i in self.canv.find_all():
            self.canv.delete(i)
        self.canv.create_rectangle(0,0,604,604,fill='white')
        for x in self.liste:
            self.canv.create_line(0,x,610,x,fill='black',width=4)
            self.canv.create_line(x,0,x,610,fill='black',width=4)
        self.canv.bind('<Button-1>', self.find_coord)
        self.canv.place(relx=0.2625,rely=0.1264)
        self.longueur = [2,3,3,4,5]
        self.affichage['text'] = f"Longeur restante :\n {' '.join([str(i) for i in self.longueur])}"
            
    def valider_bateau(self):
        self.bateau.sort()
        if len(self.bateau) not in self.longueur:
            tk.messagebox.showinfo(title="Alerte",message="Le bateau n'a pas pas la bonne longueur")
            self.effacer_bateau()
            return False
        if self.bateau_aligné() == False:
            tk.messagebox.showinfo(title="Alerte",message="Le bateau doit etre sur une ligne ou colonne")
            self.effacer_bateau()
            return False
        if self.bateau_collé() == False:
            tk.messagebox.showinfo(title="Alerte",message="On ne peut pas collé les bateaux")
            self.effacer_bateau()
            return False
        if self.bateau_1_morceau() == False:
            tk.messagebox.showinfo(title="Alerte",message="Le bateau doit etre en un morceau")
            self.effacer_bateau()
            return False
        self.map.append(self.bateau)
        self.longueur.remove(len(self.bateau))
        self.bateau = []
        self.affichage['text'] = f"Longeur restante :\n {' '.join([str(i) for i in self.longueur])}"
        if len(self.longueur) == 0:
            tk.messagebox.showinfo(title="Alerte",message="Cliquer sur le bouton jouer pour commencer !")
            tk.Button(self,text="Jouer",font=("Helvetica", 20),command=self.definir_Hplateau).place(relx=0.8,rely=0.2)
    
    def bateau_aligné(self):
        for i in range(len(self.bateau)-1):
            if self.bateau[i][0] != self.bateau[i+1][0] and self.bateau[i][1] != self.bateau[i+1][1]:
                return False
        return True
    
    def bateau_collé(self):
        for x,y in self.bateau:
            for bateau in self.map:
                for x_,y_ in bateau:
                    d = abs(x-x_) + abs(y-y_)
                    if d <= 1: return False
        return True
    
    def bateau_1_morceau(self):
        for i in range(len(self.bateau)-1):
            d = abs(self.bateau[i][0]-self.bateau[i+1][0]) + abs(self.bateau[i][1]-self.bateau[i+1][1])
            if d != 1: return False
        return True
    
    def definir_Hplateau(self):
        
        for bateau in self.map:
            for x,y in bateau:
                self.Hplateau[y][x] = 1
        self.Hpositions_bateaux = []
        for bateau in self.map:
            new_bat = []
            for x,y in bateau:
                new_bat.append([y,x])
            self.Hpositions_bateaux.append(new_bat)
        
        """ PROJET DONNEES """
        
        
        if len(self.json) == 0:
            n = "0"
            json_compo = {}
            for bateau in self.Hpositions_bateaux:
                if len(bateau) == 3:
                    json_compo[str(len(bateau))+n] = bateau
                    n = "1"
                else:
                    json_compo[str(len(bateau))] = bateau
            self.json = json.dumps(json_compo)
            
            db = mysql.connect(host="localhost",user='root',password='',db='test')
            cursor = db.cursor() 
            cursor.execute(("INSERT INTO bataille_navale (compo) VALUES (%s)"),(self.json,))    
            db.commit()
            cursor.close()
            
            cursor = db.cursor() 
            cursor.execute(('SELECT indice FROM bataille_navale'))
            table = cursor.fetchall()
            self.id = max(table)[0]
            cursor.close()
    
        
        """ FIN DE PROJET """
        
        self.remplace()
        
    def remplace(self):
        
        self.time_debut = time.time()
        
        for elt in self.winfo_children():
            elt.destroy()
            
        tk.Label(self, text="BATAILLE NAVALE", font=("Helvetica", 25)).place(relx=0.3906,rely=0.0208)
        
        self.canv_def = tk.Canvas(self, bg='light gray', height=604, width=604)
        self.canv_def.create_rectangle(0,0,604,604,fill='cyan')
        for x in self.liste:
            self.canv_def.create_line(0,x,610,x,fill='black',width=4)
            self.canv_def.create_line(x,0,x,610,fill='black',width=4)
        
        self.canv_def.place(relx=0.0195,rely=0.125)
        
        self.canv_att = tk.Canvas(self, bg='light gray', height=604, width=604)
        self.canv_att.create_rectangle(0,0,604,604,fill='cyan')
        for x in self.liste:
            self.canv_att.create_line(0,x,610,x,fill='black',width=4)
            self.canv_att.create_line(x,0,x,610,fill='black',width=4)
        
        self.canv_att.place(relx=0.5078,rely=0.125)
        
        tk.Label(self, text="DEFENSE",font=("Helvetica", 25)).place(relx=0.1992,rely=0.0625)
        tk.Label(self, text="ATTAQUE",font=("Helvetica", 25)).place(relx=0.6797,rely=0.0625)
        
        for bateau in self.Hpositions_bateaux:
            bateau.sort()
            if bateau[0][0] == bateau[1][0]: #meme ligne
                mil = self.liste[bateau[0][0]]
                self.canv_def.create_oval(self.liste[bateau[0][1]]+4,mil+10,self.liste[bateau[-1][1]]+56,mil+50,width=2,fill="grey")
            else: #meme colonne
                mil = self.liste[bateau[0][1]]
                self.canv_def.create_oval(mil+10,self.liste[bateau[0][0]]+4,mil+50,self.liste[bateau[-1][0]]+56,width=2,fill="grey")
                
        self.canv_att.bind('<Button-1>', self.Hattaquer)
        
    def toucher_attaque(self,x,y):
        x,y = self.liste[y]+30,self.liste[x]+30
        r = 20
        self.canv_att.create_oval(x-r,y-r,x+r,y+r,width=2,fill="red")
    
    def dans_leau_attaque(self,x,y):
        x,y = self.liste[y]+30,self.liste[x]+30
        self.canv_att.create_line(x-20,y-20,x+20,y+20,width=2,fill="grey")
        self.canv_att.create_line(x-20,y+20,x+20,y-20,width=2,fill="grey")
        
    def toucher_defense(self,x,y):
        x,y = self.liste[y]+30,self.liste[x]+30
        r = 20
        self.canv_def.create_oval(x-r,y-r,x+r,y+r,width=2,fill="red")
    
    def dans_leau_defense(self,x,y):
        x,y = self.liste[y]+30,self.liste[x]+30
        self.canv_def.create_line(x-20,y-20,x+20,y+20,width=2,fill="grey")
        self.canv_def.create_line(x-20,y+20,x+20,y-20,width=2,fill="grey")

    def placer_bateaux(self):
        longueur = [5,4,3,3,2]
        for elt in longueur:
            self.placer(elt)
        
    def placer(self,n):
        x, y = rd.randint(0, self.n-1), rd.randint(0, self.n-1)
        self.x, self.y = x,y

        if self.plateau[x][y] != 0:
            return self.placer(n)
        self.plateau[x][y] = 1
        
        choice = rd.randint(0, 1)
        
        if choice == 0: 
            
            if self.haut_bas(x+1,x+n,n): #bas 
                if x+n < self.n:
                    self.plateau[x+n][y] = 2
                if x-1 >= 0:
                    self.plateau[x-1][y] = 2
                if y-1 >= 0:
                    self.plateau[x][y-1] = 2
                if y+1 < self.n:
                    self.plateau[x][y+1] = 2
                return True
            
            if self.haut_bas(x-n+1,x,n): #haut
                if x-n >= 0:
                    self.plateau[x-n][y] = 2
                if x+1 < self.n:
                    self.plateau[x+1][y] = 2
                if y-1 >= 0:
                    self.plateau[x][y-1] = 2
                if y+1 < self.n:
                    self.plateau[x][y+1] = 2
                return True
            
            if self.gauche_droite(y+1,y+n,n): #droite
                if y + n < self.n:
                    self.plateau[x][y+n] = 2
                if y - 1 >= 0:
                    self.plateau[x][y-1] = 2
                if x - 1 >= 0:
                    self.plateau[x-1][y] = 2
                if x + 1 < self.n:
                    self.plateau[x+1][y] = 2
                return True
            
            if self.gauche_droite(y-n+1,y,n): #gauche
                if y - n >= 0:
                    self.plateau[x][y-n] = 2
                if y + 1 < self.n:
                    self.plateau[x][y+1] = 2
                if x - 1 >= 0:
                    self.plateau[x-1][y] = 2
                if x + 1 < self.n:
                    self.plateau[x+1][y] = 2
                return True
        
        else:
            
            if self.gauche_droite(y-n+1,y,n): #gauche
                if y - n >= 0:
                    self.plateau[x][y-n] = 2
                if y + 1 < self.n:
                    self.plateau[x][y+1] = 2
                if x - 1 >= 0:
                    self.plateau[x-1][y] = 2
                if x + 1 < self.n:
                    self.plateau[x+1][y] = 2
                return True
            
            if self.gauche_droite(y+1,y+n,n): #droite
                if y + n < self.n:
                    self.plateau[x][y+n] = 2
                if y - 1 >= 0:
                    self.plateau[x][y-1] = 2
                if x - 1 >= 0:
                    self.plateau[x-1][y] = 2
                if x + 1 < self.n:
                    self.plateau[x+1][y] = 2
                return True
            
            if self.haut_bas(x-n+1,x,n): #haut
                if x-n >= 0:
                    self.plateau[x-n][y] = 2
                if x+1 < self.n:
                    self.plateau[x+1][y] = 2
                if y-1 >= 0:
                    self.plateau[x][y-1] = 2
                if y+1 < self.n:
                    self.plateau[x][y+1] = 2
                return True
            
            if self.haut_bas(x+1,x+n,n): #bas
                if x+n < self.n:
                    self.plateau[x+n][y] = 2
                if x-1 >= 0:
                    self.plateau[x-1][y] = 2
                if y-1 >= 0:
                    self.plateau[x][y-1] = 2
                if y+1 < self.n:
                    self.plateau[x][y+1] = 2
                return True
            
        
        self.plateau[x][y] = 0
        return self.placer(n)
        
        
    def haut_bas(self,a,b,n):
        y = self.y
        compteur = 1
        for k in range(a,b):
            if k >= 0 and k < self.n and self.plateau[k][y] == 0:
                compteur += 1
        if compteur == n: 
            for x in range(a,b):
                self.plateau[x][y] = 1
                if x >= 0 and x < self.n and y-1 >= 0:
                    self.plateau[x][y-1] = 2
                if x >= 0 and x < self.n and y+1 < self.n:
                    self.plateau[x][y+1] = 2
            return True
        return False
    
    def gauche_droite(self,a,b,n):
        x = self.x
        compteur = 1
        for k in range(a,b):
            if k >= 0 and k < self.n and self.plateau[x][k] == 0:
                compteur += 1
        if compteur == n: 
            for y in range(a,b):
                self.plateau[x][y] = 1
                if y >= 0 and y < self.n and x-1 >= 0:
                    self.plateau[x-1][y] = 2
                if y >= 0 and y < self.n and x+1 < self.n:
                    self.plateau[x+1][y] = 2
            return True
        return False
    
    def nettoyage(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.plateau[i][j] == 2:
                    self.plateau[i][j] = 0
                    
    def listes_positions_bateaux(self):
        position = []
        for i in range(self.n):
            for j in range(self.n):
                if self.plateau[i][j] == 1:
                    position.append((i,j))
        positions_bateaux = []
        while len(position) > 0:
            arbre = [position[0]]
            for i in range(len(position)):
                for j in range(len(arbre)):
                    d = abs(arbre[j][0] - position[i][0]) + abs(arbre[j][1] - position[i][1])
                    if d == 1:
                        arbre.append(position[i])
            positions_bateaux.append(arbre)
            for elt in arbre:
                position.remove(elt)
                
        self.positions_bateaux = positions_bateaux
    
    def est_coule(self):
        for bateau in self.positions_bateaux:
            s = 0
            for coord in bateau:
                s += self.plateau[coord[0]][coord[1]]
            if s == -len(bateau):
                self.positions_bateaux.remove(bateau)
                return True
        return False
    
    def Hest_coule(self):
        for bateau in self.Hpositions_bateaux:
            s = 0
            for coord in bateau:
                s += self.Hplateau[coord[0]][coord[1]]
            if s == -len(bateau):
                self.contour(bateau)
                self.Hpositions_bateaux.remove(bateau)
                return True
        return False
    
    def partie_fini(self):
        if len(self.positions_bateaux) == 0 or len(self.Hpositions_bateaux) == 0:
            return True
        return False
    
    def contour(self,bateau):
        for coord in bateau:
            x,y = coord[0],coord[1]
            if x - 1 >= 0 and self.attaque[x-1][y] == 0:
                self.attaque[x-1][y] = 2
            if x + 1 < self.n and self.attaque[x+1][y] == 0:
                self.attaque[x+1][y] = 2
            if y - 1 >= 0 and self.attaque[x][y-1] == 0:
                self.attaque[x][y-1] = 2
            if y + 1 < self.n and self.attaque[x][y+1] == 0:
                self.attaque[x][y+1] = 2
    
    def nb_coup(self):
        coup = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.Hattaque[i][j] != 0 and abs(self.Hattaque[i][j]) == 1:
                    coup += 1
        return coup
    
    def trouver_direction(self):
        
        if self.recherche[0] == 'gauche':
            if self.y_att - 1 >= 0 and self.attaque[self.x_att][self.y_att-1] == 0:
                if self.Hplateau[self.x_att][self.y_att-1] == 1:
                    self.attaque[self.x_att][self.y_att-1] = 1
                    self.Hplateau[self.x_att][self.y_att-1] = -1
                    self.direction = ['horizontal','gauche']
                    self.current_x = self.x_att
                    self.current_y = self.y_att-1
                    self.level = "avancer"
                    self.toucher_defense(self.x_att, self.y_att-1)
                    return True
                else:
                    self.dans_leau_defense(self.x_att, self.y_att-1)
                    self.attaque[self.x_att][self.y_att-1] = -1
                    self.Hplateau[self.x_att][self.y_att-1] = -2
            else:
                self.recherche.pop(0)
                return self.trouver_direction()
            
        if self.recherche[0] == 'droite':
            if self.y_att + 1 < self.n and self.attaque[self.x_att][self.y_att+1] == 0:
                if self.Hplateau[self.x_att][self.y_att+1] == 1:
                    self.attaque[self.x_att][self.y_att+1] = 1
                    self.Hplateau[self.x_att][self.y_att+1] = -1
                    self.direction = ['horizontal','droite']
                    self.current_x = self.x_att
                    self.current_y = self.y_att+1
                    self.level = "avancer"
                    self.toucher_defense(self.x_att,self.y_att+1)
                    return True
                else:
                    self.dans_leau_defense(self.x_att,self.y_att+1)
                    self.attaque[self.x_att][self.y_att+1] = -1
                    self.Hplateau[self.x_att][self.y_att+1] = -2
            else:
                self.recherche.pop(0)
                return self.trouver_direction()
            
        if self.recherche[0] == 'bas':
            if self.x_att + 1 < self.n and self.attaque[self.x_att+1][self.y_att] == 0:
                if self.Hplateau[self.x_att+1][self.y_att] == 1:
                    self.attaque[self.x_att+1][self.y_att] = 1
                    self.Hplateau[self.x_att+1][self.y_att] = -1
                    self.direction = ['vertical','bas']
                    self.current_x = self.x_att+1
                    self.current_y = self.y_att
                    self.level = "avancer"
                    self.toucher_defense(self.x_att+1,self.y_att)
                    return True
                else:
                    self.dans_leau_defense(self.x_att+1,self.y_att)
                    self.attaque[self.x_att+1][self.y_att] = -1
                    self.Hplateau[self.x_att+1][self.y_att] = -2
            else:
                self.recherche.pop(0)
                return self.trouver_direction()
            
        if self.recherche[0] == 'haut':
            if self.x_att - 1 >= 0 and self.attaque[self.x_att-1][self.y_att] == 0:
                if self.Hplateau[self.x_att-1][self.y_att] == 1:
                    self.attaque[self.x_att-1][self.y_att] = 1
                    self.Hplateau[self.x_att-1][self.y_att] = -1
                    self.direction = ['vertical','haut']
                    self.current_x = self.x_att-1
                    self.current_y = self.y_att
                    self.level = "avancer"
                    self.toucher_defense(self.x_att-1,self.y_att)
                    return True
                else:
                    self.dans_leau_defense(self.x_att-1,self.y_att)
                    self.attaque[self.x_att-1][self.y_att] = -1
                    self.Hplateau[self.x_att-1][self.y_att] = -2
            else:
                self.recherche.pop(0)
                return self.trouver_direction()
            
        self.recherche.pop(0)
        return False
    
    def avancer(self):
        
        if self.direction[0] == 'vertical':
            if self.direction[1] == 'bas':
                if self.current_x+1 >= self.n or self.attaque[self.current_x+1][self.current_y] != 0 :
                    self.inversion()
                    return self.avancer()
                if self.Hplateau[self.current_x+1][self.current_y] == 1:
                    self.attaque[self.current_x+1][self.current_y] = 1
                    self.Hplateau[self.current_x+1][self.current_y] = -1
                    self.toucher_defense(self.current_x+1, self.current_y)
                    self.current_x += 1
                    return True
                else:
                    self.dans_leau_defense(self.current_x+1, self.current_y)
                    self.attaque[self.current_x+1][self.current_y] = -1
                    self.Hplateau[self.current_x+1][self.current_y] = -2
                    return False
                
            if self.direction[1] == 'haut':
                if self.current_x-1 < 0 or self.attaque[self.current_x-1][self.current_y] != 0:
                    self.inversion()
                    return self.avancer()
                if self.Hplateau[self.current_x-1][self.current_y] == 1:
                    self.attaque[self.current_x-1][self.current_y] = 1
                    self.Hplateau[self.current_x-1][self.current_y] = -1
                    self.toucher_defense(self.current_x-1, self.current_y)
                    self.current_x -= 1
                    return True
                else:
                    self.dans_leau_defense(self.current_x-1, self.current_y)
                    self.attaque[self.current_x-1][self.current_y] = -1
                    self.Hplateau[self.current_x-1][self.current_y] = -2
                    return False
        
        if self.direction[0] == 'horizontal':
            if self.direction[1] == 'droite':
                if self.current_y+1 >= self.n or self.attaque[self.current_x][self.current_y+1] != 0:
                    self.inversion()
                    return self.avancer()
                if self.Hplateau[self.current_x][self.current_y+1] == 1:
                    self.attaque[self.current_x][self.current_y+1] = 1
                    self.Hplateau[self.current_x][self.current_y+1] = -1
                    self.toucher_defense(self.current_x, self.current_y+1)
                    self.current_y += 1
                    return True
                else:
                    self.dans_leau_defense(self.current_x, self.current_y+1)
                    self.attaque[self.current_x][self.current_y+1] = -1
                    self.Hplateau[self.current_x][self.current_y+1] = -2
                    return False
                
            if self.direction[1] == 'gauche':
                if self.current_y-1 < 0 or self.attaque[self.current_x][self.current_y-1] != 0: 
                    self.inversion()
                    return self.avancer()
                if self.Hplateau[self.current_x][self.current_y-1] == 1:
                    self.attaque[self.current_x][self.current_y-1] = 1
                    self.Hplateau[self.current_x][self.current_y-1] = -1
                    self.toucher_defense(self.current_x, self.current_y-1)
                    self.current_y -= 1
                    return True
                else:
                    self.dans_leau_defense(self.current_x, self.current_y-1)
                    self.attaque[self.current_x][self.current_y-1] = -1
                    self.Hplateau[self.current_x][self.current_y-1] = -2
                    return False
                
    
    def attaquer(self):
        
        if self.level == "direction":
            self.trouver_direction()
            if self.Hest_coule() == True:
                self.mode = 'recherche'
                self.level = "direction"
            return
        
        if self.level == "avancer":
            if self.avancer() == False:
                self.inversion()
                
            if self.Hest_coule() == True:
                self.mode = 'recherche'
                self.level = 'direction'
                return
            
    def inversion(self):
        
        if self.direction[1] == 'droite':
            self.direction[1] = 'gauche'
            
        elif self.direction[1] == 'gauche':
            self.direction[1] = 'droite'
        
        elif self.direction[1] == 'haut':
            self.direction[1] = 'bas'
        
        elif self.direction[1] == 'bas':
            self.direction[1] = 'haut'
            
        self.current_x = self.x_att
        self.current_y = self.y_att
    
    def choix(self):
        
        self.choisir = [[0 for i in range(self.n)] for j in range(self.n)]
                
        x,y = self.choix_intelligent()
        
        if self.attaque[x][y] != 0:
            return self.choix()
            
        if self.Hplateau[x][y] == 1:
            self.toucher_defense(x, y)
            self.attaque[x][y] = 1
            self.Hplateau[x][y] = -1
            self.x_att = x
            self.y_att = y
            self.recherche = ['gauche','droite','haut','bas']
            rd.shuffle(self.recherche)
            self.mode = 'toucher'
        else:
            self.dans_leau_defense(x, y)
            self.attaque[x][y] = -1
            self.Hplateau[x][y] = -2
            
    def choix_intelligent(self):
        
        attaque = np.array(self.attaque)
        choix =  np.array(self.choisir)
        
        for bateau in self.positions_bateaux:
            n = len(bateau)
            for i in range(self.n):
                for j in range(self.n-n+1):
                    
                    if list(attaque[i,j:j+n]) == [0 for p in range(n)]:
                        choix[i,j:j+n] = [k+1 for k in list(choix[i,j:j+n])]
            
                    if list(attaque[j:j+n,i]) == [0 for p in range(n)]:
                        choix[j:j+n,i] = [k+1 for k in list(choix[j:j+n,i])]
                    
        """ STRATEGIE ANTI-RAF"""
        
        for i in range(self.n):
            if choix[0][i] > 0:
                choix[0][i] += 1
            if i > 0 and choix[i][0] > 0:
                choix[i][0] += 1
            if i > 0 and choix[i][-1] > 0:
                choix[i][-1] += 1
            if i < self.n - 1 and i > 0 and choix[-1][i] > 0:
                choix[-1][i] += 1

        maxi = choix.max()
        rep = []
        for i in range(self.n):
            for j in range(self.n):
                if choix[i,j] == maxi:
                    rep.append([i,j])

        return rep[rd.randint(0,len(rep)-1)]
    
    def Hattaquer(self,click):
        
        if self.partie_fini():
            self.fin()
            return False
        
        x,y = 0,0
        for index,elt in enumerate(self.liste):
            if click.x <= elt+60 and click.x >= elt:
                y = index
            if click.y <= elt+60 and click.y >= elt:
                x = index
                
        if self.Hattaque[x][y] != 0:
            return False
        
        if self.plateau[x][y] == 1:
            self.plateau[x][y] = -1 
            self.Hattaque[x][y] = 1
            self.toucher_attaque(x, y)
            if self.est_coule():
                tk.messagebox.showinfo(title="Alerte",message="Coulé")
        else:
            self.dans_leau_attaque(x, y)
            self.plateau[x][y] = -2
            self.Hattaque[x][y] = -1
            
        self.Botattaque()
            
    def Botattaque(self):
        
         if self.partie_fini():
            self.fin()
            return False
             
         mode = self.mode
         if mode == 'recherche':
             self.choix()
         if mode == 'toucher':
             self.attaquer()
    
    def fin(self):
        
        self.canv_att.unbind('<Button-1>')
        tk.Button(self,text="FIN",font=("Helvetica", 30),bg="light gray",command=self.afficher_resultat).place(x=1120,y=10)
        tk.messagebox.showinfo(title="Alerte",message="Fin de  la partie")
        
        for bateau in self.positions_bateaux:
            bateau.sort()
            if bateau[0][0] == bateau[1][0]: #meme ligne
                mil = self.liste[bateau[0][0]]
                self.canv_att.create_oval(self.liste[bateau[0][1]]+4,mil+10,self.liste[bateau[-1][1]]+56,mil+50,width=2,fill="grey")
            else: #meme colonne
                mil = self.liste[bateau[0][1]]
                self.canv_att.create_oval(mil+10,self.liste[bateau[0][0]]+4,mil+50,self.liste[bateau[-1][0]]+56,width=2,fill="grey")
        
    def afficher_resultat(self):
        
        for elt in self.winfo_children():
            elt.destroy()
            
        if len(self.positions_bateaux) == 0:
            Hstatut, statut = "VICTOIRE","DEFAITE"
        else:
            Hstatut, statut = "DEFAITE","VICTOIRE"
        tk.Label(self, text=Hstatut,font=("Helvetica", 35)).place(relx=0.4297,rely=0.0278)
        
        """ HUMAIN """
        
        Hcoup = self.nb_coup()
        Hreussite = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.Hattaque[i][j] == 1:
                    Hreussite += 1
        Hreussite = round(100*Hreussite/Hcoup)
        Hcoules = 5 - len(self.positions_bateaux)
        temps = round((time.time()-self.time_debut)/60)
        Hpoints = self.points(Hstatut, Hcoup, Hreussite, temps, 'humain')
        
        tk.Label(self, text="HUMAIN",font=("Arial", 25)).place(relx=0.2578,rely=0.1389)
        texte = f"Nombre de tours : {Hcoup}\nTaux de reussite : {Hreussite}%\nBateaux coulés : {Hcoules}\nTemps : {temps} min\nStatut : {Hstatut}\nPOINTS : {Hpoints}"
        tk.Label(self, text=texte,font=("Arial", 25)).place(relx=0.1797,rely=0.2778)
        
        """ ORDINATEUR """
        
        if statut == "VICTOIRE": coup = Hcoup
        else: coup = Hcoup-1
        reussite = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.attaque[i][j] == 1:
                    reussite += 1
        reussite = round(100*reussite/coup)
        coules = 5 - len(self.Hpositions_bateaux)
        points = self.points(statut, coup, reussite, temps, 'ordinateur')
        
        tk.Label(self, text="ORDINATEUR",font=("Arial", 25)).place(relx=0.6016,rely=0.1389)
        texte = f"Nombre de tours : {coup}\nTaux de reussite : {reussite}%\nBateaux coulés : {coules}\nTemps : {temps} min\nStatut : {statut}\nPOINTS : {points}"
        tk.Label(self, text=texte,font=("Arial", 25)).place(relx=0.5625,rely=0.2778)
        
        """ RESULTAT """
        
        score = Hpoints-points
        texte = f"SCORE : {score} pts"
        tk.Label(self, text=texte,font=("Arial", 25)).place(relx=0.4063,rely=0.6528)
        
        tk.Button(self,text="Continuer",font=("Helvetica", 30),borderwidth=4,command=self.continuer_partie).place(relx=0.25,rely=0.7778)
        tk.Button(self,text="Recommencer",font=("Helvetica", 30),borderwidth=4,command=self.recommencer_partie).place(relx=0.4141,rely=0.7778)
        tk.Button(self,text="Quitter",font=("Helvetica", 30),borderwidth=4,command=self.quitter_partie).place(relx=0.6484,rely=0.7778)
        
        """ PROJET DONNEES """
        
        
        db = mysql.connect(host="localhost",user='root',password='',db='test')
        cursor = db.cursor() 
        cursor.execute( ('SELECT victoire,defaite,score FROM bataille_navale WHERE bataille_navale.indice = %s'),(self.id,) )
        table = cursor.fetchall()
        victoire,defaite,scores = table[0]
        scores = json.loads(scores.decode('utf-8'))
        scores.append(score)
        cursor.close()
        
        cursor = db.cursor()
        if len(self.Hpositions_bateaux) == 0:
            cursor.execute(("UPDATE bataille_navale SET victoire=%s,score=%s WHERE bataille_navale.indice = %s"),(victoire+1,json.dumps(scores),self.id))
        else:
            cursor.execute(("UPDATE bataille_navale SET defaite=%s,score=%s WHERE bataille_navale.indice = %s"),(defaite+1,json.dumps(scores),self.id))
        db.commit()
        cursor.close()
        
        
        """ FIN DE PROJET """
        
    def points(self,statut,coup,reussite,temps,joueur):
        
        points = 0
        if statut == "VICTOIRE":
            points += 10
        else:
            points -= 10
        longueur = [2,3,3,4,5]
        if joueur == 'humain':
            for bateau in self.positions_bateaux:
                longueur.remove(len(bateau))
        else:
            for bateau in self.Hpositions_bateaux:
                longueur.remove(len(bateau))
        for chiffre in longueur:
            points += 2*(7-chiffre)
        points += 100 - coup*2
        points += reussite
        points += 20 - temps*2
        
        return points
    
    def quitter_partie(self):
        
        rep = tk.messagebox.askyesno(title="Alert",message="Etes vous sur ?")
        if rep == True:
            self.destroy()
            
    def continuer_partie(self):
            
        self.plateau = [[0 for i in range(self.n)] for j in range(self.n)]
        self.attaque = [[0 for i in range(self.n)] for j in range(self.n)]
        self.Hplateau = [[0 for i in range(self.n)] for j in range(self.n)]
        self.Hattaque = [[0 for i in range(self.n)] for j in range(self.n)]
        self.placer_bateaux()
        self.nettoyage()
        self.listes_positions_bateaux()
        self.mode = "recherche"
        self.level = "direction"
        
        self.definir_Hplateau()
        
        if rd.randint(0,1) == 1:
            self.Botattaque()
            
    def recommencer_partie(self):
        
        for elt in self.winfo_children():
            elt.destroy()
        
        self.plateau = [[0 for i in range(self.n)] for j in range(self.n)]
        self.attaque = [[0 for i in range(self.n)] for j in range(self.n)]
        self.Hplateau = [[0 for i in range(self.n)] for j in range(self.n)]
        self.Hattaque = [[0 for i in range(self.n)] for j in range(self.n)]
        self.placer_bateaux()
        self.nettoyage()
        self.listes_positions_bateaux()
        self.mode = "recherche"
        self.level = "direction"
        
        self.longueur = [2,3,3,4,5]
        self.map = []
        self.bateau = []
        self.json = {}
        self.create()
        
        if rd.randint(0,1) == 1:
            self.Botattaque()
    
Naval()