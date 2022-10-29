class Nemoc:
    # poradi argumentu v radku nize si klidne preskladejte
    def __init__(self, jmeno, inkubacni_doba, pocet_obeti, sireni):
        self.jmeno = jmeno
        self.inkubacni_doba = inkubacni_doba
        self.pocet_obeti = pocet_obeti
        self.sireni = sireni

    def __str__(self):
        return f'Jmeno: {self.jmeno}'

    def zmen_pocet_obeti(self, pocet_obeti):
        self.pocet_obeti = pocet_obeti

class Koronavirus(Nemoc):
    def __init__(self, jmeno, inkubacni_doba, pocet_obeti, sireni):
        super().__init__(jmeno, inkubacni_doba, pocet_obeti, sireni)
        self.varianty = []

    def pridej_variantu(self, varianta):
        self.varianty.append(varianta)
        
    def __str__(self):
        if self.varianty == []:
            return super().__str__() + f" (žádné nalezené varianty)."
        else:
            self.varianty = ', '.join(self.varianty)
            return super().__str__() + f" (varianty: {self.varianty})."

corona = Koronavirus("Coronavirus", 12, 10_000, "vzduchem")

print(corona)
corona.pridej_variantu("delta")
corona.pridej_variantu("omikron")
print(corona)

print(corona.sireni)
print(corona.pocet_obeti)

corona.zmen_pocet_obeti(15_000)
print(corona.pocet_obeti)
