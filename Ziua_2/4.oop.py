
## OOP -> Object Oriented Programming 

"""Trebuie creată clasa STBCard care reprezintă cardul de la regia autonomă de transport București. 
Atributele necesare sunt: numele deținătorului, călătorii disponibile și creditul disponibil
În cazul in care nu primește numele deținătorului, setati-l automat pe "Nenominal"
Setați valoarea unei călătorii validate cu credit la 3 lei.
Creați funcții automate pentru validare cu credit/validare călătorie și reîncare credit/reîncarcare călătorii """

## Definirea unei clase - conventie cu litera mare
class Student:
    ## functie, variabile

    ## functii (metode) -> CE FACE
    def __init__(self, nume, varsta, numar_telefon):
        self.nume = nume
        self.varsta = varsta
        self.numar_telefon = numar_telefon

    ## __ -> metode magice
    ## str(obiect)
    def __str__(self):
        return f"{self.nume} are {self.varsta} ani si numarul de telefon {self.numar_telefon}"

    def schimba_numar(self, noul_numar):
        if noul_numar.isnumeric():
            self.numar_telefon = noul_numar
        else:
            print("Numarul nu poate fi schimbat")


    ## variabilele  (atribute) -> CE ARE
    

## Creare unui obiect 1
obiect_stud1 = Student("Marian", 18, "07321231") ### Marian
print(obiect_stud1)
print(obiect_stud1.nume, "are", obiect_stud1.varsta)

## Creare unui obiect 2
obiect_stud2 = Student("Florina", 22, "0732532") ### Florina
print(obiect_stud2)
print(obiect_stud2.nume, "are", obiect_stud2.varsta, "telefon", obiect_stud2.numar_telefon)

obiect_stud2.schimba_numar("jhfjksdhfsjdkhfkjs")
print(obiect_stud2.nume, "are", obiect_stud2.varsta, "telefon", obiect_stud2.numar_telefon)