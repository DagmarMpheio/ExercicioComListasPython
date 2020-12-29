#Ler uma lista de 10 números reais e mostre-os na ordem inversa.
lista=[]
for i in range(10):
    valor=int(input("Digite o valor "+str(i+1)+": "))
    lista.append(valor)
print(lista[::-1])