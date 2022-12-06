
# autor:
# michel silva

# data: 06/12/2022
#
# 2 – ler uma lista de 5 número inteiros e imprimir na ordem inversa.

#
# ler uma lista de 5 número inteiros
lista1 = [] 
# indices: 0 1 2 3 e 4
# lista[0] = valor

for i in range(5): # 0, 1, 2, 3, 4
  # print(i)
  valor = int(input(f"informe o valor[{i}]: "))
  lista1.append(valor) # adiciona o valor no fim da lista

lista1.reverse() # inverte a ordem da lista 
print(lista1) # imprime a lista invertida

# imprimir cada número
for i in range(5):
  print(f"{i} -> {lista1[i]}") # imprime o indice e o valor do indice
  
""" lista2 = lista1
lista2[0] = 50
print(lista1)
print(lista2) """

l2 = lista1[::-1] # inverte a ordem da lista 
print(l2)

print("fim do programa")