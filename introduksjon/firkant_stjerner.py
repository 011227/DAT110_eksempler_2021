#Eksempel: Ønsker å skrive ut en firkant av stjerner, hvor brukeren angir høyde og bredde

hoyde=int(input("Høyde på stjernen: "))
lengde=int(input("Lengde på stjernen: "))

resultat =""

for hoyde_index in range(hoyde):
    resultat =""
    for lengde_index in range(lengde):
        resultat+="*"
    print(resultat)

print()
for linje in range(hoyde):
    for tall in range(lengde):
        print("*", end="")
    print()

