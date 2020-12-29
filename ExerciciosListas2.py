#Ler uma lista de 5 números inteiros e mostre cada número juntamente com a sua posição na lista.
nums=[]
for i in range(5):
    va=int(input("Digite o valor: "))
    nums.append(va)
print("Valores: ")
for i , p in enumerate(nums):
    print(i+1,"=>",nums[i])

