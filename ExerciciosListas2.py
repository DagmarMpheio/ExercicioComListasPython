#Ler uma lista de 5 n�meros inteiros e mostre cada n�mero juntamente com a sua posi��o na lista.
nums=[]
for i in range(5):
    va=int(input("Digite o valor: "))
    nums.append(va)
print("Valores: ")
for i , p in enumerate(nums):
    print(i+1,"=>",nums[i])

