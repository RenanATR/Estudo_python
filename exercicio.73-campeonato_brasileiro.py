# #Exercicio 73

times = ("Botafogo",
"Palmeiras",
"Flamengo",
"Fluminense",
"Grêmio",
"Athletico-PR",
"Bragantino",
"Fortaleza",
"Cuiabá",
"São Paulo",
"Atlético-MG",
"Cruzeiro",
"Corinthians",
"Internacional",
"Goiás",
"Bahia",
"Santos",
"Vasco da Gama",
"Coritiba",
"América-MG"
)

print(f'Lista de Times do Brasileirão: {times}')
print('-='*20)

print(f'Os 5 primeiros são: {times[0:5]}')
print('-='*20)

print(f'Os 4 Ultimos são: {times[-4:]}') #do final para o começo da lista
print('-='*20)

print(f'times em ordem alfabética: {(sorted(times))}')
print('-='*20)
print(f'O Fortaleza está na {times.index("Fortaleza")+1}ª posição .')   