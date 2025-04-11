import math
from math import sqrt, hypot, radians, trunc
print(f"\n\033[1;32m{' CALCULADORA ':=^35}\033[0m")
nome = input('Bem vindo à calculadora do pedrAo! Qual é o seu nome? ')

while True:

    oPC = input(f'O que irá fazer, {nome}?  \n { "_" * 25} \n [1]- Calculos algébricos \n [2]- Calculos geométricos \n [3]- Sair \n { "_" * 25} \n ').lower().strip()
    if oPC not in ('1', '2'):
        print('Até mais programador!!')
        break

    #Calculos geométricos
    elif oPC ==('2'):
        print(f"\n\033[1;32m{' CALCULADORA GEOMÉTRICA ':=^35}\033[0m")
        oPG = (input(f' { "_" * 25} \n Qual operação geométrica irá usar? \n [1]- Calculo da Hipotenusa \n [2]- Seno, cosseno e tangente \n [3]- Porção real do número \n { "_" * 25} \n ')).strip()
        if oPG not in ('1', '2', '3'):
            print('Digitou errado parsa')
        if oPG =='1':
            CO = float(input('Valor do cateto oposto da hipotenusa: '))
            CA = float(input('Valor do cateto adjacente da hipotenusa: '))
            hipotenusa = hypot(CO, CA)
            print(f'A hipotenusa do cateto oposto {CO} e do cateto adjacente {CA} é igual a {hipotenusa:.2f} ')

        if oPG =='2':
            angulo = float(input('Digite o angulo à ter seu seno, cosseno e tangente calculados: '))
            radiano = radians(angulo)
            seno = math.sin(math.radians(angulo))
            cosseno = math.cos(math.radians(angulo))
            tangente = math.tan(math.radians(angulo))
            print(f'O valor de seno, cosseno e tangente deste ângulo é, respectivamente: \n {seno:.2f} \n {cosseno:.2f} \n {tangente:.2f}')

        if oPG =='3' :
            numero = float(input('Digite o número inteiro para ter sua porção real dita: '))
            porção = (numero.__trunc__())
            print(f'A porção real do número escolhido é {porção}')



    elif oPC =="1":

        #raiz quadrada
        print(f"\n\033[1;32m{' CALCULADORA ALGÉBRICA ':=^35}\033[0m")
        oPM = input(f' { "_" * 25} \n Qual operação algébrica irá usar? \n [1]- Adição \n [2]- Subtração \n [3]- Multiplicação \n [4]- Divisão \n [5]- Raiz quadrada \n [6]- Potência \n [7]- Porcentagem \n { "_" * 25} \n  ').strip()
        if oPM not in ("1", "2", "3", "4", "5", "6", "7"):
            print('Erro! Opção incorreta.')
            continue
        if oPM=='5':
            n1r = int(input('Calcule a raiz quadrada de: '))
            if n1r <0:
                print('Erro! Número negativo.')
            else:
                r1 = sqrt(n1r)
        if oPM=='7':
            np1 = float(input('Digite quantos % do número irá querer: '))
            np2 = float(input('Digite o número para calcular a porcentagem: '))

            rp = (np1 * np2 / 100)


        #variáveis das operações algébricas
        else:

            n1 = int(input('Digite um número: '))
            n2 = int(input('Digite outro número: '))
            a = (n1 + n2)
            s = (n1 - n2)
            m = (n1 * n2)
            d = (n1 / n2)
            p = (n1**n2)

        #operações
        if oPM =='1':
            print(f'A soma de {n1} e {n2} dá {a}.')
        elif oPM =='2':
            print(f'A subtração de {n1} e {n2} dá {s}.')
        elif oPM == '3':
            print(f'A multiplicação de {n1} e {n2} dá {m}.')
        elif oPM =='4':
            if n2 == (0):
                print('Erro! Não existe divisão por zero.')
            else:
                print(f'A divisão de {n1} e {n2} dá {d}.')

        elif oPM=='5':
            print(f'A raiz quadrada de {n1r} é {r1}.')
        elif oPM=='6':
            print(f'A potência de {n1} elevado à {n2} é {p}.')
        elif oPM=='7':
            print(f'{np1}% de {np2} é igual a {rp}. ')
        else:
            print('TA ERRADO VEI')
