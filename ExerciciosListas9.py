#Fa�a um programa que receba a temperatura m�dia de cada m�s do ano e armazene-as em uma lista. Em seguida, calcule a m�dia anual das temperaturas e mostre a m�dia calculada juntamente com todas as temperaturas acima da m�dia anual, e em que m�s elas ocorreram (mostrar o m�s por extenso: 1 �Janeiro, 2 � Fevereiro, . . . ).
meses=[]
mes=['Janeiro','Fevereiro','Marco','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
for i in range(12):
    temp=float(input("temperatura: "))
    meses.append(temp)
media=sum(meses)/12
print("\nMedia Anual: ",media,"\n")
print("\t\t Temperaturas acima da media anual: ")
for i, p in enumerate(meses):
    if p>media:
        print(mes[i],"=>",p)