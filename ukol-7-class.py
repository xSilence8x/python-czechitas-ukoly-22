# Otevírací doba kina:
# 1. 7. 2021 - 10. 8. 2021 = 250 Kč/ os.
# 11. 8. 2021 - 31. 8. 2021 = 180 Kč/ os.

# TODO
# input = počet osob + datum 
# -> string datum => datetime.strptime()

from datetime import datetime

sezona1_start = datetime(2021, 7, 1)
sezona1_end = datetime(2021, 8, 10)
sezona1_cena = 250
sezona2_start = datetime(2021, 8, 11)
sezona2_end = datetime(2021, 8, 31)
sezona2_cena = 180


class Nakup:
    def __init__(self, input_datum, input_pocet):
        self.datum = datetime.strptime(input_datum, "%d. %m. %Y")
        self.pocet_osob = input_pocet

    def __str__(self):
        if sezona1_start <= self.datum <= sezona1_end:
            return f"Cena za vstupenky je {self.pocet_osob * sezona1_cena} Kč."
        elif sezona2_start <= self.datum <= sezona2_end:
            return f"Cena za vstupenky je {self.pocet_osob * sezona2_cena} Kč."
        else:
            return f"Kino je zavřené."

nakup1 = Nakup(input("Zadej datum ve formátu dd. mm. yyyy: "), int(input("Zadej počet lístků: ")))
print(nakup1)

