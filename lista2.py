# Criando uma lista 
minha_lista = [1, 2, 3, 4, 5]
# Usando um loop for para percorrer a lista e imprimir cada elemento 
for i in range(len(minha_lista)):
    print("o elemento", i+1, "da lista é", minha_lista[i])
    
    # Criamdo uma lista de numeros 
numeros = [1, 2, 3, 4, 5]
# Usando um loop for para percorrer a lista e imprimir cada elemento 
for numero in numeros:
    print(numero, " - com for")
        
# Usano um loop while para percorrrer aa lista e imprimir cada elemento 
i = 0 
while i < len(numeros):
    print(numeros[i], " - com while")
    i += 1