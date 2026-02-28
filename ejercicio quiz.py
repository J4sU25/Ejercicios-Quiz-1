def imprimir_pares(arreglo, n):
    for i in range(n):
        # El bucle interno itera 'n' veces por cada iteración del bucle externo
        for j in range(n):
            # Imprime la combinación de pares
            print(f"{arreglo[i]}-{arreglo[j]}")

# generamos el arreglo y la variable espacio para que pueda imprimir las combinaciones de pares
mi_arreglo = [1, 2, 3, 4, 5]
espacio = len(mi_arreglo)
imprimir_pares(mi_arreglo, espacio)
