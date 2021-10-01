try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print(f'O problema encontrado foi {erro.__cause__}')
else:
    print(f'O resuntado é: {r}')

