import random

numeros = ["1","2","3","4","5","6","7","8","9","10"]
letras = ["A","B","C","D","a","b","c","d"]
codigo = ""

for i in range(6):
    nOuL = random.randint(1,2)
    if nOuL == 1:
        sort = random.randint(0,9)
        codigo += str(numeros[sort])
    else:
        sort = random.randint(0,7)
        codigo += letras[sort]

codigo = str(codigo)
print(codigo)
confCod = input('Digite o codigo:\n')
if confCod == codigo:
    print('Codigo certo👌')

else:
    print('Codigo errado👎, paia')