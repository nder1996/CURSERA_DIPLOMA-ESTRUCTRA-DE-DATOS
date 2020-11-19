print("\t     ---------------------------------")
print("\t       Bienvenidos al juego TA-TE-TI")
print("\t     ---------------------------------\n")
Tablero=[
    ["\t\t\t|","X","|","X","|","3","|"],
    ["\t\t\t|","O","|","O","|","X","|"],
    ["\t\t\t|","X","|","O","|","O","|"]
    ]

def VRecorrido(Simbolo):
        c = 0 ; a = 3 ; b = 7
        for x in range(a):
            for y in range(1,b,2):
                if Tablero[x][y] == Simbolo:
                    c+=1
                    if c==3: print("1. G_A_N_A_S_T_E") ; a = 0 ; b = 0
                else:
                    break      
            c = 0
        if a!=0 and b != 0:
           c = 0 ; a = 3 ; b = 7
           for y in range(1,b,2):
                for x in range(a):
                    if Tablero[x][y] == Simbolo:
                       c+=1
                       if c==3: a = 0 ; b = 0
                    else:
                        break
                c = 0     
        if a!=0 and b != 0:
           c = 0 ; a = 3 ; b = 1
           for x in range(a):
                if Tablero[x][b] == Simbolo:
                      c+=1
                      if c==3:   a = 0
                else:
                    break  
                b += 2    
        if a!=0 :
           c = 0 ; x = 0 ; b = 0
           for y in range(5,b,-2):
                if Tablero[x][y] == Simbolo:
                      c+=1
                      if c==3:  b = 7
                else:
                    break  
                x += 1
        if b==0:
            c = 0
            for x in range(3):
                for y in range(1,7,2):
                    if Tablero[x][y].isdigit()==False:
                       c+=1
                    else:
                        break
            if c == 9:
                print("TODOS SON DIGITOS : ",c)
            else:
                print("TODAVIA HAY JUEGO") 
            
            
           
print("\t     -------------------------------")
print("\t\t       HAY EMPATE")
print("\t     -------------------------------\n")                     
        

                     
#VRecorrido("O")                    
                    
                      
                
                    
