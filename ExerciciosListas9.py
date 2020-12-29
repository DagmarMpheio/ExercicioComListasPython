#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Em seguida, calcule a média anual das temperaturas e mostre a média calculada juntamente com todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 –Janeiro, 2 – Fevereiro, . . . ).
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