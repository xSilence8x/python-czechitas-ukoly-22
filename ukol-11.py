import re

with open("posta.html", encoding='utf-8') as vstup:
    data = vstup.read()

data = data.replace("\n", " ")
nova_data = re.sub("\s+", " ", data)

"""PSČ MĚSTO; 111 11 město nad čímkoliv (30)"""

hledana_shoda = re.compile(r"(\d{3} \d{2} )([a-zA-ZÀ-ž]+)( [a-zA-ZÀ-ž]+)?( [a-zA-ZÀ-ž]+)?( \d+)?") 

vysledky = hledana_shoda.findall(nova_data)

print(f"Celkový počet shod: {len(vysledky)}")

for x in vysledky:
    print(x[1], x[2], x[3])