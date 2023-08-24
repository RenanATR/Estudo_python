#Exercicio 72 - Mostrando numero por extenso

cont = ('zero','um','dois','três','quatro',
        'cinco','seis','sete','oito','nove','dez',
        'onze','doze','treze','quatorze','quinze',
        'dezeseis','dezesete','dezoito','dezenove','vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <=20:
        break
    print('Tente Novamente. ', end='')

print(f'Você Digitou o numero {cont[num]}')

while True:
        sim = input('Quer tentar de novo?: ')
        if sim == 'y' or "sim":
                continue
        else:
                print("Você não quer mais. Obrigado!")
