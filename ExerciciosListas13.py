#Utilizando listas fa�a um programa que fa�a 5 perguntas para uma pessoa sobre um crime. As perguntas s�o:
#1 "Telefonou para a v�tima?"
#2 "Esteve no local do crime?"
#3 "Mora perto da v�tima?"
#4 �Tinha d�vidas com a v�tima?"
#5 "J� trabalhou com a v�tima?�
#O programa deve no final emitir uma classifica��o sobre a participa��o da pessoa no crime. Se a pessoa responder positivamente a 2 quest�es ela deve ser classificada como "Suspeita�; entre 3 e 4 como "C�mplice" e; 5 como "Assassino". Caso contr�rio, ele ser� classificado como "Inocente".
perguntas=["1-Telefonou para a v�tima?","2-Esteve no local do crime?","3-Mora perto da v�tima?","4-Tinha d�vidas com a v�tima?","5-J� trabalhou com a v�tima?"]
contSim=0
contNao=0
for i in range(len(perguntas)):
        print(perguntas[i])
        res=int(input("1-SIM\n2-NAO\nResposta: "))
        if res==1:
                contSim=contSim+1
        elif res==2:
                contNao=contNao+1
        else:
                print("Resposta Invalida!")
                break
if contSim==2:
        print("Suspeita!")
elif contSim>=3 and contSim<=4:
        print("C�mplice")
elif contSim==5:
        print("Assassino!")
else:
        print("Inocente")
#print("{} sim's e {} nao's".format(contSim,contNao))