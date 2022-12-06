## autor:
# michel silva

# data: 06/12/2022
#
# 3 – ler uma lista de 4 notas e em seguida mostra as notas e a média
listaNotas = [] # lista vazia 
for i in range(4): # 0, 1, 2, 3
  nota = int(input('informe a nota:' ))
  listaNotas.append(nota) # adiciona a nota no fim da lista 

print(listaNotas) # imprime a lista de notas 
media = sum(listaNotas) / len(listaNotas) # calcula a média das notas 
print(f"média = {media}") # imprime a média das notas
print("fim do programa")