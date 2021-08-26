# Escribe aquí tus funciones...

def main():
    #escribe tu código abajo de esta línea
    def volumen_prisma(a,b,p):
        return a*b*p


    b = float(input("Dame la base: "))
    a = float(input("Dame la altura: "))
    p = float(input("Dame la profundidad: "))

    r = volumen_prisma(b,a,p)

    print("El volumen del prisma es:",r)

if __name__=='__main__':
    main()
