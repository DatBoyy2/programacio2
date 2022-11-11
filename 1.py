print("""
    1) Si       
    2) No        
    """)


eligio=input("Selecciona 1 o 2:")

while True:
    if "1" or "2" in eligio:
        if eligio == "1" :
            print("test")
        elif eligio == "2":
            print("ndad")
        break
    else:
        print(eligio)
        eligio=input("Selecciona 1 o 2:")

    