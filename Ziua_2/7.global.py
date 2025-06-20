
## GLOBAL
x = 99

def functie(x):
    ## LOCAL
    x += 1
    print(x)

def functie_cu_x_global():
    global x
    x += 1
    print(x)



functie(10)
print(x)


functie_cu_x_global()
print(x)
