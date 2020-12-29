#Ler uma lista com 4 notas, em seguida o programa deve exibir as notas e a média.
lista=[]
for i in range(4):
    v=float(input("Nota: "))
    lista.append(v)
print(lista)
print("media = ",(sum(lista)/4))