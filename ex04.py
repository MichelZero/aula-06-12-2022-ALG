# autor:
# michel silva

# data: 06/12/2022
#
# 4 – ler uma lista de 5 números e imprimir o menor e
# maior valor.

lista1 = [] # lista vazia
for i in range(5):  # 0, 1, 2, 3, 4
  # print(i) # 0, 1, 2, 3, 4
  valor = int(input(f"informe o valor[{i}]: ")) 
  lista1.append(valor) # adiciona o valor no fim da lista 

maior = max(lista1) # maior valor da lista
menor = min(lista1) # menor valor da lista
print(f"Maior ={maior}, Menor={menor}") # imprime o maior e menor valor da lista
print("fim do programa")