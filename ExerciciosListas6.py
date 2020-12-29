#Inicialize uma lista de 20 números inteiros. Armazene os números pares em uma lista PAR e os números ímpares em uma lista IMPAR. Imprima as listas PAR e IMPAR.
nums=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,18,19,20]
PAR = [i for i in nums if i%2 == 0]
print("Elementos Pares: ",PAR)
IMPAR = [i for i in nums if i%2 != 0]
print("Elementos Impares",IMPAR)