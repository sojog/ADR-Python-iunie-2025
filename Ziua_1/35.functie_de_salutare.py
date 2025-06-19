import time


def saluta(sleep):
    print("Buna dimineata")
    time.sleep(sleep)
    print("Buna ziua")
    time.sleep(sleep)
    print("Buna seara")


for i in range(10):
    saluta(i)