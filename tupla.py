# Tuplas
# tuplas são imutáveis - Não podem ser alteradas

lanche = ("hamburguer","suco","pizza","pudim","batata frita")

# #mostra a posição dos parametros da TUPLA

for pos, comida in enumerate(lanche):
        print(f'Eu vou comer {comida} na posição {pos}.')
    
for food in lanche:
    print(lanche)

# Ajusta a ordem dos parametros

print(sorted(lanche))


