# Escribir una función que calcule el máximo común divisor entre dos números.

def mcd(a, b):
    mcd = 1
    for x in range(a, 0, -1):
        if a % x == 0 and b % x == 0:
            mcd = x
            break
    return mcd

print(mcd(166,249))
print(mcd(250,360))
print(mcd(360,690))
