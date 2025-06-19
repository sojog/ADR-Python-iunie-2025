

while True:
    nr = input("Introduceti un numar\n")
    
    while not nr.isnumeric():
        print("Numarul nu poate fi transformat in int")
        nr = input("Introduceti un numar\n")

    print("Numarul poate fi transformat")
    nr = int(nr)
    if nr % 2 == 0:
        print("Par")
    else:
        print("Impar")


