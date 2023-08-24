tupla = (1,2,3) #variaveis não mutaveis
tupla [0] #posição do dado na variavel
print(tupla[0])
lista = [1,2,3,4] # variaveis mutaveis
lista.append(5) # acrescenta dados na variavel
print(lista)

lista.reverse() #reverte os dados da variavel

print(lista)

lista[2]="três" # troca o dado informado da variavel
print(lista)

lista=[]
for numero in range(1,15): #Range - Gera sequencia numerica
    print(numero) 
    if len(lista) >0:
        multiplica=lista[-1]*numero
        lista.append(multiplica)
    else:
        lista.append(numero)
    print(lista)
        

        
        
    