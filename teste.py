
aluno = input("Digite o nome do aluno: ")
materia = input("Digite o nome da Materia: ")
nota1 = int (input("Digite a primeira nota: "))
nota2 = int (input("Digite a segunda nota: "))
nota3 = int (input("Digite a terceira nota: "))
nota4 = int (input("Digite a quarta nota: "))

soma = (nota1+nota2+nota3+nota4)
print(f'A soma das notas é de {soma}')

print(f'A média das notas {nota1,nota2,nota3,nota4} do Aluno(a):{aluno} é {soma/4} na materia {materia}')