# Zahrajeme si na lékárnu :-D (snad to nebude moc chaotické)

# Registr pojištěných pacientů (k dispozici u zdravotní pojišťovny)
registr_pojistencu_obj = [
        {"jméno a příjmení" : "František Novák", "rodné číslo" : 4510101111},
        {"jméno a příjmení" : "Jana Nováková", "rodné číslo" : 6855101111}
]


# Třída Recept:
# pro zjednodušení naši pacienti mají jméno, rodné číslo, 
# uhrada = částka, kterou budeme fakturovat na pojišťovnu,
# a atribut je_vydano = recepty se musí před fakturací na pojišťovnu vydat v lékárně
class Recept:
    def __init__(self, pacient, rodne_cislo, uhrada, je_vydano = False):
        self.pacient = pacient
        self.rodne_cislo = rodne_cislo
        self.uhrada = uhrada
        self.je_vydano = je_vydano
    
    def __str__(self):
        self.recept_vystup_list = []
        self.recept_vystup_dict = {}
        self.recept_vystup_dict["jméno a příjmení"] = self.pacient
        self.recept_vystup_dict["rodné číslo"] = self.rodne_cislo
        self.recept_vystup_dict["úhrada"] = self.uhrada
        self.recept_vystup_list.append(self.recept_vystup_dict)
        return f"{self.recept_vystup_list}"
    
    def vrat_list(self):
        self.recept_vystup_list = []
        self.recept_vystup_dict = {}
        self.recept_vystup_dict["jméno a příjmení"] = self.pacient
        self.recept_vystup_dict["rodné číslo"] = self.rodne_cislo
        self.recept_vystup_dict["úhrada"] = self.uhrada
        self.recept_vystup_list.append(self.recept_vystup_dict)
        return self.recept_vystup_dict
    
    # Abychom mohli recept vyfakturovat na pojišťovnu, je potřeba provést výdej receptu
    def vydani_receptu(self):
        self.je_vydano = True

# Naši pacienti přichází do lékárny
recept1 = Recept("František Novák", 4510101111, 1500)
recept2 = Recept("James Bond", 7707121111, 2000)
recept3 = Recept("Jana Nováková", 6855101111, 5300)


# A my potřebujeme vydat jejich recepty
recept1.vydani_receptu()
# Zapomnělo se na výdej receptu2 (to se někdy stává...)
recept3.vydani_receptu()
vydej1 = recept1.je_vydano
vydej2 = recept2.je_vydano
vydej3 = recept3.je_vydano


uhrada_recept1 = recept1.uhrada
uhrada_recept2 = recept2.uhrada
uhrada_recept3 = recept3.uhrada

# Pro zjednodušení: 1x měsíčně odešleme fakturu na pojišťovnu k proplacení receptů
class Faktura():
    def __init__(self):
        self.celkova_uhrada = 0
        self.seznam_receptu = []
    
    def __str__(self):
        return f"Faktura je za {self.celkova_uhrada} Kč a obsahuje položky: \n" + "\n".join(f"{x}" for x in self.seznam_receptu)
    
    # Do faktury můžeme nahrát jen recepty, které byly vydány v lékárně (viz podmínka)
    def pridej_recept_do_faktury(self, recept, uhrada, je_vydano):
        self.recept = recept
        self.uhrada = uhrada
        self.je_vydano = je_vydano
        if self.je_vydano:
            self.celkova_uhrada += uhrada
            self.seznam_receptu.append(str(recept))
            return f"{self.seznam_receptu}"
        else: 
            print(f"Položka: {self.recept} ještě nebyla vydána.")

# Vytvoříme fakturu za měsíc říjen a nahrajeme do ní vydané recepty
faktura_rijen = Faktura()
faktura_rijen.pridej_recept_do_faktury(recept1, uhrada_recept1, recept1.je_vydano)
faktura_rijen.pridej_recept_do_faktury(recept2, uhrada_recept2, recept2.je_vydano)
# Přišlo se na to, že se zapomněl vydat recept na pana Bonda
faktura_rijen.pridej_recept_do_faktury(recept3, uhrada_recept3, recept3.je_vydano)

print(faktura_rijen)

# Vydání receptu na pana Bonda
recept2.vydani_receptu()
faktura_rijen.pridej_recept_do_faktury(recept2, uhrada_recept2, recept2.je_vydano)
print(faktura_rijen)


# A aby to bylo kompletní (už to teda nebude v Class):
# pojišťovna ve vyfakturovaných dokladech provede kontrolu pojištění pacientů
def kontrolor_pojisteni(objekt):
    pocitadlo = False
    for x in registr_pojistencu_obj:
        rc = x["rodné číslo"]
        if rc == objekt["rodné číslo"]:
            print("Pojištění je v pořádku.")
            pocitadlo = True
    if not pocitadlo:
        print("Rodné číslo není v evidenci!")

kontrolor_pojisteni(recept1.vrat_list())
kontrolor_pojisteni(recept2.vrat_list())
kontrolor_pojisteni(recept3.vrat_list())

# No a on ten prevít Bond nemá pojištění, protože je cizinec :-D


