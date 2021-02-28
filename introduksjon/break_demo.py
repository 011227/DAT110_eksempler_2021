#break: Avbryter en løkke midt i

#While TRUE evig løkke
resultat=""
while True:
    linje = input("Skriv inn ei linje tekst")
    if linje == "":
        break
    resultat += linje + "\n"
print(resultat)
