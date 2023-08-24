class Cliente:
    def __init__(self, nome, email,plano):
        
        self.nome = nome
        self.email = email
        self.lista_planos = ["basic","premium","family"]
        self.plano = plano
        
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception("Plano Inválido")
        
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else: 
            print("Plano Inválido")
            
    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'"Você pode ver o Filme:"{filme}"')
        elif self.plano == "premium":
            print(f'"Você pode ver o Filme:"{filme}"')
        elif self.plano =="basic" and plano_filme=="premium":
            print("Faça upgrade para Ver Esse Filme")
        else:
            print("Plano Invalido")
                    
cliente = Cliente("Rodrigo","rodrigogostosomanhoso@gmail.com","premium")
print(cliente.plano)

#botão de upgrade de plano
cliente.mudar_plano("basic")

#botão de Ver Filme
print(f'Você mudou se Plano para: {cliente.plano}')
cliente.ver_filme("Eu vi","premium")

