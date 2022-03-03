import random
try:
    letrasMin = 'abcdefghijklmnopqrstuvxwxyz'
    letrasMaisc = letrasMin.upper()
    numeros = '0123456789'
    especiais = '!@#$%^&*(`)'
    senha = ''
    minusculas = input('Deseja incluir letras minúsculas? [S/N] ').strip().upper()[0]
    if minusculas == 'S':
        senha += letrasMin
    maisculas = input('Deseja incluir letras maiusculas? [S/N] ').strip().upper()[0]
    if maisculas == 'S':
        senha += letrasMaisc
    nums = input('Deseja incluir números? [S/N] ').strip().upper()[0]
    if nums == 'S':
        senha += numeros
    syms = input('Deseja incluir símbolos? [S/N] ').strip().upper()[0]
    if syms == 'S':
        senha += especiais
    tamanho = int(input('Qual o tamanho da senha? '))

    senha = ''.join(random.sample(senha, tamanho))
    print(f'Sua senha é: {senha}.')
except:
    print('Senha grande de mais, tente novamente.')