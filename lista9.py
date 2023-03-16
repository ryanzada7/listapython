# criando uma lista com elementos duplicados 
lista_com_duplicatas = [1, 2, 3 ,1, 4, 2, 5, 6, 7, 8, 5, 9]

# Inicializando um lista vazia para armazenar os elementos unicos
lista_sem_duplicatas = []

# Usando um loop while para percorrer a lista e remover os elementos duplicados 
while lista_com_duplicatas:
    elemento = lista_com_duplicatas.pop(0) # pop é usada para remover o elemento 
    if elemento not in lista_sem_duplicatas:
        lista_sem_duplicatas.append(elemento)
        
# Imprimindo o resultado 
print("A lista sem duplicatas é:", lista_sem_duplicatas)