#Inicialize uma lista de 20 números inteiros. Armazene os números pares em uma lista PAR e os números ímpares em uma lista IMPAR. Imprima as listas PAR e IMPAR.
numeros=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20]
par=[i for i in numeros if i%2==0]
impar=[i for i in numeros if i%2!=0]
print("Numeros Pares: ",par)
print("Numeros Impares: ",impar)

