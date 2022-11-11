x=(5.5)
y=(3.7)

a=x-y
b=x+y
c=x**y
x+=1
y-=2
f=x%y
g=x//y
h=x/y

print("Ejercicio 1:")
print("a)",a)
print("b)",b)
print("c)",c)
print("d)",x)
print("e)",y)
print("f)",f)
print("g)",g)
print("h)",h)

name="Guillem"
print("Ejercicio 2:")
print(name)

print("Ejercicio 2.2.:")
nombre=input("¿Como te llamas?")
print(nombre)

print("Ejercicio 3")

edad=int(input("Pon tu edad"))

if edad>=18:
    print("Eres mayor")
else:
    print("Eres menor")

print("Ejercicio 4")

nota=float(input("¿Que nota tienes?"))
if nota<5:
    print("Suspès")

if nota>=5 and nota<=6:
    print("Bé")

if nota>=6 and nota<=8:
    print("Notable")

if nota>=8:
    print("Excel·lent")


print("ejercicio 5:")
print("""Estas deprimido?
        1)Si
        2)No""")

eligio=input("Selecciona 1 o 2:")

while True:
    if "1" or "2" in eligio:
        if eligio == "1" :
            print("""Vas al psicologo?
            1)Si
            2)No""")
            
            eligio1=input("Selecciona 1 o 2:")

            while True:
                if "1" or "2" in eligio1:
                    if eligio1 == "1" :
                        print("""Te ayuda?
                        1)Si
                        2)No""")
                        
                        eligio2=input("Selecciona 1 o 2:")

                        while True:
                            if "1" or "2" in eligio2:
                                if eligio2 == "1" :
                                    print("De Puta Madre")
                                elif eligio2 == "2":
                                    print("Drogate")
                                break
                            else:
                                print("Invalido, reinicia")
                            
                    elif eligio1 == "2":
                        print("Empieza a ir")
                    break
                else:
                    print("Invalido, reinicia")
                    

    elif eligio == "2":
        print("De Puta Madre")
        break
    else:
        print("Invalido, reinicia")