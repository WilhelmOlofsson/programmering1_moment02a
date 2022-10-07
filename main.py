#Wilhelm Olofsson, Tk21
#Moment 02a
#Inte en särskilt svår uppgift utom att ge svar i två decimaler

π = 3.14

r = float(input("Cirkelns radie i centimeter:"))

print()

area = π * r * r

omkrets = (r + r) * π

print("Cirkelns area är %.2f" %area, "cm\u00b2") #%.2f ger svar med två variabler. Om 2 exempelvis ändras till 5 får svaret istället 5 variabler

print()

print("Cirkelns omkrets är %.2f" %omkrets, "cm")
