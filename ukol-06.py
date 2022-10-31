with open("studenti-a-hodnoceni.txt", "r", encoding="utf-8" ) as file:
    stare_znamky = file.readlines()

a = [x.split("\t") for x in stare_znamky] # vytvori seznam seznamů

b = a.pop(0) # vyjme prvni radek ze seznamu ("jmeno", "prijmeni" a spol.)
b = [x.replace("\n", "") for x in b] # odstrani newline

jmena = [] # vytvori seznam slovniku studentu a jejich znamek
for x in a:
    jmena.append({
        b[0]: x[0], 
        b[1]: x[1], 
        b[2]: int(x[2]), 
        b[3]: int(x[3]), 
        b[4]: int(x[4]), 
        b[5]: int(x[5]), 
        b[6]: int(x[6]),
        b[7]: int(x[7])
        })

def zmen_znamky(znamka):
    if znamka == 1:
        znamka = "A"
    elif znamka == 2:
        znamka = "B"
    elif znamka == 3:
        znamka = "C"
    elif znamka == 4:
        znamka = "D"
    else:
        znamka = "F"
    return znamka

for x in jmena: # prepise znamky
    for i in range(2,8):
        x[b[i]] = zmen_znamky(x.get(b[i]))

d = [x.get(b[i]) for x in jmena for i in range(0,8) ] # vytvori seznam studentu a znamek
        
e = b + d # slouci seznamy

with open("nove-studenti-a-znamky.txt", "w", encoding="utf-8") as file:
    nove_znamky = []
    i=0
    for x in e:
        i+=1
        if i < 8:
            nove_znamky.append(x + "\t")
        else:
            nove_znamky.append(x + "\n")
            i = 0
    file.writelines(nove_znamky)