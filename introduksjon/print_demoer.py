print("Test")
print("En test til")
print("Tredje test")

#ikke linjeskift
print("Test", end="")
print("En test til")
print("Tredje test")

print("Test", end=" ")
print("En test til")
print("Tredje test")

print("tester linjeskift. \nDette kommer på ei ny linje. \n\tEtter tabulator")

#Printe ut spesialtegn
print("Spesialtegn: \" \\")

tall=5/3
test = "to"
streng=format(tall, "8.2f")
print(streng)
#tallet skal presentere 8 tegn, 2 bak komma

#en f-streng kan inkludere variabler
print(f"Tallet er {tall} og strengen er {test}")

# formattere tall
print(f"Tallet er {tall: 8.4f} og strengen er {test}")

heltall=123
print(f"Heltall: {heltall:6d}")

#5.2f: Flyttall med 5 siffer(inkludert kommaet), hvorav 2 er bak komma
# 8d: Heltall på vanlig format hvor den setter av 8 siffer.
# Høyrejustere hvis tallet ikke er så stort
# 10b: Binary tall format
# c -> for karakter
# x -> hexadeksimal 0-15
# e --> ekspnentaial funksjon * 10 ^noe

flyttall=5/3
print(str.format(("variabler {} {}"), heltall, flyttall))
#sette inn parameter samme versjon under men annen funksjon

print("Verdien ble %8.4f" % flyttall)

# fstreng er moderne
