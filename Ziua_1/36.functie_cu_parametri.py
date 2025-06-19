

# def adunare(x, y):
#     return x + y


# print(adunare(2, 3))

def adunare_param_optionali(x, *restul):
    print("x=", x, type(x))
    print("restul=", restul, type(restul))


adunare_param_optionali(1, 2, 3, 5, 5, 6, 53, 321)

adunare_param_optionali(1)

# adunare_param_optionali()



