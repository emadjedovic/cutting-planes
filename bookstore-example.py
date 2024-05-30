import lippy as lp
# lippy je Python biblioteka za rjesavanje problema linearnog programiranja

# funkcija cilja Z = 5x1 + 6x2 + 8x3

c_vektor = [5, 6, 8]

# ogranicenja

a_matrica = [
    [12, 15, 20],
    [0.5, 0.7, 1],
    [-1, 0, 0],
    [0, -1, 0],
    [0, 0, -1]]
b_vektor = [2000, 100, -10, -5, -8]

gomory = lp.CuttingPlaneMethod(c_vektor, a_matrica, b_vektor)
rjesenje = gomory.solve()

# ispis rezultata

print()
print("Optimalan broj knjiga za svaku kategoriju: ", rjesenje[0])
print("Maksimalni profit: ", rjesenje[1])
