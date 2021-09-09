
def main():
    #escribe tu código abajo de esta línea
    base = int(input("Inserta un valor para la base : "))  ##Debias convertirlos a flotante
    altura = int(input("Inserta un valor para la altura : ")) ##Debias convertirlos a flotante
    profundidad = float(input("Inserta un valor para la profundidad" )) ##Debias convertirlos a flotante
           
    def area():
        area_1 = base * altura
        volumen = area_1 * profundidad
        return volumen
    print("El volumen del prisma es : "+ str(area()))
    pass
    pass

if __name__=='__main__':
    main()
