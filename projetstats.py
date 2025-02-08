import mysql.connector as mysql
import matplotlib.pyplot as plt
import json

db = mysql.connect(host="localhost",user='root',password='',db='test')
cursor = db.cursor() 
cursor.execute(('SELECT compo,score,victoire,defaite FROM bataille_navale'))
table = cursor.fetchall()
cursor.close()

stats = [[0 for i in range(10)] for j in range(10)]
stats2 = [[0 for i in range(10)] for j in range(10)]
stats3 = [[0 for i in range(10)] for j in range(10)]
stats4 = [[0 for i in range(10)] for j in range(10)]
stats5 = [[0 for i in range(10)] for j in range(10)]
nombre = 0

for i in range(len(table)):
    data = json.loads(table[i][0].decode('utf-8'))
    for x,y in data['2']:
        stats2[x][y] += 1
        stats[x][y] += 1
    for x,y in data['30']:
        stats3[x][y] += 1
        stats[x][y] += 1
    for x,y in data['31']:
        stats3[x][y] += 1
        stats[x][y] += 1
    for x,y in data['4']:
        stats4[x][y] += 1
        stats[x][y] += 1
    for x,y in data['5']:
        stats5[x][y] += 1
        stats[x][y] += 1
    victoire, defaite = table[i][2],table[i][3]
    nombre += victoire+defaite
        
plt.imshow(stats2)
plt.title("Présence des bateaux de taille 2")
plt.show()

plt.imshow(stats3)
plt.title("Présence des bateaux de taille 3")
plt.show()

plt.imshow(stats4)
plt.title("Présence des bateaux de taille 4")
plt.show()

plt.imshow(stats5)
plt.title("Présence des bateaux de taille 5")
plt.show()

plt.imshow(stats)
plt.title("Présence des bateaux de toutes tailles")
plt.show()

print(f"\nNombre de parties jouées : {nombre}, dont {len(table)} uniques")