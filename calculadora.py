#Calculadora de figuras geometricas 

import os

def pause():
    input("Presione Enter para continuar...")

def limp():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


Opciones = 0

while Opciones != 10:

    print("MENU DE OPCIONES ")
    print("1. Rectángulo")
    print("2. Triángulo")
    print("3. Esfera")
    print("4. Cubo")
    print("5. Triángulo Rectángulo")
    print("6. Cono")
    print("7. Trapecio")
    print("8. Pentágono")
    print("9. Hexágono")
    print("10. Salir")

    Opciones = int(input("Elige una opción: "))

    # RECTANGULO
    if Opciones == 1:
        print("¿Qué desea hallar?")
        print("1. Área")
        print("2. Base")
        print("3. Altura")
        op = int(input("Opción: "))

        if op == 1:
            b = float(input("Base: "))
            h = float(input("Altura: "))

            while b <= 0 or h <= 0:
                print("Ponga numero positivo")
                b = float(input("Base: "))
                h = float(input("Altura: "))

            area = b * h
            print("Área =", area)

        elif op == 2:
            area = float(input("Área: "))
            h = float(input("Altura: "))

            while area <= 0 or h <= 0:
                print("Ponga numero positivo")
                area = float(input("Área: "))
                h = float(input("Altura: "))

            base = area / h
            print("Base =", base)

        elif op == 3:
            area = float(input("Área: "))
            b = float(input("Base: "))

            while area <= 0 or b <= 0:
                print("Ponga numero positivo")
                area = float(input("Área: "))
                b = float(input("Base: "))

            altura = area / b
            print("Altura =", altura)

    # TRIANGULO
    elif Opciones == 2:
        print("¿Qué desea hallar?")
        print("1. Área")
        print("2. Base")
        print("3. Altura")
        op = int(input("Opción: "))

        if op == 1:
            b = float(input("Base: "))
            h = float(input("Altura: "))

            while b <= 0 or h <= 0:
                print("Ponga numero positivo")
                b = float(input("Base: "))
                h = float(input("Altura: "))

            area = (b * h) / 2
            print("Área =", area)

        elif op == 2:
            area = float(input("Área: "))
            h = float(input("Altura: "))

            while area <= 0 or h <= 0:
                print("Ponga numero positivo")
                area = float(input("Área: "))
                h = float(input("Altura: "))

            base = (2 * area) / h
            print("Base =", base)

        elif op == 3:
            area = float(input("Área: "))
            b = float(input("Base: "))

            while area <= 0 or b <= 0:
                print("Ponga numero positivo")
                area = float(input("Área: "))
                b = float(input("Base: "))

            altura = (2 * area) / b
            print("Altura =", altura)

    # ESFERA
    elif Opciones == 3:
        print("¿Qué desea hallar?")
        print("1. Volumen")
        print("2. Radio")
        op = int(input("Opción: "))

        if op == 1:
            r = float(input("Radio: "))

            while r <= 0:
                print("Ponga numero positivo")
                r = float(input("Radio: "))

            volumen = (4/3) * 3.1416 * r**3
            print("Volumen =", volumen)

        elif op == 2:
            volumen = float(input("Volumen: "))

            while volumen <= 0:
                print("Ponga numero positivo")
                volumen = float(input("Volumen: "))

            r = ((3 * volumen) / (4 * 3.1416)) ** (1/3)
            print("Radio =", r)

    # CUBO
    elif Opciones == 4:
        print("¿Qué desea hallar?")
        print("1. Volumen")
        print("2. Lado")
        op = int(input("Opción: "))

        if op == 1:
            l = float(input("Lado: "))

            while l <= 0:
                print("Ponga numero positivo")
                l = float(input("Lado: "))

            volumen = l**3
            print("Volumen =", volumen)

        elif op == 2:
            volumen = float(input("Volumen: "))

            while volumen <= 0:
                print("Ponga numero positivo")
                volumen = float(input("Volumen: "))

            lado = volumen ** (1/3)
            print("Lado =", lado)

    # TRIANGULO RECTANGULO
    elif Opciones == 5:
        print("¿Qué desea hallar?")
        print("1. Hipotenusa")
        print("2. Lado a")
        print("3. Lado b")
        op = int(input("Opción: "))

        if op == 1:
            a = float(input("Lado a: "))
            b = float(input("Lado b: "))

            while a <= 0 or b <= 0:
                print("Ponga numero positivo")
                a = float(input("Lado a: "))
                b = float(input("Lado b: "))

            c = (a*2 + b*2) * 0.5
            print("Hipotenusa =", c)

        elif op == 2:
            c = float(input("Hipotenusa: "))
            b = float(input("Lado b: "))

            while c <= 0 or b <= 0:
                print("Ponga numero positivo")
                c = float(input("Hipotenusa: "))
                b = float(input("Lado b: "))

            a = (c*2 - b*2) * 0.5
            print("Lado a =", a)

        elif op == 3:
            c = float(input("Hipotenusa: "))
            a = float(input("Lado a: "))

            while c <= 0 or a <= 0:
                print("Ponga numero positivo")
                c = float(input("Hipotenusa: "))
                a = float(input("Lado a: "))

            b = (c*2 - a*2) * 0.5
            print("Lado b =", b)

    # CONO
    elif Opciones == 6:
        print("¿Qué desea hallar?")
        print("1. Volumen")
        print("2. Altura")
        op = int(input("Opción: "))

        if op == 1:
            r = float(input("Radio: "))
            h = float(input("Altura: "))

            while r <= 0 or h <= 0:
                print("Ponga numero positivo")
                r = float(input("Radio: "))
                h = float(input("Altura: "))

            volumen = (3.1416 * r**2 * h) / 3
            print("Volumen =", volumen)

        elif op == 2:
            volumen = float(input("Volumen: "))
            r = float(input("Radio: "))

            while volumen <= 0 or r <= 0:
                print("Ponga numero positivo")
                volumen = float(input("Volumen: "))
                r = float(input("Radio: "))

            h = (3 * volumen) / (3.1416 * r**2)
            print("Altura =", h)

    # TRAPECIO
    elif Opciones == 7:
        print("¿Qué desea hallar?")
        print("1. Área")
        op = int(input("Opción: "))

        if op == 1:
            B = float(input("Base mayor: "))
            b = float(input("Base menor: "))
            h = float(input("Altura: "))

            while B <= 0 or b <= 0 or h <= 0:
                print("Ponga numero positivo")
                B = float(input("Base mayor: "))
                b = float(input("Base menor: "))
                h = float(input("Altura: "))

            area = ((B + b) * h) / 2
            print("Área =", area)

    # PENTAGONO
    elif Opciones == 8:
        print("¿Qué desea hallar?")
        print("1. Área")
        op = int(input("Opción: "))

        if op == 1:
            p = float(input("Perímetro: "))
            a = float(input("Apotema: "))

            while p <= 0 or a <= 0:
                print("Ponga numero positivo")
                p = float(input("Perímetro: "))
                a = float(input("Apotema: "))

            area = (p * a) / 2
            print("Área =", area)

    # HEXAGONO
    elif Opciones == 9:
        print("¿Qué desea hallar?")
        print("1. Área")
        op = int(input("Opción: "))

        if op == 1:
            p = float(input("Perímetro: "))
            a = float(input("Apotema: "))

            while p <= 0 or a <= 0:
                print("Ponga numero positivo")
                p = float(input("Perímetro: "))
                a = float(input("Apotema: "))

            area = (p * a) / 2
            print("Área =", area)

    elif Opciones == 10:
        print("Programa terminado")

    else:
        print("Opción incorrecta")

    pause()
    limp()
    



    
