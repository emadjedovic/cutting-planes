import lippy as lp
# lippy je Python biblioteka za rjesavanje problema linearnog programiranja

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
