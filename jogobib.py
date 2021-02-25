from time import sleep
certas = 0
while True:
    print('''Pergunta 1
    Quem fez a arca?
    [1] Noé
    [2] Adão
    [3] Moisés''')
    resposta1 = int(input('Sua escolha? '))
    sleep(1)
    if resposta1 == 1:
        certas = certas + 1
        print('Parabéns, você acertou!!!')
        break
    elif resposta1 == 2 or resposta1 == 3:
        print('Você errou!')
        break
    else:
        print('Resposta inválida!')
sleep(1)
while True:
    print('''Pergunta 2
    Quem matou Abel?
    [1] Tubalcaim
    [2] Jó
    [3] Caim''')
    resposta2 = int(input('Sua escolha? '))
    sleep(1)
    if resposta2 == 3:
        certas = certas + 1
        print('Parabéns, você acertou!!!')
        break
    elif resposta2 == 1 or resposta2 == 2:
        print('Você errou!')
        break
    else:
        print('Resposta inválida!')
sleep(1)
while True:
    print('''Pergunta 3
    Jesus foi batizado com quantos anos?
    [1] 33
    [2] 30
    [3] 20''')
    resposta3 = int(input('Sua escolha? '))
    sleep(1)
    if resposta3 == 2:
        certas = certas + 1
        print('Parabéns, você acertou!!!')
        break
    elif resposta3 == 1 or resposta3 == 3:
        print('Você errou!')
        break
    else:
        print('Resposta inválida!')
sleep(1)
while True:
    print('''Pergunta 4
    O nome da mãe de Jesus é?
    [1] Maria
    [2] Marta
    [3] Josefina''')
    resposta4 = int(input('Sua escolha? '))
    sleep(1)
    if resposta4 == 1:
        certas = certas + 1
        print('Parabéns, você acertou!!!')
        break
    elif resposta4 == 2 or resposta2 == 3:
        print('Você errou!')
        break
    else:
        print('Resposta inválida!')
sleep(1)
while True:
    print('''Pergunta 5
    Quem foi o primeiro homem?
    [1] Adão
    [2] Moisés
    [3] Pedro''')
    resposta5 = int(input('Sua escolha? '))
    sleep(1)
    if resposta5 == 1:
        certas = certas + 1
        print('Parabéns, você acertou!!!')
        break
    elif resposta5 == 2 or resposta5 == 3:
        print('Você errou!')
        break
    else:
        print('Resposta inválida!')
sleep(1)
while True:
    print('''Pergunta 6
    Quem batizou Jesus?
    [1] Tiago
    [2] João Batista
    [3] Marcos''')
    resposta6 = int(input('Sua escolha? '))
    sleep(1)
    if resposta6 == 2:
        certas = certas + 1
        print('Parabéns, você acertou!!!')
        break
    elif resposta6 == 1 or resposta6 == 3:
        print('Você errou!')
        break
    else:
        print('Resposta inválida!')
sleep(1)
while True:
    print('''Pergunta 7
    Quem ajudou a libertar os israelitas do Egito?
    [1] Balaão
    [2] Sansão
    [3] Moisés''')
    resposta7 = int(input('Sua escolha? '))
    sleep(1)
    if resposta7 == 3:
        certas = certas + 1
        print('Parabéns, você acertou!!!')
        break
    elif resposta7 == 1 or resposta7 == 2:
        print('Você errou!')
        break
    else:
        print('Resposta inválida!')
sleep(1)
while True:
    print('''Pergunta 8
    Qual profeta foi engolido por uma baleia?
    [1] Enoque
    [2] Joseph Smith
    [3] Jonas''')
    resposta8 = int(input('Sua escolha? '))
    sleep(1)
    if resposta8 == 3:
        certas = certas + 1
        print('Parabéns, você acertou!!!')
        break
    elif resposta8 == 1 or resposta8 == 2:
        print('Você errou!')
        break
    else:
        print('Resposta inválida!')
sleep(1)
while True:
    print('''Pergunta 9
    Qual apóstolo traiu Jesus?
    [1] Paulo
    [2] Judas
    [3] Pedro''')
    resposta9 = int(input('Sua escolha? '))
    sleep(1)
    if resposta9 == 2:
        certas = certas + 1
        print('Parabéns, você acertou!!!')
        break
    elif resposta9 == 1 or resposta9 == 3:
        print('Você errou!')
        break
    else:
        print('Resposta inválida!')
sleep(1)
while True:
    print('''Pergunta 10
    Quem foi para a cova dos leões?
    [1] Abdnego
    [2] Sadraque
    [3] Daniel''')
    resposta10 = int(input('Sua escolha? '))
    sleep(1)
    if resposta10 == 3:
        certas = certas + 1
        print('Parabéns, você acertou!!!')
        break
    elif resposta10 == 1 or resposta10 == 2:
        print('Você errou!')
        break
    else:
        print('Resposta inválida')
sleep(1)
print(f'Parabéns você acertou {certas} de 10 perguntas')
if certas >= 7:
    print('Você conhece bastante a Bíblia')
elif certas >= 4 and certas < 7:
    print('Ok, você precisa estudar mais')
else:
    print('Você não sabe quase nada sobre a Bíblia')