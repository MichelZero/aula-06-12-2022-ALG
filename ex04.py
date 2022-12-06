# autor:
# michel silva

# data: 06/12/2022
#
# 4 – ler uma lista de 5 números e imprimir o menor e
# maior valor.

lista1 = []
for i in range(5):
  # print(i)
  valor = int(input(f"informe o valor[{i}]: "))
  lista1.append(valor)

maior = max(lista1)
menor = min(lista1)
print(f"Maior ={maior}, Menor={menor}")