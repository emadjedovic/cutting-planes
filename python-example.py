import lippy as lp
# biblioteka za rjesavanje problema linearnog programiranja

# ------------------------------------------------------------

# PRIMJER I
# funkcija cilja Z = 3x1 + 3x2 + 7x3

c_vektor = [3, 3, 7]

# ogranicenja

a_matrica = [
    [1, 1, 1],
    [1, 4, 0],
    [0, 0.5, 3]]
b_vektor = [3, 5, 7]

gomory = lp.CuttingPlaneMethod(c_vektor, a_matrica, b_vektor)
rjesenje = gomory.solve()

# ispis rezultata

print()
print("Optimalne vrijednosti varijabli: ", rjesenje[0])
print("Vrijednost funkcije cilja: ", rjesenje[1])

# ------------------------------------------------------------

# PRIMJER II
# funkcija cilja Z = 7x1 + 9x2

c_vektor = [7, 9]

# ogranicenja

a_matrica = [
    [-1, 3],
    [7, 1]]
b_vektor = [6, 35]

gomory = lp.CuttingPlaneMethod(c_vektor, a_matrica, b_vektor)
rjesenje = gomory.solve()

# ispis rezultata

print()
print("Optimalne vrijednosti varijabli: ", rjesenje[0])
print("Vrijednost funkcije cilja: ", rjesenje[1])


# ------------------------------------------------------------

# OPTIMIZACIJA KNJIZARE
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
