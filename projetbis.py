"""
Mini-projet
Sujet 13
"""

import numpy as np
import random as rd
import matplotlib.pyplot as plt

class Naval:
    
    def __init__(self,n=10):
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
        
        #self.Hpositions_bateaux = [[(0, 1), (0, 2), (0, 3)], [(2, 1), (2, 2), (2, 3), (2, 4), (2, 5)], [(4, 5), (4, 6), (4, 7)], [(5, 2), (6, 2)], [(9, 4), (9, 5), (9, 6), (9, 7)]]
        #self.Hpositions_bateaux = [[(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)], [(6, 0), (7, 0), (8, 0), (9, 0)], [(9, 2), (9, 3), (9, 4)], [(9, 6), (9, 7), (9, 8)], [(3, 9), (4, 9)]]
        #for bateau in self.Hpositions_bateaux:
            #for elt in bateau:
                #self.Hplateau[elt[0]][elt[1]] = 1
        self.remplir_Hplateau()
        
        self.main()
        
    def afficher_plateau(self,plateau):
        """
        0 une case jamais touché
        1 une case contenant un bateau
        2 cases ou un bateau ne peut pas etre
        -1 une attaque arrivée dans l'eau
        -2 un bateau touché par une torpille
        
        for i in range(self.n):
            line = "|"
            for j in range(self.n):
                if self.plateau[i][j] == 0:
                    line += " |"
                if self.plateau[i][j] == -1:
                    line += "X|"
                if self.plateau[i][j] == 1:
                    line += "0|"
                if self.plateau[i][j] == -2: 
                    line += ".|"
            print(line)
        """
        #cmap = ListedColormap(["darkorange", "gold", "blue", "lawngreen", "lightseagreen"])
        plt.imshow(plateau)
        plt.show()

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
                if self.attaque[i][j] != 0 and abs(self.attaque[i][j]) == 1:
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
                    return True
                else:
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
                    return True
                else:
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
                    return True
                else:
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
                    return True
                else:
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
                    self.current_x += 1
                    return True
                else:
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
                    self.current_x -= 1
                    return True
                else:
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
                    self.current_y += 1
                    return True
                else:
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
                    self.current_y -= 1
                    return True
                else:
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
            self.attaque[x][y] = 1
            self.Hplateau[x][y] = -1
            self.x_att = x
            self.y_att = y
            self.recherche = ['gauche','droite','haut','bas']
            self.mode = 'toucher'
        else:
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

        maxi = choix.max()
        rep = []
        for i in range(self.n):
            for j in range(self.n):
                if choix[i,j] == maxi:
                    rep.append([i,j])

        return rep[rd.randint(0,len(rep)-1)]
    
    def remplir_Hplateau(self):
        #try:
        self.Hpositions_bateaux = []
        for i in range(5):
            liste = [(int(i[0]),int(i[1])) for i in input().split()]
            for elt in liste:
                self.Hplateau[elt[0]][elt[1]] = 1
            self.Hpositions_bateaux.append(liste)
        print(self.Hpositions_bateaux)
        """
        except:
            print("Erreur, reessayer !")
            return self.remplir_Hplateau()
        """
    
    def Hattaquer(self):
        try:
            x,y = [int(i) for i in input().split()]
        except ValueError:
            print("Erreur, ressayer !")
            return self.Hattaquer()
        if x < 0 or x >= self.n or y < 0 or y >= self.n:
            print("Coordoonnées hors du tableau")
            return self.Hattaquer()
        if self.Hattaque[x][y] != 0:
            print("Déja utiliser")
            return self.Hattaquer()
        if self.plateau[x][y] == 1:
            self.plateau[x][y] = -1
            self.Hattaque[x][y] = 1
            if self.est_coule():
                print("Coulé")
            else:
                print('Toucher')
        else:
            print('Raté')
            self.plateau[x][y] = -2
            self.Hattaque[x][y] = -1
            
    def main(self):
        
         while self.partie_fini() == False:
             
             self.Hattaquer()
             
             mode = self.mode
             if mode == 'recherche':
                 self.choix()
             if mode == 'toucher':
                 self.attaquer()
                 
             self.afficher_plateau(self.Hplateau)
             self.afficher_plateau(self.Hattaque)
             
            
         self.afficher_plateau(self.plateau)
         if len(self.Hpositions_bateaux) == 0:
             print("\nTu t'es fait fumé")
         if len(self.positions_bateaux) == 0:
             print("\nHeuresement ta de la chance")
            
Naval()