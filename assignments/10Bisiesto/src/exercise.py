
def main():
    #escribe tu código abajo de esta línea
    def es_bisiesto(x):
    bi=x
    if (bi%4==0):
        if(bi%100==0):
            if(bi%400==0):
                bi=True
            else:
                bi=False
        else:
            bi=True
    else:
        bi:False
    return bi

año= int(input())
calculo= es_bisiesto(año)
print(calculo)
    pass

if __name__=='__main__':
    main()
