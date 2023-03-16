# Criando uma lista de numeros 
numeros = [10, 20, 30, 40, 50]

# Inicializando a variavel que irá armazenar o maior numero
maior_numero = numeros[0]

# Usando um loop a variavel que ira armazenar o maior numero
for numero in numeros:
    if numero > maior_numero:
        maior_numero = numero 
        
# Imprimindo o resultado 
print("O maior numero na lista é", maior_numero)