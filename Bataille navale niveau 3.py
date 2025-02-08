from random import randint,shuffle,choice
import numpy as np
import matplotlib.pyplot as plt
import time

class Bataille_navale():
    
    def __init__(self):
        
        self.tour = 0
        
        self.plateau_1 = [[7,7,7,7,7,7,7,7,7,7,7,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,7,7,7,7,7,7,7,7,7,7,7]]
        self.plateau_2 = [[7,7,7,7,7,7,7,7,7,7,7,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,7,7,7,7,7,7,7,7,7,7,7]] 
        
        self.liste_bateaux_1,self.plateau_1 = self.placer_bateaux(self.plateau_1)
        self.liste_bateaux_2,self.plateau_2 = self.placer_bateaux(self.plateau_2)
        
        self.type1 = 'chercher'
        self.type2 = 'chercher'
        self.sens1 = ['haut','bas','gauche','droite']
        self.sens2 = ['haut','bas','gauche','droite']

        
        """
        Pour voir le placement des bateaux
        """
        """
        plt.imshow(self.plateau_1)
        plt.show()
        
        plt.imshow(self.plateau_2)
        plt.show()
        """
        
        self.main()
        
    def placer_bateaux(self,plateau):
        
        self.plateau = np.array(plateau)
        self.liste_provisoire_bateaux = []
        for i in [5,4,3,3,2]:
            self.sens = ['haut','bas','droite','gauche']
            shuffle(self.sens)
            x,y = randint(1, 10),randint(1,10)
            self.placer_bateau(i,x,y)
            self.contour()
        self.clean()
        return self.liste_provisoire_bateaux, self.plateau
            
    def placer_bateau(self,n,x,y):
        
        if self.sens[0] == 'haut':
            if list(self.plateau[x-n:x,y]) == [0 for p in range(n)]:
                self.plateau[x-n:x,y] = [1 for p in range(n)]
                self.liste_provisoire_bateaux.append([(i,y) for i in range(x-n,x)])
                return True
                
        if self.sens[0] == 'bas':
            if list(self.plateau[x:x+n,y]) == [0 for p in range(n)]:
                self.plateau[x:x+n,y] = [1 for p in range(n)]
                self.liste_provisoire_bateaux.append([(i,y) for i in range(x,x+n)])
                return True
            
        if self.sens[0] == 'gauche':
            if list(self.plateau[x,y-n:y]) == [0 for p in range(n)]:
                self.plateau[x,y-n:y] = [1 for p in range(n)]
                self.liste_provisoire_bateaux.append([(x,i) for i in range(y-n,y)])
                return True
                
        if self.sens[0] == 'droite':
            if list(self.plateau[x,y:y+n]) == [0 for p in range(n)]:
                self.plateau[x,y:y+n] = [1 for p in range(n)]
                self.liste_provisoire_bateaux.append([(x,i) for i in range(y,y+n)])
                return True
                
        self.sens.pop(0)
        if len(self.sens) == 0:
            x,y = randint(1,10), randint(1,10)
            self.sens = ['haut','bas','droite','gauche']
        return self.placer_bateau(n,x,y)
    
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
    
    def partie_finie(self):
        if len(self.liste_bateaux_1) == 0 or len(self.liste_bateaux_2) == 0:
            return True
        return False
    
    def attaque_1(self):
        "Le plateau 1 attaque le plateau 2"
        
        x,y = randint(1,10),randint(1,10)
        if self.plateau_2[x][y] in [7,-2,2,-1]:
            self.attaque_1()
        if self.plateau_2[x][y] == 1:
            self.plateau_2[x][y] = -1
            self.type1 = 'couler'
            self.mode1 = 'direction'
            self.x1,self.y1 = x,y
            self.new_x1,self.new_y1 = x,y
            self.sens1 = ['haut','bas','droite','gauche']
            shuffle(self.sens1)
        if self.plateau_2[x][y] == 0:
            self.plateau_2[x][y] = -2
            
    def attaque_2(self):
        "Le plateau 2 attaque le plateau 1"
        
        x,y = self.tir_damier()
        if self.plateau_1[x][y] in [7,-1,-2,2]:
            self.attaque_2()
        if self.plateau_1[x][y] == 1:
            self.plateau_1[x][y] = -1
            self.type2 = 'couler'
            self.mode2 = 'direction'
            self.x2,self.y2 = x,y
            self.new_x2,self.new_y2 = x,y
            self.sens2 = ['haut','bas','droite','gauche']
            shuffle(self.sens2)
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
            
    def trouver_direction1(self):
        "Trouver la direction du bateau touché sur le plateau 2 par le 1"
        
        if self.sens1[0] == 'haut':
            if self.plateau_2[self.new_x1-1][self.new_y1] in [7,-2,-1,2]:
                self.sens1.pop(0)
                return self.trouver_direction1()
            if self.plateau_2[self.new_x1-1][self.new_y1] == 1:
                self.plateau_2[self.new_x1-1][self.new_y1] = -1
                self.mode1 = 'continuer'
                self.direction1 = 'haut'
                self.new_x1 -= 1
                return True
            else:
                self.plateau_2[self.new_x1-1][self.new_y1] = -2
        
        if self.sens1[0] == 'bas':
            if self.plateau_2[self.new_x1+1][self.new_y1] in [7,-2,-1,2]:
                self.sens1.pop(0)
                return self.trouver_direction1()
            if self.plateau_2[self.new_x1+1][self.new_y1] == 1:
                self.plateau_2[self.new_x1+1][self.new_y1] = -1
                self.mode1 = 'continuer'
                self.direction1 = 'bas'
                self.new_x1 += 1
                return True
            else:
                self.plateau_2[self.new_x1+1][self.new_y1] = -2
        
        if self.sens1[0] == 'gauche':
            if self.plateau_2[self.new_x1][self.new_y1-1] in [7,-2,-1,2]:
                self.sens1.pop(0)
                return self.trouver_direction1()
            if self.plateau_2[self.new_x1][self.new_y1-1] == 1:
                self.plateau_2[self.new_x1][self.new_y1-1] = -1
                self.mode1 = 'continuer'
                self.direction1 = 'gauche'
                self.new_y1 -= 1
                return True
            else:
                self.plateau_2[self.new_x1][self.new_y1-1] = -2
                
        if self.sens1[0] == 'droite':
            if self.plateau_2[self.new_x1][self.new_y1+1] in [7,-2,-1,2]:
                self.sens1.pop(0)
                return self.trouver_direction1()
            if self.plateau_2[self.new_x1][self.new_y1+1] == 1:
                self.plateau_2[self.new_x1][self.new_y1+1] = -1
                self.mode1 = 'continuer'
                self.direction1 = 'droite'
                self.new_y1 += 1
                return True
            else:
                self.plateau_2[self.new_x1][self.new_y1+1] = -2
                
        self.sens1.pop(0)
        return False
                
    def trouver_direction2(self):
        "Trouver la direction du bateau touché sur le plateau 1 par le 2"
        
        if self.sens2[0] == 'haut':
            if self.plateau_1[self.new_x2-1][self.new_y2] in [7,-2,-1,2]:
                self.sens2.pop(0)
                return self.trouver_direction2()
            if self.plateau_1[self.new_x2-1][self.new_y2] == 1:
                self.plateau_1[self.new_x2-1][self.new_y2] = -1
                self.mode2 = 'continuer'
                self.direction2 = 'haut'
                self.new_x2 -= 1
                return True
            else:
                self.plateau_1[self.new_x2-1][self.new_y2] = -2
        
        if self.sens2[0] == 'bas':
            if self.plateau_1[self.new_x2+1][self.new_y2] in [7,-2,-1,2]:
                self.sens2.pop(0)
                return self.trouver_direction2()
            if self.plateau_1[self.new_x2+1][self.new_y2] == 1:
                self.plateau_1[self.new_x2+1][self.new_y2] = -1
                self.mode2 = 'continuer'
                self.direction2 = 'bas'
                self.new_x2 += 1
                return True
            else:
                self.plateau_1[self.new_x2+1][self.new_y2] = -2
        
        if self.sens2[0] == 'gauche':
            if self.plateau_1[self.new_x2][self.new_y2-1] in [7,-2,-1,2]:
                self.sens2.pop(0)
                return self.trouver_direction2()
            if self.plateau_1[self.new_x2][self.new_y2-1] == 1:
                self.plateau_1[self.new_x2][self.new_y2-1] = -1
                self.mode2 = 'continuer'
                self.direction2 = 'gauche'
                self.new_y2 -= 1
                return True
            else:
                self.plateau_1[self.new_x2][self.new_y2-1] = -2
                
        if self.sens2[0] == 'droite':
            if self.plateau_1[self.new_x2][self.new_y2+1] in [7,-2,-1,2]:
                self.sens2.pop(0)
                return self.trouver_direction2()
            if self.plateau_1[self.new_x2][self.new_y2+1] == 1:
                self.plateau_1[self.new_x2][self.new_y2+1] = -1
                self.mode2 = 'continuer'
                self.direction2 = 'droite'
                self.new_y2 += 1
                return True
            else:
                self.plateau_1[self.new_x2][self.new_y2+1] = -2
                
        self.sens2.pop(0)
        return False
                
    def continuer1(self):
        
        if self.direction1 == 'haut':
            if self.plateau_2[self.new_x1-1][self.new_y1] in [-1,-2,7,2]:
                self.direction1 = 'bas'
                self.new_x1 = self.x1
                return self.continuer1()
            if self.plateau_2[self.new_x1-1][self.new_y1] == 1:
                self.plateau_2[self.new_x1-1][self.new_y1] = -1
                self.new_x1 -= 1
                return True
            if self.plateau_2[self.new_x1-1][self.new_y1] == 0:
                self.plateau_2[self.new_x1-1][self.new_y1] = -2
                self.direction1 = 'bas'
                self.new_x1 = self.x1
                return False
                
        if self.direction1 == 'bas':
            if self.plateau_2[self.new_x1+1][self.new_y1] in [-1,-2,7,2]:
                self.direction1 = 'haut'
                self.new_x1 = self.x1
                return self.continuer1()
            if self.plateau_2[self.new_x1+1][self.new_y1] == 1:
                self.plateau_2[self.new_x1+1][self.new_y1] = -1
                self.new_x1 += 1
                return True
            if self.plateau_2[self.new_x1+1][self.new_y1] == 0:
                self.plateau_2[self.new_x1+1][self.new_y1] = -2
                self.direction1 = 'haut'
                self.new_x1 = self.x1
                return False
        
        if self.direction1 == 'gauche':
            if self.plateau_2[self.new_x1][self.new_y1-1] in [-1,-2,7,2]:
                self.direction1 = 'droite'
                self.new_y1 = self.y1
                return self.continuer1()
            if self.plateau_2[self.new_x1][self.new_y1-1] == 1:
                self.plateau_2[self.new_x1][self.new_y1-1] = -1
                self.new_y1 -= 1
                return True
            if self.plateau_2[self.new_x1][self.new_y1-1] == 0:
                self.plateau_2[self.new_x1][self.new_y1-1] = -2
                self.direction1 = 'droite'
                self.new_y1 = self.y1
                return False
        
        if self.direction1 == 'droite':
            if self.plateau_2[self.new_x1][self.new_y1+1] in [-1,-2,7,2]:
                self.direction1 = 'gauche'
                self.new_y1 = self.y1
                return self.continuer1()
            if self.plateau_2[self.new_x1][self.new_y1+1] == 1:
                self.plateau_2[self.new_x1][self.new_y1+1] = -1
                self.new_y1 += 1
                return True
            if self.plateau_2[self.new_x1][self.new_y1+1] == 0:
                self.plateau_2[self.new_x1][self.new_y1+1] = -2
                self.direction1 = 'gauche'
                self.new_y1 = self.y1
                return False
                
    def continuer2(self):
        
        if self.direction2 == 'haut':
            if self.plateau_1[self.new_x2-1][self.new_y2] in [-1,-2,7,2]:
                self.direction2 = 'bas'
                self.new_x2 = self.x2
                return self.continuer2()
            if self.plateau_1[self.new_x2-1][self.new_y2] == 1:
                self.plateau_1[self.new_x2-1][self.new_y2] = -1
                self.new_x2 -= 1
                return True
            if self.plateau_1[self.new_x2-1][self.new_y2] == 0:
                self.plateau_1[self.new_x2-1][self.new_y2] = -2
                self.direction2 = 'bas'
                self.new_x2 = self.x2
                return False
                
        if self.direction2 == 'bas':
            if self.plateau_1[self.new_x2+1][self.new_y2] in [-1,-2,7,2]:
                self.direction2 = 'haut'
                self.new_x2 = self.x2
                return self.continuer2()
            if self.plateau_1[self.new_x2+1][self.new_y2] == 1:
                self.plateau_1[self.new_x2+1][self.new_y2] = -1
                self.new_x2 += 1
                return True
            if self.plateau_1[self.new_x2+1][self.new_y2] == 0:
                self.plateau_1[self.new_x2+1][self.new_y2] = -2
                self.direction2 = 'haut'
                self.new_x2 = self.x2
                return False
        
        if self.direction2 == 'gauche':
            if self.plateau_1[self.new_x2][self.new_y2-1] in [-1,-2,7,2]:
                self.direction2 = 'droite'
                self.new_y2 = self.y2
                return self.continuer2()
            if self.plateau_1[self.new_x2][self.new_y2-1] == 1:
                self.plateau_1[self.new_x2][self.new_y2-1] = -1
                self.new_y2 -= 1
                return True
            if self.plateau_1[self.new_x2][self.new_y2-1] == 0:
                self.plateau_1[self.new_x2][self.new_y2-1] = -2
                self.direction2 = 'droite'
                self.new_y2 = self.y2
                return False
        
        if self.direction2 == 'droite':
            if self.plateau_1[self.new_x2][self.new_y2+1] in [-1,-2,7,2]:
                self.direction2 = 'gauche'
                self.new_y2 = self.y2
                return self.continuer2()
            if self.plateau_1[self.new_x2][self.new_y2+1] == 1:
                self.plateau_1[self.new_x2][self.new_y2+1] = -1
                self.new_y2 += 1
                return True
            if self.plateau_1[self.new_x2][self.new_y2+1] == 0:
                self.plateau_1[self.new_x2][self.new_y2+1] = -2
                self.direction2 = 'gauche'
                self.new_y2 = self.y2
                return False
                
    def le_1_a_coule_bateau(self):
        "1 a t il coule un bateau de 2 ?"
        for bateau in self.liste_bateaux_2:
            if [self.plateau_2[x][y] for x,y in bateau] == [-1 for _ in range(len(bateau))]:
                self.contour_bateau_2_est_coule(bateau)
                self.liste_bateaux_2.remove(bateau)
                return True
        return False
    
    def le_2_a_coule_bateau(self):
        "2 a t il coule un bateau de 1 ?"
        for bateau in self.liste_bateaux_1:
            if [self.plateau_1[x][y] for x,y in bateau] == [-1 for _ in range(len(bateau))]:
                self.contour_bateau_1_est_coule(bateau)
                self.liste_bateaux_1.remove(bateau)
                return True
        return False
            
    def attaque_bateau1(self):
        "Le plateau 1 attaque un bateau trouvé du plateau 2"
        
        if self.mode1 == 'direction':
            self.trouver_direction1()
        else:
            self.continuer1()
        if self.le_1_a_coule_bateau():
            self.type1 = 'chercher'
            
    def attaque_bateau2(self):
        "Le plateau 1 attaque un bateau trouvé du plateau 2"
        
        if self.mode2 == 'direction':
            self.trouver_direction2()
        else:
            self.continuer2()
        if self.le_2_a_coule_bateau():
            self.type2 = 'chercher'
            
    def contour_bateau_1_est_coule(self,bateau):
        for x,y in bateau:
            if self.plateau_1[x+1][y] == 0:
                self.plateau_1[x+1][y] = 2
            if self.plateau_1[x-1][y] == 0:
                self.plateau_1[x-1][y] = 2
            if self.plateau_1[x][y+1] == 0:
                self.plateau_1[x][y+1] = 2
            if self.plateau_1[x][y-1] == 0:
                self.plateau_1[x][y-1] = 2
                
    def contour_bateau_2_est_coule(self,bateau):
        for x,y in bateau:
            if self.plateau_2[x+1][y] == 0:
                self.plateau_2[x+1][y] = 2
            if self.plateau_2[x-1][y] == 0:
                self.plateau_2[x-1][y] = 2
            if self.plateau_2[x][y+1] == 0:
                self.plateau_2[x][y+1] = 2
            if self.plateau_2[x][y-1] == 0:
                self.plateau_2[x][y-1] = 2
    
    def main(self):
        
        while self.partie_finie() == False:
            
            if self.type1 == 'chercher':
                self.attaque_1()
            else:
                self.attaque_bateau1()  
            
            if self.partie_finie() == True:
                break
            
            if self.type2 == 'chercher':
                self.attaque_2()
            else:
                self.attaque_bateau2()
            """
            Affiche le plateau 1
            """
            """
            plt.imshow(self.plateau_1)
            plt.show()
            time.sleep(0.5)
            """
            
            self.tour += 1
        
        return self.tour
        """
        Pour voir la fin
        
        print("\nFIN\n")
        
        plt.imshow(self.plateau_1)
        plt.show()
        
        plt.imshow(self.plateau_2)
        plt.show()
        """

liste = []
for i in range(5000):
    liste.append(Bataille_navale().tour)
    if (i+1)%100==0:
        print(i+1)
print(np.mean(np.array(liste)))