
# IMPORT
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from IPython.display import HTML
from scipy import integrate

# POCATECNI PODMINKY
hmotnost_slunce = 333000 # Me (v jednotkach hmotnosti zeme)
polomer_slunce = 0.0004*150000000 # AU (astronomicka jednotka) na km
hmotnost_asteroidu = 2e-25 # Me
prumer_asteroidu = 1 # km
G = 6.674e-11 # gravitacni konstanta
n = 150
numOfAsteroids = n



# VYPOCET pozice asteroidu v intervalu <0.1; 30> AU

##
# náhodná posloupnost 1 a -1
volba = np.ones((1,n))
for i in range(n):
  volba[0,i]=random.choice([-1, 1])
##
ppoziceR = np.array([np.multiply(random.sample(range(100, 30000), numOfAsteroids),0.001)])
ppoziceX = np.array([np.multiply(random.sample(range(-999, 999), numOfAsteroids),0.001)])
ppoziceX = np.multiply(ppoziceX,ppoziceR)
ppoziceY = np.multiply((ppoziceR**2-ppoziceX**2)**0.5,volba)
ppozice = np.append([ppoziceX], [ppoziceY]).reshape(2,numOfAsteroids)
temp = np.append([ppoziceX], [ppoziceY]).reshape(2,numOfAsteroids) # z nejakeho duvodu se pri zmene prychlost menilo i ppozice, proto bylo pouzito temp**

sizePozice = np.sqrt(ppozice[0,:]**2+ppozice[1,:]**2)
alpha = np.sqrt(hmotnost_slunce*G/sizePozice)


#rychlost =np.array([[3, 2, 6, 7, 3, 0, 7],
#          [0, 4, 0, 2, 2, 4, 0]])
# VYPOCET rychlosti
prychlost = temp[::-1,:] #pouziti temp
prychlost[0,:] = prychlost[0,:]*(-1)
prychlost = np.divide(alpha * prychlost,sizePozice)




nezname = np.append([ppozice], [prychlost]).reshape(4,numOfAsteroids).transpose() #reshape - N radku, slozit, rozdelit, transponovat
#print(nezname)
#nezname = np.array([[1, 2, -3, 4],
#                   [3, -7, 9, 0],
#                   [-2, 3, 4, -4]])


# SILY  - v matici "nezname" je poloha a rychlost, vytvorime matici F, kde jsou slozky sil
m_shluku = 14 # jednotka: hmotnost Země (M_e)
F = np.ones((n,2)) 
for index, row in enumerate(nezname):
    vec_size = np.sqrt(nezname[index,0]**2+nezname[index,1]**2)
    F[index,0]=-G*hmotnost_slunce*m_shluku*nezname[index,0]/vec_size**3
    F[index,1]=-G*hmotnost_slunce*m_shluku*nezname[index,1]/vec_size**3
    
    #####################
#def model1(v,t)
    
    

fig, ax = plt.subplots()


ax.scatter(0, 0, marker="*", c="orange", s=1000)
ax.scatter(nezname[:,0], nezname[:,1], marker="o", c="black", s=14)
#plt.show()
plt.quiver(nezname[:,0],nezname[:,1],nezname[:,2],nezname[:,3])
plt.quiver(nezname[:,0],nezname[:,1],F[:,0],F[:,1], color='g')



ax.set_xlim(( -2, 2))
ax.set_ylim((-2, 2))
ax.grid()

plt.show()
