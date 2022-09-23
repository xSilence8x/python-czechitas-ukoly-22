baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}

vstup = input("Zadejte číslo balíku: ")

if vstup in baliky:
    if baliky.get(vstup) == True:
        print("Balík byl předán kurýrovi.")
    else:
        print("Balík zatím nebyl předán kurýrovi.")
else:
    print("Takový balíček neevidujeme.")