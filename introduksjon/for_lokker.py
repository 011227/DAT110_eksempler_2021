#Fakultet

#Ber brukeren om input og konverterer strenget til et heltall
parameter = int(input("Hvilket tall vil du ha fakultet til? "))

while parameter < 0:
    print("Fakultet av et negativt tall finnes ikke!")
    parameter = int(input("Hvilket tall vil du ha fakultet til? "))

#Range går gjennom alle tall fra 0 til men ikke med parameteren
resultat = 1
for tall in range(1, parameter+1):
    resultat *= tall
    print(f"Tall: {tall} Foreløpig resultat: {resultat}")
print(resultat)

#print()
#liste = [1,3,6,9,11]
#for x in liste:
#    print(x)

#modifisere liste
#for index in range(len(liste))
#    liste[index]=2*liste[index]
