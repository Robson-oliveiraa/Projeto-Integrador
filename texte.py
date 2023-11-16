# import random

# alunos= []

# class Bateria():   

#     def __init__(self,alunos):
#         self.alunos = alunos

#     def DefinirOrdem(self, ListaAlunos):
#         ListaBateria = random.sample(ListaAlunos, len(ListaAlunos))
#         return  ListaBateria

# while True:
#     objeto = input("Nome:\n")
#     alunos.append(objeto)
#     reini = input('Reiniciar:\n[1]S\n[2]N\n')
#     try:
#         if reini == '2':
#             break
#     except:
#         print()

# Ordem_Bateria = Bateria(alunos)
# Ordem = Ordem_Bateria.DefinirOrdem(alunos)

# for pessoa in Ordem:
#     print(pessoa)


teste = ['1','2','3','4','5','6','7']
if len(teste) % 2 == 0:
    tamanho = (len(teste)/2)
    tamanho = int(tamanho)
    for i in range(tamanho):
        print(teste[i])

elif len(teste) % 2 == 1:
    teste.append(None)
    tamanho = (len(teste)/2)
    tamanho = int(tamanho)
    for i in range(tamanho):
        print(teste[i])
