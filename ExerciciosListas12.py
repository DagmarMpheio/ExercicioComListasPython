#Fa�a um programa que leia um n�mero indeterminado de notas. Ap�s esta entrada de dados, fa�a o seguinte:
#� Mostre a quantidade de notas que foram lidas.
#� Exiba todas as notas na ordem em que foram informadas.
#� Exiba todas as notas na ordem inversa � que foram informadas, uma abaixo do outra.
#� Calcule e mostre a soma das notas.
#� Calcule e mostre a m�dia das notas.
#� Calcule e mostre a quantidade de notas acima a m�dia calculada.
print("\t\tDigite um valor negativo para parar o programa")
notas=[]
while True:
    va=int(input("Valor: "))
    if va < 0:
        break
    else:
        notas.append(va)
print("Foram inseridas {} notas".format(len(notas)))
print("Notas Informadas: ",notas)
print("Notas Invertidas: ")
inv=notas[::-1]
for i in range(len(inv)):
    print(inv[i])
print("Soma das notas: ",sum(notas))
media=float(sum(notas)/len(notas))
print("Media das notas: ",media)
cont=0
for i in range(len(notas)):
    if media<notas[i]:
        cont=cont+1
print("Existe(m) {} nota(s) acima da media ".format(cont))