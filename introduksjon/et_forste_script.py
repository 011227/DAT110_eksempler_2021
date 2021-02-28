5#Oppgaven: Ønske på å regne ut arealet til rom hvor brukeren oppgir lengde og bredde

#Psuedokode
# Be brukeren om lengde
# Be brukeren om bredde
# Regne ut arealet
# Skrive ut arealet

lengde = float(input("Lengden til rommet i meter: "))
bredde = float(input("Bredden til rommet i meter: "))

areal = round(lengde * bredde,2)

print("Arealet ble: " + str(areal))
print("Arealet til rommet er", areal)

