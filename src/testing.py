class Juego:
    def __init__(self, numero_juego):
        self.piedra = "Piedra"
        self.papel = "Papel"
        self.tijera = "Tijera"
        x=0
        x=x+1
        self.juego = int(numero_juego)+x

#Para crear el objeto

x =  Juego(1)
print (x.piedra)
print (x.papel)
print (x.tijera)
print (x.juego)