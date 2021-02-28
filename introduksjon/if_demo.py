#flytskjema: boks viser hva ting gjør
#diamant: option

tall_streng = input("Skriv inn tall for å sjekke om det er negativt: ")
tall = float(tall_streng)

if tall < 0.0:
    print("Tallet er negativt")
    print("Tester ei linje til")
elif tall == 0.0:
    print("Tallet er eksakt 0")
else:
    print("Tallet er positivt")
    print("Tester.....")
print("Avslutter")

# Ta inn alder og sjekk om personen er tenåring. Tallet er mellom 13-19

if tall >=13.0 and tall <=19.0:
    print("Personen er tenåring")
else:
    print("Personen er ikke tenåring")
print("Avslutt")

# har and, or, not
#not det som står etter må være usant = not
