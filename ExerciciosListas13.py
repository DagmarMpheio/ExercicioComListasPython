#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#1 "Telefonou para a vítima?"
#2 "Esteve no local do crime?"
#3 "Mora perto da vítima?"
#4 “Tinha dívidas com a vítima?"
#5 "Já trabalhou com a vítima?“
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita“; entre 3 e 4 como "Cúmplice" e; 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
perguntas=["1-Telefonou para a vítima?","2-Esteve no local do crime?","3-Mora perto da vítima?","4-Tinha dívidas com a vítima?","5-Já trabalhou com a vítima?"]
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
        print("Cúmplice")
elif contSim==5:
        print("Assassino!")
else:
        print("Inocente")
#print("{} sim's e {} nao's".format(contSim,contNao))