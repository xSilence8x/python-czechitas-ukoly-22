import math

def overovac_cisla(tel_cislo):
    tel_cislo = tel_cislo.replace(" ", "")
    if len(tel_cislo) == 9 or (len(tel_cislo) == 13 and tel_cislo[0:4] == "+420"):
        return True
    else:
        return False

def cena_sms(sms):
    pocet_znaku_sms = len(sms)
    cena_za_180_znaku = 3
    zaokrouhleny_pomer = math.ceil(pocet_znaku_sms / 180)
    return zaokrouhleny_pomer * cena_za_180_znaku


uzivatelovo_cislo = input("Zadejte telefonní číslo: ")

if overovac_cisla(uzivatelovo_cislo):
    uzivatelova_sms = input("Zadejte text Vaší sms zprávy: ")
    print(f"Cena Vaší SMS zprávy je: {cena_sms(uzivatelova_sms)} Kč.")
else:
    print("Vámi zadané číslo neexistuje.")