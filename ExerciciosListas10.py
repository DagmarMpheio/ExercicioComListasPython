#Faça um programa que crie uma matriz aleatoriamente. O tamanho da matriz deve ser informado pelo usuário.
import random
print("\t\t Matriz")
mat=[]
lin=int(input("Digite o numero de linhas: "))
col=int(input("Digite o numero de colunas: "))
for i in range(lin):
    val=[]
    for j in range(col):
        val.append(random.randint(-100,100))
    mat.append(val)
print(mat)