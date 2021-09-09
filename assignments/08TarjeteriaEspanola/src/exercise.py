
def main():
    #escribe tu código abajo de esta línea
    def tarjetas(pliegos,plumones):  ## 1. ESTA FUNCION DEBERIA ESTAR AFUERA COMO UNA FUNCIÓN INDEPENDIENTE, NO DENTRO DE LA FUNCIÓN MAIJ()
    tarjetasPli=pliegos*12
    tarjetasPlu=plumones*35
    if tarjetasPli<= tarjetasPlu:
        return tarjetasPli
    elif tarjetasPlu<=tarjetasPli:
        return tarjetasPlu

pliegos=int(input('Inserte la cantidad de pliegos albanene:'))
plumones=int(input('Inserte la cantidad de plumones:'))
total=tarjetas(pliegos,plumones)  ##2. POR LA MISMA RAZON DEL COMENTARIO 1, ESTA FUNCIÓN NUNCA SE ENCUENTRA
print('El número máximo de tarjetas que se pueden hacer es:',total)
    pass

if __name__=='__main__':
    main()
