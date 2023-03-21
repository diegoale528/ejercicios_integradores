# Escribir una función que calcule el mínimo común múltiplo entre dos números

def mcm(a, b):
    z = max(a, b)

    while True:
        if (z % a == 0) and (z % b == 0):
            return z
        
        z += 1

print(mcm(20, 12))
print(mcm(25, 52))
