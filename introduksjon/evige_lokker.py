#Skriv inn et antall tall, så skl den gjøre 1+2+3+...+antall

antall = int(input("Antall tall:"))
tall = 1
resultat = 0

while tall <= antall:
    resultat+=tall
    tall+=1
print(f"Resultatet ble: {resultat}")
