from random import randint,shuffle
import numpy as np
import matplotlib.pyplot as plt

class Bataille_navale():
    
    def __init__(self):
        
        self.tour = 0
        
        self.plateau_1 = [[7,7,7,7,7,7,7,7,7,7,7,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,7,7,7,7,7,7,7,7,7,7,7]]
        self.plateau_2 = [[7,7,7,7,7,7,7,7,7,7,7,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,0,0,0,0,0,0,0,0,0,0,7],[7,7,7,7,7,7,7,7,7,7,7,7]] 
        
        self.liste_bateaux_1,self.plateau_1 = self.placer_bateaux(self.plateau_1)
        self.liste_bateaux_2,self.plateau_2 = self.placer_bateaux(self.plateau_2)
        
        """
        Pour voir le placement des bateaux
        """
        
        plt.imshow(self.plateau_1)
        plt.show()
        
        plt.imshow(self.plateau_2)
        plt.show()
        
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
        n = 0
        for bateau in self.liste_bateaux_1:
            for x,y in bateau:
                if self.plateau_1[x][y] == -1:
                    n += 1
        if n == 17:
            return True
        n = 0
        for bateau in self.liste_bateaux_2:
            for x,y in bateau:
                if self.plateau_2[x][y] == -1:
                    n += 1
        if n == 17:
            return True
        return False
    
    def attaque_1(self):
        "Le plateau 1 attaque le plateau 2"
        
        x,y = randint(1,10),randint(1,10)
        if self.plateau_2[x][y] != 0 and self.plateau_2[x][y] != 1:
            self.attaque_1()
        if self.plateau_2[x][y] == 1:
            self.plateau_2[x][y] = -1
        if self.plateau_2[x][y] == 0:
            self.plateau_2[x][y] = -2
            
    def attaque_2(self):
        "Le plateau 2 attaque le plateau 1"
        
        x,y = randint(1,10),randint(1,10)
        if self.plateau_1[x][y] != 0 and self.plateau_1[x][y] != 1:
            self.attaque_2()
        if self.plateau_1[x][y] == 1:
            self.plateau_1[x][y] = -1
        if self.plateau_1[x][y] == 0:
            self.plateau_1[x][y] = -2
    
    def main(self):
        
        while self.partie_finie() == False:
            self.attaque_1()
            self.attaque_2()
            self.tour += 1
            
        print(self.tour)
        
        
        """Pour voir la fin
        
        print("\nFIN\n")
        
        plt.imshow(self.plateau_1)
        plt.show()
        
        plt.imshow(self.plateau_2)
        plt.show()
        """
        

Bataille_navale()