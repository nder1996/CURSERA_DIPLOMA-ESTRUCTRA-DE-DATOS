import string
import os
import sys
import time



def Inicio():
       print("\t     ---------------------------------")
       print("\t       Bienvenidos al juego TA-TE-TI")
       print("\t     ---------------------------------\n")
       Tablero=[
       ["\t\t\t|","1","|","2","|","3","|"],
       ["\t\t\t|","4","|","5","|","6","|"],
       ["\t\t\t|","7","|","8","|","9","|"]
       ]
       return Tablero

def GanarFinal(Ganador):
       print("\t     ------------------------------------------")
       print("\t        F E L I C I D A D E S  G A N A S T E ")
       print("\t     ------------------------------------------\n")
       print("\t\t   Jugador Con El Simbolo : ",Ganador,"\n\n")

def Verificador(Simbolo,Tablero):
        c = 0 ; a = 3 ; b = 7 ;
        for x in range(a):
            for y in range(1,b,2):
                if Tablero[x][y] == Simbolo:
                    c+=1
                    if c==3: 
                        return True
                        a = 0 ; b = 0
                else:
                    break      
            c = 0
        if a!=0 and b != 0:
           c = 0 ; a = 3 ; b = 7
           for y in range(1,b,2):
                for x in range(a):
                    if Tablero[x][y] == Simbolo:
                       c+=1
                       if c==3: 
                           return True
                           a = 0 ; b = 0
                    else:
                        break
                c = 0     
        if a!=0 and b != 0:
           c = 0 ; a = 3 ; b = 1
           for x in range(a):
                if Tablero[x][b] == Simbolo:
                      c+=1
                      if c==3: 
                          return True
                          a = 0
                else:
                    break  
                b += 2    
        if a!=0 :
           c = 0 ; x = 0 ; b = 0
           for y in range(5,b,-2):
                if Tablero[x][y] == Simbolo:
                      c+=1
                      if c==3:
                          return True
                          b = 7
                else:
                    break  
                x += 1
        if b==0:
            c = 0
            for x in range(3):
                for y in range(1,7,2):
                    if Tablero[x][y].isdigit()==False:
                       c+=1
            if c == 9:
               return "Empate"
        return False 
                
def Juego(Tab,Simbolo,NJugador):
    Posicion=str(input("\n\t  Ingrese la Posicion que desea Jugardor {} - ({}) : ".format(NJugador,Simbolo)))
    for i in range(3):
         for j in range(7):
           if Tab[i][j] == Posicion:
              if Tab[i][j]!="X" or Tab[i][j]!="O":
                Tab[i][j]=Simbolo
                print("\n");Tablero(Tab);print("\n")
                return Tab
    #Posicion=str(input("\n\t  Ingrese la Posicion que desea Jugardor {} : ".format(NJugador)))
                                                           
def Tablero(Tab):
    for i in range(3):
      for j in range(7):
          print(Tab[i][j],end=' ')
      print()
            
def Menu():
    print("\t     ---------------------------------")
    print("\t       Bienvenidos al juego TA-TE-TI")
    print("\t     ---------------------------------\n")
    print("""
        \t\t| _ | _ | _ |
        \t\t| _ | _ | _ |
        \t\t| _ | _ | _ |  
        \n
        """)
    print("\t\t1. Escoge el simbolo X para iniciar")
    print("\t\t2. Escoge el simbolo O para iniciar\n")
    Opcion = int(input("\t\tEscribe El Simbolo Que Desea Usar : "))
    os.system ("cls")
    TabJuego = Inicio() ; Ganar = False
    print("\n");Tablero(TabJuego);print("\n")
    
    if Opcion == 1:
       for i in range(9):
          TabJuego = Juego(TabJuego,"X",1)
          Ganar = Verificador("X",TabJuego)
          if Ganar == True:
             GanarFinal("X")
             break
          if Ganar == False:
             TabJuego = Juego(TabJuego,"O",2)
             if Verificador("O",TabJuego)==True:
                GanarFinal("O")
                break
          if Verificador("X",TabJuego) == "Empate": 
           print("\t     -------------------------------")
           print("\t\t       HAY EMPATE")
           print("\t     -------------------------------\n")    
    
    if Opcion == 2 :
        for i in range(9):
          TabJuego = Juego(TabJuego,"O",2)
          Ganar = Verificador("0",TabJuego)
          if Ganar == True:
             GanarFinal("O")
             break
          if Ganar == False:
             TabJuego = Juego(TabJuego,"X",1)
             if Verificador("X",TabJuego)==True:
                GanarFinal("X")
                break             
        if Verificador("X",TabJuego) == "Empate": 
           print("\t     -------------------------------")
           print("\t\t       HAY EMPATE")
           print("\t     -------------------------------\n")     
         

os.system ("cls")  

Menu()

 