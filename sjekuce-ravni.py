import lippy as lp
# lippy je Python biblioteka za rjesavanje problema linearnog programiranja

c_vektor = [3, 3, 7]
a_matrica = [
    [1, 1, 1],
    [1, 4, 0],
    [0, 0.5, 3]
]
b_vektor = [3, 5, 7]

gomory = lp.CuttingPlaneMethod(c_vektor, a_matrica, b_vektor)
print("Rjesenje: ", gomory.solve())