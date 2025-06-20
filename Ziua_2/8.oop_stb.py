
## DEFINIRE - interiorul clasei
class STBCard:
    def __init__(self, nume="Nenominal", calatorii=0, credit=0):
        self.nume = nume
        self.calatorii = calatorii
        self.credit = credit
        self.pret_calatorie = 3

    def __str__(self):
        return f"{self.nume} are {self.calatorii} calatorii, {self.credit} credit"

    def validare_calatorie(self):
        if self.calatorii > 0:
            self.calatorii -= 1
        else:
            print("Nu exista suficiente calatorii")

    def validare_credit(self):
        if self.credit >= self.pret_calatorie:
            self.credit -= self.pret_calatorie

    def reincarcare_credit(self, suma):
        self.credit += suma

    def reincarcare_calatorii(self, numar):
        self.calatorii += numar


## FOLOSIRE - exteriorul clasei
obiect_card1 = STBCard()
print (obiect_card1)

obiect_card1.validare_calatorie()

obiect_card2 = STBCard("Mariana", 2, 30)
print (obiect_card2)
