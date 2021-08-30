
def main():
    #escribe tu código abajo de esta línea
    def tarjeta_total(pliegos, plumones):
    tarjetasPli = pliegos * 12
    tarjetasPlu = plumones * 35
    if tarjetasPli > trajetasPlu:
        tarjetasTotal = tarjetasPlu
    elif tarjetasPlu > tarjetasPli:
        tarjetasTotal = tarjetasPli
    return tarjetasTotal
def main ():
    pliegos = int(input("Inserte la cantidad de pliegos de papel albanene"))
    plumones = int(input("Inserte la cantidad de plumones"))
    maximo = tarjeta_total (pliegos, plumones)
    print ("El número máximo de tarjetas que se pueden hacer es: " + str(maximo))
if __name__ == '__main__':
    main()
    pass

if __name__=='__main__':
    main()
