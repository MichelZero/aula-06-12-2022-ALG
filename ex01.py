
# autor:
# michel silva

# data: 06/12/2022
#
# 1 – ler uma lista de 5 número inteiros e imprimir cada número 
# juntamente com a sua posição na lista.

#
# ler uma lista de 5 número inteiros
lista = []  # lista vazia
# indices: 0 1 2 3 e 4
# lista[0] = valor

for i in range(5):
  # print(i)
  valor = int(input(f"informe o valor[{i}]: "))
  lista.append(valor) # adiciona o valor no fim da lista

# imprimir cada número
for i in range(5):
  print(f"{i} -> {lista[i]}") # imprime o indice e o valor do indice
  
print("fim do programa")