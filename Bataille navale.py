#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
from random import randint

class Bataille_navale():
    
    def __init__(self):
        
        self.joueur = 0
        
        #plateau de départ (7=contours et 0=cases vides)
        self.plateau_1 = [[7,7,7,7,7,7,7,7,7,7,7,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,7,7,7,7,7,7,7,7,7,7,7]]
        self.plateau_2 = [[7,7,7,7,7,7,7,7,7,7,7,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,7,7,7,7,7,7,7,7,7,7,7]]   
        
        self.coordonnees_1 = [] #couples de coordonnées associées au plateau 1
        self.coordonnees_2 = [] #couples de coordonnées associées au plateau 2
        for i in range(1,11):
            for j in range(1,11):
                self.coordonnees_1.append([i, j])
        for i in range(1,11):
            for j in range(1,11):
                self.coordonnees_2.append([i, j])
        
        #coordonnées des bateaux sur plateau 1
        self.porte_avion_1 = []
        self.croiseur_1 = []
        self.contre_torpilleur_1 = []
        self.sous_marin_1 = []
        self.torpilleur_1 = []
        
        #coordonnées des bateaux sur plateau 1
        self.porte_avion_2 = []
        self.croiseur_2 = []
        self.contre_torpilleur_2 = []
        self.sous_marin_2 = []
        self.torpilleur_2 = []
        
        #coordonnées des contours des bateaux sur le plateau 1
        self.porte_avion_contour_1 = []
        self.croiseur_contour_1 = []
        self.contre_torpilleur_contour_1 = []
        self.sous_marin_contour_1 = []
        self.torpilleur_contour_1 = []
        
        #coordonnées des contours des bateaux sur le plateau 2
        self.porte_avion_contour_2 = []
        self.croiseur_contour_2 = []
        self.contre_torpilleur_contour_2 = []
        self.sous_marin_contour_2 = []
        self.torpilleur_contour_2 = []
        
        self.case_1 = [] #coordonnées de la dernière case touchée sur le plateau 1
        self.case_2 = [] #coordonnées de la dernière case touchée sur le plateau 2     
    
    def possible_1(self,i,j,sens,taille): #vérifie la possibilité de placer le bateau sur le plateau 1
        if sens == 1: #vertical
            if i+taille-1 <= 10:
                a = i
                n = 0
                possible = True
                while n != taille and possible == True:
                    if self.plateau_1[a][j] == 0:
                        possible = True
                        a += 1
                        n += 1
                    else:
                        possible = False
                return possible
            else:
                return False
        elif sens == 2: #horizontal
            if j+taille-1 <= 10:
                a = j
                n = 0
                possible = True
                while n != taille and possible == True:
                    if self.plateau_1[i][a] == 0:
                        possible = True
                        a += 1
                        n += 1
                    else:
                        possible = False
                return possible
            else:
                return False 
    
    def possible_2(self,i,j,sens,taille): #vérifie la possibilité de placer le bateau sur le plateau 2
        if sens == 1: #vertical
            if i+taille-1 <= 10:
                a = i
                n = 0
                possible = True
                while n != taille and possible == True:
                    if self.plateau_2[a][j] == 0:
                        possible = True
                        a += 1
                        n += 1
                    else:
                        possible = False
                return possible
            else:
                return False
        elif sens == 2: #horizontal
            if j+taille-1 <= 10:
                a = j
                n = 0
                possible = True
                while n != taille and possible == True:
                    if self.plateau_2[i][a] == 0:
                        possible = True
                        a += 1
                        n += 1
                    else:
                        possible = False
                return possible
            else:
                return False
            
    def placement_humain_bateaux(self):
        a = []
        b = []
        taille=[5,4,3,3,2]
        for t in taille:
            print("Bateau de taille",t)
            p = False
            while p == False:
                s = int(input("Vertical ou horizontal ? (Tapez 1 pour vertical, tapez 2 pour horizontal)"))
                i = int(input("Ligne :"))
                j = int(input("Colonne :"))
                p = self.possible_1(i,j,s,t)
                if s not in [1,2]:
                    p = False
                if i not in [1,2,3,4,5,6,7,8,9,10] and j not in [1,2,3,4,5,6,7,8,9,10]:
                    p = False
                if p == False:
                    print("Erreur!")
            if s == 1: #vertical
                for k in range(t):
                    self.plateau_1[i+k][j] = 1
                    self.plateau_1[i+k][j+1] = 2
                    self.plateau_1[i+k][j-1] = 2
                    self.plateau_1[i-1][j] = 2
                    self.plateau_1[i+t][j] = 2   
                    if t == 5:
                        self.porte_avion_1.append([i+k,j])
                        self.porte_avion_contour_1.extend([[i+k,j+1],[i+k,j-1],[i-1,j],[i+t,j]])
                    elif t == 4:
                        self.croiseur_1.append([i+k,j])
                        self.croiseur_contour_1.extend([[i+k,j+1],[i+k,j-1],[i-1,j],[i+t,j]])
                    elif t == 3:
                        a.append([i+k,j])
                        b.extend([[i+k,j+1],[i+k,j-1],[i-1,j],[i+t,j]])
                    elif t == 2:
                        self.torpilleur_1.append([i+k,j])
                        self.torpilleur_contour_1.extend([[i+k,j+1],[i+k,j-1],[i-1,j],[i+t,j]])       
            elif s == 2: #horizontal
                for k in range(t):
                    self.plateau_1[i][j+k] = 1
                    self.plateau_1[i+1][j+k] = 2
                    self.plateau_1[i-1][j+k] = 2
                    self.plateau_1[i][j-1] = 2
                    self.plateau_1[i][j+t] = 2
                    if t == 5:
                        self.porte_avion_1.append([i,j+k])
                        self.porte_avion_contour_1.extend([[i+1,j+k],[i-1,j+k],[i,j-1],[i,j+t]])
                    elif t == 4:
                        self.croiseur_1.append([i,j+k])
                        self.croiseur_contour_1.extend([[i+1,j+k],[i-1,j+k],[i,j-1],[i,j+t]])
                    elif t == 3:
                        a.append([i,j+k])
                        b.extend([[i+1,j+k],[i-1,j+k],[i,j-1],[i,j+t]])
                    elif t == 2:
                        self.torpilleur_1.append([i,j+k])
                        self.torpilleur_contour_1.extend([[i+1,j+k],[i-1,j+k],[i,j-1],[i,j+t]])
            self.afficher_plateau_1()
        self.contre_torpilleur_1.extend([a[0],a[1],a[2]])
        self.sous_marin_1.append([a[3],a[4],a[5]])
        self.contre_torpilleur_contour_1.extend([b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7],b[8],b[9],b[10],b[11]])
        self.sous_marin_contour_1.extend([b[12],b[13],b[14],b[15],b[16],b[17],b[18],b[19],b[20],b[21],b[22],b[23]])
        
        c = []
        for element in self.porte_avion_1:
            if element not in c:
                c.append(element)
        self.porte_avion_1 = c
        d = []
        for element in self.croiseur_1:
            if element not in d:
                d.append(element)
        self.croiseur_1 = d
        e = []
        for element in self.contre_torpilleur_1:
            if element not in e:
                e.append(element)
        self.contre_torpilleur_1 = e
        f = []
        for element in self.sous_marin_1:
            if element not in f:
                f.append(element)
        self.sous_marin_1 = f
        g = []
        for element in self.torpilleur_1:
            if element not in g:
                g.append(element)
        self.porte_avion_1 = g
    
    def placement_aleatoire_bateaux_1(self): #place les bateaux sur le plateau 1
        a = []
        b = []
        taille=[5,4,3,3,2]
        for t in taille:
            p = False
            while p == False:
                i,j = random.randint(1,10),random.randint(1,10)
                s = random.randint(1,2)
                p = self.possible_1(i,j,s,t)
            if s == 1: #vertical
                for k in range(t):
                    self.plateau_1[i+k][j] = 1
                    self.plateau_1[i+k][j+1] = 2
                    self.plateau_1[i+k][j-1] = 2
                    self.plateau_1[i-1][j] = 2
                    self.plateau_1[i+t][j] = 2   
                    if t == 5:
                        self.porte_avion_1.append([i+k,j])
                        self.porte_avion_contour_1.extend([[i+k,j+1],[i+k,j-1],[i-1,j],[i+t,j]])
                    elif t == 4:
                        self.croiseur_1.append([i+k,j])
                        self.croiseur_contour_1.extend([[i+k,j+1],[i+k,j-1],[i-1,j],[i+t,j]])
                    elif t == 3:
                        a.append([i+k,j])
                        b.extend([[i+k,j+1],[i+k,j-1],[i-1,j],[i+t,j]])
                    elif t == 2:
                        self.torpilleur_1.append([i+k,j])
                        self.torpilleur_contour_1.extend([[i+k,j+1],[i+k,j-1],[i-1,j],[i+t,j]])       
            elif s == 2: #horizontal
                for k in range(t):
                    self.plateau_1[i][j+k] = 1
                    self.plateau_1[i+1][j+k] = 2
                    self.plateau_1[i-1][j+k] = 2
                    self.plateau_1[i][j-1] = 2
                    self.plateau_1[i][j+t] = 2
                    if t == 5:
                        self.porte_avion_1.append([i,j+k])
                        self.porte_avion_contour_1.extend([[i+1,j+k],[i-1,j+k],[i,j-1],[i,j+t]])
                    elif t == 4:
                        self.croiseur_1.append([i,j+k])
                        self.croiseur_contour_1.extend([[i+1,j+k],[i-1,j+k],[i,j-1],[i,j+t]])
                    elif t == 3:
                        a.append([i,j+k])
                        b.extend([[i+1,j+k],[i-1,j+k],[i,j-1],[i,j+t]])
                    elif t == 2:
                        self.torpilleur_1.append([i,j+k])
                        self.torpilleur_contour_1.extend([[i+1,j+k],[i-1,j+k],[i,j-1],[i,j+t]])
        self.contre_torpilleur_1.extend([a[0],a[1],a[2]])
        self.sous_marin_1.append([a[3],a[4],a[5]])
        self.contre_torpilleur_contour_1.extend([b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7],b[8],b[9],b[10],b[11]])
        self.sous_marin_contour_1.extend([b[12],b[13],b[14],b[15],b[16],b[17],b[18],b[19],b[20],b[21],b[22],b[23]])
        
        c = []
        for element in self.porte_avion_1:
            if element not in c:
                c.append(element)
        self.porte_avion_1 = c
        d = []
        for element in self.croiseur_1:
            if element not in d:
                d.append(element)
        self.croiseur_1 = d
        e = []
        for element in self.contre_torpilleur_1:
            if element not in e:
                e.append(element)
        self.contre_torpilleur_1 = e
        f = []
        for element in self.sous_marin_1:
            if element not in f:
                f.append(element)
        self.sous_marin_1 = f
        g = []
        for element in self.torpilleur_1:
            if element not in g:
                g.append(element)
        self.porte_avion_1 = g
                                           
    def placement_aleatoire_bateaux_2(self): #place les bateaux sur le plateau 2
        a = []
        b = []
        taille=[5,4,3,3,2]
        for t in taille:
            p = False
            while p == False:
                i,j = random.randint(1,10),random.randint(1,10)
                s = random.randint(1,2)
                p = self.possible_2(i,j,s,t)
            if s == 1: #vertical
                for k in range(t):
                    self.plateau_2[i+k][j] = 1
                    self.plateau_2[i+k][j+1] = 2
                    self.plateau_2[i+k][j-1] = 2
                    self.plateau_2[i-1][j] = 2
                    self.plateau_2[i+t][j] = 2
                    if t == 5:
                        self.porte_avion_2.append([i+k,j])
                        self.porte_avion_contour_2.extend([[i+k,j+1],[i+k,j-1],[i-1,j],[i+t,j]])
                    elif t == 4:
                        self.croiseur_2.append([i+k,j])
                        self.croiseur_contour_2.extend([[i+k,j+1],[i+k,j-1],[i-1,j],[i+t,j]])
                    elif t == 3:
                        a.append([i+k,j])
                        b.extend([[i+k,j+1],[i+k,j-1],[i-1,j],[i+t,j]])
                    elif t == 2:
                        self.torpilleur_2.append([i+k,j])
                        self.torpilleur_contour_2.extend([[i+k,j+1],[i+k,j-1],[i-1,j],[i+t,j]])
            elif s == 2: #horizontal
                for k in range(t):
                    self.plateau_2[i][j+k] = 1
                    self.plateau_2[i+1][j+k] = 2
                    self.plateau_2[i-1][j+k] = 2
                    self.plateau_2[i][j-1] = 2
                    self.plateau_2[i][j+t] = 2
                    if t == 5:
                        self.porte_avion_2.append([i,j+k])
                        self.porte_avion_contour_2.extend([[i+1,j+k],[i-1,j+k],[i,j-1],[i,j+t]])
                    elif t == 4:
                        self.croiseur_2.append([i,j+k])
                        self.croiseur_contour_2.extend([[i+1,j+k],[i-1,j+k],[i,j-1],[i,j+t]])
                    elif t == 3:
                        a.append([i,j+k])
                        b.extend([[i+1,j+k],[i-1,j+k],[i,j-1],[i,j+t]])
                    elif t == 2:
                        self.torpilleur_2.append([i,j+k])
                        self.torpilleur_contour_2.extend([[i+1,j+k],[i-1,j+k],[i,j-1],[i,j+t]])
        self.contre_torpilleur_2.extend([a[0],a[1],a[2]])
        self.sous_marin_2.append([a[3],a[4],a[5]])
        self.contre_torpilleur_contour_2.extend([b[0],b[1],b[2],b[3],b[4],b[5],b[6],b[7],b[8],b[9],b[10],b[11]])
        self.sous_marin_contour_2.extend([b[12],b[13],b[14],b[15],b[16],b[17],b[18],b[19],b[20],b[21],b[22],b[23]])
        
        c = []
        for element in self.porte_avion_2:
            if element not in c:
                c.append(element)
        self.porte_avion_2 = c
        d = []
        for element in self.croiseur_2:
            if element not in d:
                d.append(element)
        self.croiseur_2 = d
        e = []
        for element in self.contre_torpilleur_2:
            if element not in e:
                e.append(element)
        self.contre_torpilleur_2 = e
        f = []
        for element in self.sous_marin_2:
            if element not in f:
                f.append(element)
        self.sous_marin_2 = f
        g = []
        for element in self.torpilleur_2:
            if element not in g:
                g.append(element)
        self.porte_avion_2 = g
    
    def tir_humain(self):
        h = False
        while h == False:
            i = int(input("Ligne :"))
            j = int(input("Colonne :"))
            h = True
            if i not in [1,2,3,4,5,6,7,8,9,10] and j not in [1,2,3,4,5,6,7,8,9,10]:
                h = False
            if ([i,j]) not in self.coordonnees_2:
                h = False
            if h == False:
                print("Erreur!")
        if self.plateau_2[i][j] == 0 or self.plateau_2[i][j] == 2:
            self.plateau_2[i][j] = 3  #tir manqué
            self.case_2 = []
            t = 3
        elif self.plateau_2[i][j] == 1:
            self.plateau_2[i][j] = -1 #touché
            self.case_2 = [i,j]
            t = -1
        self.coordonnees_2.remove([i,j])
        return t

    
    def tir_aleatoire_1(self): #tir sur plateau 1
        n = random.randint(0,len(self.coordonnees_1)-1)
        coordonnees = self.coordonnees_1[n]
        i,j = coordonnees[0],coordonnees[1]
        x = self.plateau_1[i][j]
        if x == 0 or x == 2:
            self.plateau_1[i][j] = 3  #tir manqué
            self.case_1 = []
            t = 3
        elif x == 1:
            self.plateau_1[i][j] = -1 #touché
            self.case_1 = [i,j]
            t = -1
        self.coordonnees_1.remove([i,j])
        return t
        
    def tir_aleatoire_2(self): #tir sur plateau 2
        n = random.randint(0,len(self.coordonnees_2)-1)
        coordonnees = self.coordonnees_2[n]
        i,j = coordonnees[0],coordonnees[1]
        y = self.plateau_2[i][j]
        if y == 0 or y == 2:
            self.plateau_2[i][j] = 3  #tir manqué
            self.case_2 = []
            t = 3
        elif y == 1:
            self.plateau_2[i][j] = -1 #touché
            self.case_2 = [i,j]
            t = -1
        self.coordonnees_2.remove([i,j])
        return t
    
    def tir_chercheur_1(self): #tir sur le plateau 1
        a = []
        i,j = self.case_1[0],self.case_1[1]
        if ([i-1,j]) in self.coordonnees_1:
            a.append([i-1,j])
        elif ([i+1,j]) in self.coordonnees_1:
            a.append([i+1,j])
        elif ([i,j-1]) in self.coordonnees_1:
            a.append([i,j-1])
        elif ([i,j+1]) in self.coordonnees_1:
            a.append([i,j+1])
        if a != []:
            b = random.choice(a)
            i,j = b[0],b[1]
            if self.plateau_1[i][j] == 0 or self.plateau_1[i][j] == 2:
                self.plateau_1[i][j] = 3
            elif self.plateau_1[i][j] == 1:
                self.plateau_1[i][j] == -1
                self.case_1 = [i,j]
            self.coordonnees_1.remove([i,j])
        
    def tir_chercheur_2(self): #tir sur plateau 2
        a = []
        i,j = self.case_2[0],self.case_2[1]
        if ([i-1,j]) in self.coordonnees_2:
            a.append([i-1,j])
        elif ([i+1,j]) in self.coordonnees_2:
            a.append([i+1,j])
        elif ([i,j-1]) in self.coordonnees_2:
            a.append([i,j-1])
        elif ([i,j+1]) in self.coordonnees_2:
            a.append([i,j+1])
        if a != []:
            b = random.choice(a)
            i,j = b[0],b[1]
            if self.plateau_2[i][j] == 0 or self.plateau_2[i][j] == 2:
                self.plateau_2[i][j] = 3
            elif self.plateau_2[i][j] == 1:
                self.plateau_2[i][j] == -1
                self.case_2 = [i,j]
            self.coordonnees_2.remove([i,j])
    
    def bateaux_coulés_1(self): #vérifie si un bateau est coulé sur le plateau 1
        cpt = 0
        for k in range(5):
            a = self.porte_avion_1[k]
            i,j = a[0],a[1]
            if self.plateau_1[i][j] == -1:
                cpt += 1
            if cpt == 5:
                porte_avion = 0 #coulé
                self.case_1 = []
            else:
                porte_avion = 1 #pas coulé
        cpt = 0
        for k in range(4):
            a = self.croiseur_1[k]
            i,j = a[0],a[1]
            if self.plateau_1[i][j] == -1:
                cpt += 1
            if cpt == 4:
                croiseur = 0 #coulé
                self.case_1 = []
            else:
                croiseur = 1 #pas coulé
        cpt = 0
        for k in range(3):
            a = self.contre_torpilleur_1[k]
            i,j = a[0],a[1]
            if self.plateau_1[i][j] == -1:
                cpt += 1
            if cpt == 3:
                contre_torpilleur = 0 #coulé
                self.case_1 = []
            else:
                contre_torpilleur = 1 #pas coulé
        cpt = 0
        for k in range(3):
            a = self.sous_marin_1[k]
            i,j = a[0],a[1]
            if self.plateau_1[i][j] == -1:
                cpt += 1
            if cpt == 3:
                sous_marin = 0 #coulé
                self.case_1 = []
            else:
                sous_marin = 1 #pas coulé
        cpt = 0
        for k in range(2):
            a = self.torpilleur_1[k]
            i,j = a[0],a[1]
            if self.plateau_1[i][j] == -1:
                cpt += 1
            if cpt == 2:
                torpilleur = 0 #coulé
                self.case_1 = []
            else:
                torpilleur = 1 #pas coulé
        coule = [porte_avion,croiseur,contre_torpilleur,sous_marin,torpilleur]
        return coule
                
    def bateaux_coulés_2(self): #vérifie si un bateau est coulé sur le plateau 2
        cpt = 0
        for k in range(5):
            a = self.porte_avion_2[k]
            i,j = a[0],a[1]
            if self.plateau_2[i][j] == -1:
                cpt += 1
            if cpt == 5:
                porte_avion = 0 #coulé
                self.case_2 = []
            else:
                porte_avion = 1 #pas coulé
        cpt = 0
        for k in range(4):
            a = self.croiseur_2[k]
            i,j = a[0],a[1]
            if self.plateau_2[i][j] == -1:
                cpt += 1
            if cpt == 4:
                croiseur = 0 #coulé
                self.case_2 = []
            else:
                croiseur = 1 #pas coulé
        cpt = 0
        for k in range(3):
            a = self.contre_torpilleur_2[k]
            i,j = a[0],a[1]
            if self.plateau_2[i][j] == -1:
                cpt += 1
            if cpt == 3:
                contre_torpilleur = 0 #coulé
                self.case_2 = []
            else:
                contre_torpilleur = 1 #pas coulé
        cpt = 0
        for k in range(3):
            a = self.sous_marin_2[k]
            i,j = a[0],a[1]
            if self.plateau_2[i][j] == -1:
                cpt += 1
            if cpt == 3:
                sous_marin = 0 #coulé
                self.case_2 = []
            else:
                sous_marin = 1 #pas coulé
        cpt = 0
        for k in range(2):
            a = self.torpilleur_2[k]
            i,j = a[0],a[1]
            if self.plateau_2[i][j] == -1:
                cpt += 1
            if cpt == 2:
                torpilleur = 0 #coulé
                self.case_2 = []
            else:
                torpilleur = 1 #pas coulé
        coule = [porte_avion,croiseur,contre_torpilleur,sous_marin,torpilleur]
        return coule
        
    def afficher_plateau_1(self):
        print('   1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔟')       
        for i in range (1,11):
            self.plateau_1[0][i] = 7
            if i != 10:
                if self.plateau_1[0][i] == 7:
                    print('',i,'',end ='')
            else:
                if self.plateau_1[0][i] == 7:
                    print(i,'',end ='')
            for j in range (1,11):
                f = self.plateau_1[i][j]
                if f == 0 or f == 2:                  #eau et contour des bateaux
                    print('🟦',end ='')
                elif f == 1:                          #bateaux
                    print('⚫️',end='')
                elif f == 3:                          #tir manqué
                    print('✖️',end='')              
                elif f == -1:                         #touché
                    print('💥',end='')
            print ('',end='\n')
            
    def afficher_plateau_2(self):
        print('   1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔟')
        for i in range (1,11):
            self.plateau_2[0][i] = 7
            if i != 10:
                if self.plateau_2[0][i] == 7:
                    print('',i,'',end ='')
            else:
                if self.plateau_2[0][i] == 7:
                    print(i,'',end ='')
            for j in range (1,11):
                g = self.plateau_2[i][j]
                if g == 0 or g == 2:                  #eau
                    print('🟦',end ='')
                elif g == 1:                          #bateau
                    print('⚪️',end='')
                elif g == 3:                          #manqué
                    print('✖️',end='')              
                elif g == -1:                         #touché
                    print('💥',end='')
            print ('',end='\n')
    
    def afficher_plateau_cache(self):
        print('   1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔟')
        for i in range (1,11):
            self.plateau_2[0][i] = 7
            if i != 10:
                if self.plateau_2[0][i] == 7:
                    print('',i,'',end ='')
            else:
                if self.plateau_2[0][i] == 7:
                    print(i,'',end ='')
            for j in range (1,11):
                h = self.plateau_2[i][j]
                if h == 0 or h == 1 or h == 2:        #eau
                    print('🟦',end ='')
                elif h == 3:                          #manqué
                    print('✖️',end='')              
                elif h == -1:                         #touché
                    print('💥',end='')
            print ('',end='\n')
    
    def check_gagnant(self):
        gagnant = None
        self.compteur1 = 0
        self.compteur2 = 0
        for i in range(1,11):
            for j in range (1,11):
                if self.plateau_1[i][j] == -1:
                    self.compteur1 += 1
                if self.plateau_2[i][j] == -1:
                    self.compteur2 += 1
        if self.compteur1 == 17 or self.compteur2 == 17:
            gagnant = True
        return gagnant
    
    def gameover(self):
        if self.compteur1 == 17:
            print("Game over")
            self.afficher_plateau_1()
            print('',end='\n')
            self.afficher_plateau_2()
            print("Joueur 2 a gagné !")
        elif self.compteur2 == 17:
            print("Game over")
            self.afficher_plateau_1()
            print ('',end='\n')
            self.afficher_plateau_2()
            print("Joueur 1 a gagné !")
    
    def jeu(self,niveau):
        j = random.randint(1,2)
        self.joueur = j
            
        if niveau == 0:
            self.placement_aleatoire_bateaux_1()
            self.placement_aleatoire_bateaux_2()
            while self.check_gagnant() == None:
                if self.joueur == 1:     
                    self.tir_aleatoire_2()
                else:
                    self.tir_aleatoire_1()
                self.joueur = 3 - self.joueur
            self.gameover()
            
        if niveau == 1:
            self.placement_aleatoire_bateaux_1()
            self.placement_aleatoire_bateaux_2()
            while self.bateaux_coulés_1() != [0,0,0,0,0] or self.bateaux_coulés_2() != [0,0,0,0,0]:   
                if self.joueur == 1:
                    if self.case_2 == []:
                        self.tir_aleatoire_2()
                    elif self.case_2 != []:
                        self.tir_chercheur_2()
                else:
                    if self.case_1 == []:
                        self.tir_aleatoire_1()
                    elif self.case_1 != []:
                        self.tir_chercheur_1()
                self.joueur = 3 - self.joueur
            self.gameover()            
        
        #if niveau == 2:
            
        
        if niveau == 4:
            self.afficher_plateau_1()
            self.placement_humain_bateaux()
            self.placement_aleatoire_bateaux_2()
            print('',end='\n')
            while self.check_gagnant() == None:
                if self.joueur == 1:
                    print("Coordonnées tir ?")
                    self.tir_humain()
                else:
                    self.tir_aleatoire_1()
                self.afficher_plateau_1()
                print ('',end='\n')
                self.afficher_plateau_cache()
                print ('',end='\n')
                print ('',end='\n')
                self.joueur = 3 - self.joueur
            self.gameover()
            
res=Bataille_navale()
res.jeu(1)


# In[ ]:




