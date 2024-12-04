#crear un motor
import pygame
pygame. init() 

#definir las dimensiones que va a tener las ventanas
screen = pygame.display.set_mode((450, 450))
pygame.display.set_caption("juego triki")

#carfar imagenes
fondo=pygame.image.load("TrikiImagen/Tablero.png")
circulo=pygame.image.load("TrikiImagen/Circulo.png")
equis=pygame.image.load("TrikiImagen/Equis.png")
resect=pygame.image.load("TrikiImagen/resect.png")
felicidades=pygame.image.load("TrikiImagen/Felicidades.png")

#renderizamo las imagenes
fondo=pygame.transform.scale(fondo,(450, 450))
circulo =pygame.transform.scale(circulo,(125, 125))
equis =pygame.transform.scale(equis,(125, 125))
resect =pygame.transform.scale(resect,(50, 50))
felicidades =pygame.transform.scale(felicidades,(250, 250))

#creamos las coordenasas de las matrices
coordenadas=[[(40,50),(165,50),(290,50)],
             [(40,175),(165,175),(290,175)],
             [(40,300),(165,300),(290,300)]] 
             
#matriz de los jugadores
tablero=[['','',''],
         ['','',''],
         ['','','']]
    
#varibles de control
#Saber de quien es el turno
turno='O'

#fin del juego
game_over=False
reloj=pygame.time.Clock()

#eatablecer la logica del juego

def graficar_tablero():
 #mostrar el fondo o llenamos la ventana
 #con la imagen de fondo
    screen. blit(fondo, (0,0)) #dibujar el fondo
    
    for fila in range (3):
        for columna in range (3):
            #Funcion para graficar la X o la O
            if tablero [fila][columna]=='O':
                graficar_O(fila, columna)    
            elif tablero[fila][columna]=='X':
                graficar_X(fila, columna)
     
    # dibuja el botón de reinicio           
    screen.blit(resect,(375,10))
    
# función para reiniciar el tablero      
def reiniciar_tablero():
    # reiniciar el tablero y vaciar las celdas
    global tablero, turno
    tablero = [['', '', ''], ['', '', ''], ['', '', '']]  # vaciar el tablero
    turno = 'O'       

# funciones para graficar las X y O     
def graficar_O(fila, columna):    
    screen. blit(circulo, coordenadas[fila][columna]) 
def graficar_X(fila, columna):
    screen. blit(equis, coordenadas[fila][columna])  
    
# función para verificar si un jugador ha ganado
def verificar_ganador():
    # Comprobar filas, columnas y diagonales
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != '':
            return tablero[i][0]  # Retorna 'O' o 'X'
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != '':
            return tablero[0][i]  # Retorna 'O' o 'X'

    # comprobar las diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != '':
        return tablero[0][0]  # Retorna 'O' o 'X'
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != '':
        return tablero[0][2]  # Retorna 'O' o 'X'

    return None  # Si no hay ganador

#iniciar el juego
while not game_over:
  reloj.tick(30) 
  
  for event in pygame.event.get():
    #definos cuamdo se cierra en juego
    #con el boton cerrar
    if event.type==pygame.QUIT:
        game_over=True
        
    elif event.type == pygame.MOUSEBUTTONDOWN:
        mouseX,mouseY=event.pos
        if(mouseX >=40 and mouseX<415 ) and (mouseY >=50 and mouseX<425 ):
                    fila=(mouseY-50)//125
                    columna=(mouseX-40)//125
                    if tablero[fila][columna]=='':
                        tablero[fila][columna]=turno
                        if turno=='O':
                            turno='X'
                        else:
                            turno='O'
                    # si alguien ha ganado
                    ganador = verificar_ganador()
                    if ganador:
                        game_over = True  # termina el juego con un ganador
                        turno = ganador
                        screen.blit(felicidades,(0,0))
                        pygame.display.update()
                        pygame.time.wait(2000)
                        print("Feliidades Gano")
                            
    # detectar clic en el botón de reinicio
        if 375 <= mouseX <= 450 and 10 <= mouseY <= 85:
            reiniciar_tablero()  # reiniciar el tablero al hacer clic en el botón
            
     
     #graficar tablero                
    graficar_tablero()
    pygame.display.update()

#si ya está lleno el tablero finaliza el juego
pygame.quit