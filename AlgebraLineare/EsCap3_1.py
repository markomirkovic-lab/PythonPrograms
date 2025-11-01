import numpy as np

def costruisci_matrice(m, n, x):
    # Creare un array di numeri consecutivi di lunghezza m * n, a partire da x
    elementi = np.arange(x, x + m * n)
    # Ridimensionare l'array in una matrice m x n
    matrice = elementi.reshape(m, n)
    return matrice

# Esempio di utilizzo:
m = 3  # numero di righe
n = 4  # numero di colonne
x = 5  # valore iniziale
matrice = costruisci_matrice(m, n, x)
print(matrice)
