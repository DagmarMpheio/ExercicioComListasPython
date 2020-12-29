#Ler um vetor com 20 idades e exibir maior e menor.
idades=[]
for i in range(20):
    va=int(input("Idade: "))
    idades.append(va)
print(idades)
print("Maior: ",max(idades))
print("Menor: ",min(idades))