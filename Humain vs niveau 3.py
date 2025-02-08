import numpy as np
from random import randint,shuffle,choice

class Bataille_navale():
    
    def __init__(self):
        
        self.joueur = 0
        self.tour = 0
        
        self.plateau_1 = [[7,7,7,7,7,7,7,7,7,7,7,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,7,7,7,7,7,7,7,7,7,7,7]]
        self.plateau_2 = [[7,7,7,7,7,7,7,7,7,7,7,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,7,7,7,7,7,7,7,7,7,7,7]] 

    def placement_aleatoire_bateaux(self):
        
        self.plateau = np.array(self.plateau_2)
        self.liste_provisoire_bateaux = []
        for t in [5,4,3,3,2]:
            self.sens = ['haut','bas','droite','gauche']
            shuffle(self.sens)
            x,y = randint(1, 10),randint(1,10)
            self.placer_bateaux(t,x,y)
            self.contour()
        self.clean()
        return self.liste_provisoire_bateaux, self.plateau
            
    def placer_bateaux(self,t,x,y):
        
        if self.sens[0] == 'haut':
            if list(self.plateau[x-t:x,y]) == [0 for p in range(t)]:
                self.plateau[x-t:x,y] = [1 for p in range(t)]
                self.liste_provisoire_bateaux.append([(i,y) for i in range(x-t,x)])
                return True
                
        if self.sens[0] == 'bas':
            if list(self.plateau[x:x+t,y]) == [0 for p in range(t)]:
                self.plateau[x:x+t,y] = [1 for p in range(t)]
                self.liste_provisoire_bateaux.append([(i,y) for i in range(x,x+t)])
                return True
            
        if self.sens[0] == 'gauche':
            if list(self.plateau[x,y-t:y]) == [0 for p in range(t)]:
                self.plateau[x,y-t:y] = [1 for p in range(t)]
                self.liste_provisoire_bateaux.append([(x,i) for i in range(y-t,y)])
                return True
                
        if self.sens[0] == 'droite':
            if list(self.plateau[x,y:y+t]) == [0 for p in range(t)]:
                self.plateau[x,y:y+t] = [1 for p in range(t)]
                self.liste_provisoire_bateaux.append([(x,i) for i in range(y,y+t)])
                return True
                
        self.sens.pop(0)
        if len(self.sens) == 0:
            x,y = randint(1,10), randint(1,10)
            self.sens = ['haut','bas','droite','gauche']
        return self.placer_bateaux(t,x,y)
    
    def contour(self):
        
        for i in range(11):
            for j in range(11):
                if self.plateau[i][j] == 1:
                    if self.plateau[i-1][j] == 0:
                        self.plateau[i-1][j] = 2
                    if self.plateau[i+1][j] == 0:
                        self.plateau[i+1][j] = 2
                    if self.plateau[i][j-1] == 0:
                        self.plateau[i][j-1] = 2
                    if self.plateau[i][j+1] == 0:
                        self.plateau[i][j+1] = 2
    
    def clean(self):
        
        for i in range(11):
            for j in range(11):
                if self.plateau[i][j] == 2:
                    self.plateau[i][j] = 0   
    
    def tir_aleatoire_1(self): #tir aléatoirement sur le plateau 1
        
        x,y = self.tir_damier()
        if self.plateau_1[x][y] in [7,2,-1,-2]:
            self.tir_aleatoire_1()
        if self.plateau_1[x][y] == 1:
            self.plateau_1[x][y] = -1
            self.action_1 = 'couler'
            self.mode_1 = 'direction'
            self.x1,self.y1 = x,y
            self.new_x1,self.new_y1 = x,y
            self.sens_1 = ['haut','bas','droite','gauche']
            shuffle(self.sens_1)
        if self.plateau_1[x][y] == 0:
            self.plateau_1[x][y] = -2
            
    def tir_damier(self):
        
        liste = []
        for i in range(11):
            for j in range(11):
                if self.plateau_1[i][j] in [0,1]:
                    liste.append([i,j])
        x,y = choice(liste)
        while len(liste) > 0 and bool(self.plateau_1[x+1][y] in [7,2,0,1]) + bool(self.plateau_1[x][y+1] in [7,2,0,1]) + bool(self.plateau_1[x-1][y] in [7,2,0,1]) + bool(self.plateau_1[x][y-1] in [7,2,0,1]) != 4: 
            liste.remove([x,y])
            if len(liste) > 0: x,y = choice(liste)
        return x,y
            
    def trouver_direction_1(self): #trouver la direction du bateau touché sur le plateau 1
        
        if self.sens_1[0] == 'haut':
            if self.plateau_1[self.new_x1-1][self.new_y1] in [7,2,-1,-2]:
                self.sens_1.pop(0)
                return self.trouver_direction_1()
            if self.plateau_1[self.new_x1-1][self.new_y1] == 1:
                self.plateau_1[self.new_x1-1][self.new_y1] = -1
                self.mode_1 = 'continuer'
                self.direction_1 = 'haut'
                self.new_x1 -= 1
                return True
            else:
                self.plateau_1[self.new_x1-1][self.new_y1] = -2
        
        if self.sens_1[0] == 'bas':
            if self.plateau_1[self.new_x1+1][self.new_y1] in [7,2,-1,-2]:
                self.sens_1.pop(0)
                return self.trouver_direction_1()
            if self.plateau_1[self.new_x1+1][self.new_y1] == 1:
                self.plateau_1[self.new_x1+1][self.new_y1] = -1
                self.mode_1 = 'continuer'
                self.direction_1 = 'bas'
                self.new_x1 += 1
                return True
            else:
                self.plateau_1[self.new_x1+1][self.new_y1] = -2
        
        if self.sens_1[0] == 'gauche':
            if self.plateau_1[self.new_x1][self.new_y1-1] in [7,2,-1,-2]:
                self.sens_1.pop(0)
                return self.trouver_direction_1()
            if self.plateau_1[self.new_x1][self.new_y1-1] == 1:
                self.plateau_1[self.new_x1][self.new_y1-1] = -1
                self.mode_1 = 'continuer'
                self.direction_1 = 'gauche'
                self.new_y1 -= 1
                return True
            else:
                self.plateau_1[self.new_x1][self.new_y1-1] = -2
                
        if self.sens_1[0] == 'droite':
            if self.plateau_1[self.new_x1][self.new_y1+1] in [7,2,-1,-2]:
                self.sens_1.pop(0)
                return self.trouver_direction_1()
            if self.plateau_1[self.new_x1][self.new_y1+1] == 1:
                self.plateau_1[self.new_x1][self.new_y1+1] = -1
                self.mode_1 = 'continuer'
                self.direction_1 = 'droite'
                self.new_y1 += 1
                return True
            else:
                self.plateau_1[self.new_x1][self.new_y1+1] = -2
                
        self.sens_1.pop(0)
        return False
    
    def continuer_1(self):
        
        if self.direction_1 == 'haut':
            if self.plateau_1[self.new_x1-1][self.new_y1] in [7,2,-1,-2]:
                self.direction_1 = 'bas'
                self.new_x1 = self.x1
                return self.continuer_1()
            if self.plateau_1[self.new_x1-1][self.new_y1] == 1:
                self.plateau_1[self.new_x1-1][self.new_y1] = -1
                self.new_x1 -= 1
                return True
            if self.plateau_1[self.new_x1-1][self.new_y1] == 0:
                self.plateau_1[self.new_x1-1][self.new_y1] = -2
                self.direction_1 = 'bas'
                self.new_x1 = self.x1
                return False
                
        if self.direction_1 == 'bas':
            if self.plateau_1[self.new_x1+1][self.new_y1] in [7,2,-1,-2]:
                self.direction_1 = 'haut'
                self.new_x1 = self.x1
                return self.continuer_1()
            if self.plateau_1[self.new_x1+1][self.new_y1] == 1:
                self.plateau_1[self.new_x1+1][self.new_y1] = -1
                self.new_x1 += 1
                return True
            if self.plateau_1[self.new_x1+1][self.new_y1] == 0:
                self.plateau_1[self.new_x1+1][self.new_y1] = -2
                self.direction_1 = 'haut'
                self.new_x1 = self.x1
                return False
        
        if self.direction_1 == 'gauche':
            if self.plateau_1[self.new_x1][self.new_y1-1] in [7,2,-1,-2]:
                self.direction_1 = 'droite'
                self.new_y1 = self.y1
                return self.continuer_1()
            if self.plateau_1[self.new_x1][self.new_y1-1] == 1:
                self.plateau_1[self.new_x1][self.new_y1-1] = -1
                self.new_y1 -= 1
                return True
            if self.plateau_1[self.new_x1][self.new_y1-1] == 0:
                self.plateau_1[self.new_x1][self.new_y1-1] = -2
                self.direction_1 = 'droite'
                self.new_y1 = self.y1
                return False
        
        if self.direction_1 == 'droite':
            if self.plateau_1[self.new_x1][self.new_y1+1] in [7,2,-1,-2]:
                self.direction_1 = 'gauche'
                self.new_y1 = self.y1
                return self.continuer_1()
            if self.plateau_1[self.new_x1][self.new_y1+1] == 1:
                self.plateau_1[self.new_x1][self.new_y1+1] = -1
                self.new_y1 += 1
                return True
            if self.plateau_1[self.new_x1][self.new_y1+1] == 0:
                self.plateau_1[self.new_x1][self.new_y1+1] = -2
                self.direction_1 = 'gauche'
                self.new_y1 = self.y1
                return False
    
    def bateau_coule_1(self):
        
        for bateau in self.liste_bateaux_1:
            if [self.plateau_1[x][y] for x,y in bateau] == [-1 for p in range(len(bateau))]:
                self.contour_bateau_coule_1(bateau)
                self.liste_bateaux_1.remove(bateau)
                return True
        return False         
      
    def contour_bateau_coule_1(self,bateau):
        
        for x,y in bateau:
            if self.plateau_1[x+1][y] == 0:
                self.plateau_1[x+1][y] = 2
            if self.plateau_1[x-1][y] == 0:
                self.plateau_1[x-1][y] = 2
            if self.plateau_1[x][y+1] == 0:
                self.plateau_1[x][y+1] = 2
            if self.plateau_1[x][y-1] == 0:
                self.plateau_1[x][y-1] = 2
    
    def attaque_bateau_1(self):
        
        mode = self.mode_1
        if mode == 'direction':
            self.trouver_direction_1()
        if mode == 'continuer':
            self.continuer_1()
        if self.bateau_coule_1():
            self.action_1 = 'chercher'
    
    def placement_humain_bateaux(self): #permet au joueur humain de placer les bateaux sur le plateau 1
        
        self.afficher_plateau_1()
        self.plateau = np.array(self.plateau_1)
        self.liste_provisoire_bateaux = []        
        taille=[5,4,3,3,2]
        for t in taille:
            print("Bateau de taille",t)
            p,q = False,False
            while p == False or q == False:
                s = input("Vertical ou horizontal ? (Tapez 1 pour vertical ou 2 pour horizontal)")
                x = input("Ligne :")
                y = input("Colonne :")
                
                #traitement des erreurs
                if s.isnumeric() == True:
                    s = int(s) 
                if x.isnumeric() == True:
                    x = int(x)
                if y.isnumeric() == True:
                    y = int(y)   
                
                if s in [1,2] and x in [1,2,3,4,5,6,7,8,9,10] and y in [1,2,3,4,5,6,7,8,9,10]:
                    p = True
                                
                if s == 1 and list(self.plateau[x:x+t,y]) == [0 for p in range(t)]:
                    self.sens = s
                    q = True
                if s == 2 and list(self.plateau[x,y:y+t]) == [0 for p in range(t)]:
                    self.sens = s
                    q = True
                 
                if p == False or q == False:
                    print("❌Erreur!❌")
                    
            self.placer(t,x,y)  
            self.contour()
            self.afficher_plateau_1()
        self.clean()
        return self.liste_provisoire_bateaux,self.plateau
    
    def placer(self,t,x,y):
        
        if self.sens == 1:
            self.plateau[x:x+t,y] = [1 for p in range(t)]
            self.liste_provisoire_bateaux.append([(i,y) for i in range(x,x+t)])
        
        if self.sens == 2:
            self.plateau[x,y:y+t] = [1 for p in range(t)]
            self.liste_provisoire_bateaux.append([(x,i) for i in range(y,y+t)])
        
        self.plateau_1 = self.plateau
        
    def tir_humain(self):
        
        print("\nCoordonnées tir ?")
        h = False
        while h == False:
            x = input("Ligne :")
            y = input("Colonne :")
            
            #traitement des erreurs
            if x.isnumeric() == True:
                x = int(x)
            if y.isnumeric() == True:
                y = int(y)
            if x in [1,2,3,4,5,6,7,8,9,10] and y in [1,2,3,4,5,6,7,8,9,10] and self.plateau_2[x][y] not in [7,-1,-2]:
                h = True
            
            if h == False:
                print("❌Erreur!❌")              
                
        if self.plateau_2[x][y] == 0 or self.plateau_2[x][y] == 2:
            self.plateau_2[x][y] = -2  #tir manqué
        elif self.plateau_2[x][y] == 1:
            self.plateau_2[x][y] = -1 #touché    
    
    def bateau_coule_2(self):
        
        for bateau in self.liste_bateaux_2:
            if [self.plateau_2[x][y] for x,y in bateau] == [-1 for p in range(len(bateau))]:
                self.liste_bateaux_2.remove(bateau)
                print('\n💣Touché coulé !💣')
                return True
        return False  
    
    def partie_finie(self):
        
        self.gagnant = None
        if len(self.liste_bateaux_1) == 0:
            self.gagnant = 'joueur 2'
            return True
        if len(self.liste_bateaux_2) == 0:
            self.gagnant = 'joueur 1'
            return True
        return False
    
    def afficher_plateau_1(self):
        
        print (' ',end='\n')
        print('   1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔟')       
        for i in range (1,11):
            if i != 10:
                print('',i,'',end ='')
            else:
                print(i,'',end ='')
            for j in range (1,11):
                f = self.plateau_1[i][j]
                if f == 0 or f == 2:                  #eau et contour des bateaux
                    print('🟦',end ='')
                elif f == 1:                          #bateaux
                    print('⚫️',end='')
                elif f == -2:                         #tir manqué
                    print('✖️',end='')              
                elif f == -1:                         #touché
                    print('💥',end='')
            print (' ',end='\n')
            
    def afficher_plateau_cache(self):
        
        print (' ',end='\n')
        print('   1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔟')       
        for i in range (1,11):
            if i != 10:
                print('',i,'',end ='')
            else:
                print(i,'',end ='')
            for j in range (1,11):
                h = self.plateau_2[i][j]
                if h == 0 or h == 1 or h == 2:        #eau et contour des bateaux
                    print('🟦',end ='')
                elif h == -2:                          #manqué
                    print('✖️',end='')              
                elif h == -1:                         #touché
                    print('💥',end='')
            print (end='\n')
    
    def jeu(self):
        
        #choix aléatoire du premier joueur
        j = randint(1,2)
        self.joueur = j
        
        #placement des bateaux sur les deux plateaux
        
        self.liste_bateaux_1,self.plateau_1 = self.placement_humain_bateaux()
        self.liste_bateaux_2,self.plateau_2 = self.placement_aleatoire_bateaux()
        
        self.action_1 = 'chercher'
        
        while self.partie_finie() == False:
            if self.joueur == 1:
                self.tir_humain()
                print('\n')
                self.afficher_plateau_cache()
                self.bateau_coule_2()
                
            if self.joueur == 2:
                action_1 = self.action_1
                if action_1 == 'chercher':
                    self.tir_aleatoire_1()
                    self.afficher_plateau_1()
                if action_1 == 'couler':
                    self.attaque_bateau_1()
                    self.afficher_plateau_1()
            
            self.joueur = 3 - self.joueur
        
        print('\nLe',self.gagnant,'a gagné !')
        print("\nFIN\n")
        
Bataille_navale().jeu()
