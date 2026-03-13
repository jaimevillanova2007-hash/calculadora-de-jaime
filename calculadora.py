#Calculadora de figuras geometricas 

Opciones  = 1

while Opciones != 0:

    print("Menu de opciones")
    print("1. Rectángulo (Área)")
    print("2. Triángulo (Área)")
    print("3. Esfera (Volumen)")
    print("4. Cubo (Volumen)")
    print("5. Triángulo Rectángulo (Hipotenusa)")
    print("6. Cono (Volumen)")
    print("7. Trapecio (Area)")
    print("8. Pentágono (Area")
    print("9. Hexágono (Area)")
    print("10. Tetraedro (volumen)")
    print("0. salir")
    Opciones = int(input("Elige una opcion: "))


    if Opciones == 1 :
        B = float(input("Base :"))
        H = float(input("Altura :"))
        Area = B*H
        print ("Area : ",Area)

    elif Opciones == 2 :
        B = float(input("Base"))
        H = float(input("Altura"))
        Area = (B*H)/2
        print("Area : ",Area)

    elif Opciones == 3 :
        r = float(input("Radio: "))
        volumen = (4/3) * 3.1416 * r**3
        print("volumen:", volumen)

    elif Opciones== 4:
        l = float(input("Lado del cubo: "))
        volumen = l**3
        print("Volumen:", volumen)

    elif Opciones == 5:
        a = float(input("Lado a: "))
        b = float(input("Lado b: "))
        c = (a**2 + b**2)**0.5
        print("Hipotenusa:", c)


    elif Opciones == 6 :
        r = float(input("Radio: "))
        h = float(input("Altura: "))
        volumen = (3.1416 * r**2 * h)/3
        print("Volumen:", volumen)

    elif Opciones == 7:
        B = float(input("Base mayor: "))
        b = float(input("Base menor: "))
        h = float(input("Altura: "))
        area = ((B + b) * h) / 2
        print("Área:", area)

    elif Opciones == 8:
        p = float(input("Perímetro: "))
        a = float(input("Apotema: "))
        area = (p * a) / 2
        print("Área:", area)

    elif Opciones == 9:
        p = float(input("Perímetro: "))
        a = float(input("Apotema: "))
        area = (p * a) / 2
        print("Área:", area)

    elif Opciones == 10:
        lado = float(input("Ingresa el lado del tetraedro: "))
        volumen = (lado**3) / (6 * 1.414)
        print("Volumen:", volumen)

    elif op == 0:
        print("Programa terminado")

    else:
        print("Opción incorrecta")




    