
def main():
    #escribe tu código abajo de esta línea
    def tarjetas(pliegos,plumones):
    tarjetasPli=pliegos*12
    tarjetasPlu=plumones*35
    if tarjetasPli<= tarjetasPlu:
        return tarjetasPli
    elif tarjetasPlu<=tarjetasPli:
        return tarjetasPlu

pliegos=int(input('Inserte la cantidad de pliegos albanene:'))
plumones=int(input('Inserte la cantidad de plumones:'))
total=tarjetas(pliegos,plumones)
print('El número máximo de tarjetas que se pueden hacer es:',total)
    pass

if __name__=='__main__':
    main()
