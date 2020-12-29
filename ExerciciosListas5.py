#Ler um vetor com 20 idades e exibir a maior e menor.
idades=[]
for i in range(20):
    v=int(input("Idade: "))
    idades.append(v)
print("Maior Idade: ",max(idades)," Menor Idade: ",min(idades))