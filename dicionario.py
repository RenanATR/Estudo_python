emails_gerentes={
    "iguatemi":"iguatemi@gmail.com",
    "Plaza":"plaza@gmail.com",
    "Barra":"barra@gmail.com"
    }

#adicionar chave e valor no dicionário
emails_gerentes["Leblon"] = "leblon@gmail.com" 

#trazer a informação do dicionario exata com variavel
email = emails_gerentes ["Leblon"] 
print(email)

#for shopping in emails_gerentes:
    #print(shopping)
    
#Keys.Chaves do dicionario
print(emails_gerentes.keys())

#Ver todas as cheves e valores

for shopping in emails_gerentes:
        email= emails_gerentes[shopping]
        print(email)
        
#Dicionario.Values
print(emails_gerentes.values())
    
#Deletar uma das Chaves
emails_gerentes.pop("Leblon")
print(emails_gerentes)
    
if "ipanema" in emails_gerentes:
    print("Existe")
else:
    print("Não Existe")