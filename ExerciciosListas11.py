#Faça um programa que crie uma matriz M (com valores informados do usuário) e mostre a matriz com o dobro dos valores lidos (2*M).
mat=[]
lin=int(input("Digite o numero de linhas: "))
col=int(input("Digite o numero de colunas: "))
for i in range(lin):
    val=[]
    for j in range(col):
        val.append(int(input("valores: ")))
    mat.append(val)
for i in range(lin):
    for j in range(col):
        mat[i][j]=mat[i][j]*2
print(mat)
    