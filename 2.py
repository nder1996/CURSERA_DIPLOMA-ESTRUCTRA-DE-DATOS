import math
import os




print("\t     ---------------------------------")
print("\t       Bienvenidos al juego TA-TE-TI")
print("\t     ---------------------------------\n")
Tablero=[
    ["\t\t\t|","1","|","2","|","X","|"],
    ["\t\t\t|","4","|","5","|","X","|"],
    ["\t\t\t|","7","|","8","|","X","|"]
    ]

def VRecorrido(Q):    
    c = 0 ; x = 0 ; y = 1 ; Cy = 0
    for i in range(3):
        for j in range(7):
            print("( ",x," , ",y," )") 
            if i==x and j==y:
               if Tablero[i][j]=="X":
                  c+=1
                  if Q==0: y+=2
                  if Q==1 and c==1: Cy = j ; print("VALOR DE J : ",Cy)
                  y = Cy
        if c==3:
           print("G_A_N_A_S_T_E")
           break
        if Q==0: x+=1 ; y=1
        if Q==1: x+=1


print("\n\n")   
#os.system ("cls")  
VRecorrido(1)




print("\n\n")   
#print("Ganar",Ganar[0][1])
