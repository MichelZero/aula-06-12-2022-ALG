## autor:
# michel silva

# data: 06/12/2022
#
# 3 – ler uma lista de 4 notas e em seguida mostra as notas e a média
listaNotas = []
for i in range(4):
  nota = int(input('informe a nota:' ))
  listaNotas.append(nota)

print(listaNotas)
media = sum(listaNotas) / len(listaNotas)
print(f"média = {media}")