
import turtle

def dibujar_estrella():
    puntas = int(input("Cuántas puntas quiere que tenga la estrella? (al menos 5): "))
    longitud = 100

    ''' Deben ser al menos 5 puntas porque si no saldrían cuadrados/triángulos... etc'''
    if puntas < 5:
        print("El número debe de ser al menos 5.")
        return
    
    angle = 180 - 180 / puntas  #Ángulo por el que turtle va a girar para crear los vértices
    turtle.color("pink") #Color de la estrella
    turtle.shape("turtle") #Forma del puntero (hace una tortuga)

    for _ in range(puntas):
        turtle.forward(longitud) #Mueve la tortuga hacia delante cada vez en una distancia igual a la longitud
        turtle.right(angle)

    turtle.done()


dibujar_estrella() 
