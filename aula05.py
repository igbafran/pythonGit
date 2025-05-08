import os
os.system("cls")

#IF ENCADEADO -> TESTA TODAS AS CONDIÇÕES MESMO SE UMA FOR VERDADEIRA
#ELIF -> TESTA TODAS AS CONDIÇÕES ATÉ UMA SER VERDADEIRA


# x = 15 

# if x <=20 :
#     print("entrou no if 14")
# if x <=15 :
#     print("entrou no if 15")
# if x <=16:
#     print("entrou no if 16")


# if x <=20:
#     print("entrou no if 14")
# elif x<=15:
#     print("entrou no if 15")
# elif x <=16:
#     print("entrou no if 16")


# ESCREVA UM PROGRAMA EM PYTHON NA QUAL O USUARIO DIGITA A IDADE
#  SE MENOR QUE 12 -> CRIANÇA
#  SE MENOR QUE 18 -> ADOLESCENTE
#  SE MENOR QUE 60 -> ADULTO
#  SE NAO -> IDOSO


# NO CASO SE USAR IF ELE VAI TESTAR TODAS AS CONDIÇÕES
# idade = int(input("digite sua idade: "))

# if idade < 12:
#     print("criança")
# if idade < 18:
#     print("adolescente")
# if idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")


# SE USAR ELIF ELE VAI TESTAR UMA E SAIR DA ESTRUTURA
# if idade < 12:
#     print("criança")
# elif idade < 18:
#     print("adolescente")
# elif idade< 60:
#     print("adulto")
# else: 
#     print("IDOSO")

#===========================================================
#replace("valor1","valor2") -> Substitui o valor1 pelo valor2

#o do professor

# n1= float(input("digite a 1º nota: ") .replace(",", ","))
# n2=float(input("digite a 2º nota: ") .replace ("," , ","))

# media= (n1+n2)/2
# #:.2f -> formata para 2 casas decimais apenas no fstring
# print(f"media: {media:.2f}")

# if media <5:
#     print("reprovado")
# elif media >=5 and media<=7:
#     print("em recuperação")
# else:
#     print("aprovado")

#============================================================
# ativ.01
# nota1=float(input("digite sua primeira nota: "))
# nota2=float(input("digite sua segunda nota: "))
# calc= (nota1+nota2) /2
# print("media do aluno:" , calc)

# if calc < 5:
#     print("reprovado")
# elif calc<7:
#     print("em recuperaçao")
# else:
#     print("aprovado")

#==========================================================
#ativ.02

# print("==========INDICE DE MASSA CORPOREO==========")
# peso=float(input("Digite seu peso: "))
# altura=float(input("Digite sua altura: "))
# calc=round (peso/(altura*altura)) 

# print(f"Seu IMC é: {calc}")

# if calc < 17:
#     print("muito abaixo do peso")
# elif calc >=17 and calc <= 18.49:
#     print("abaixo do peso")
# elif calc >=18.5 and calc <= 24.99:
#     print("peso normal")
# elif calc >= 25 and calc <= 29.99:
#     print("acima do peso")
# elif calc >= 30 and calc <= 34.99:
#     print("obesidade I")
# elif calc >= 35 and calc <= 39.99:
#     print("obesidade II")
# else:
#     print("obesidade III")

#=========================================================
#ativ.03

# print("."*20, "REAJUSTE AUTOCAR", "."*20)

# print(r"""                                          ,-~ |            
#        ________________          o==]___|            
#       |                |            \ \              
#       |________________|            /\ \             
#  __  /  _,-----._      )           |  \ \.           
# |_||/_-~         `.   /()          |  /|]_|_____     
#   |//              \ |              \/ /_-~     ~-_  
#   //________________||              / //___________\ 
#  //__|______________| \____________/ //___/-\ \~-_   
# ((_________________/_-o___________/_//___/  /\,\  \  
#  |__/(  ((====)o===--~~                 (  ( (o/)  ) 
#       \  ``==' /                         \  `--'  /  
#        `-.__,-'                           `-.__,-'                                        
                                                           
#                 """)
# print("."*70)
# print("TABELA DE REAJUSTE DE SALARIO:")
# print("Salario até R$ 2799,99: AUMENTO DE 20%")
# print("Salario entre R$ 2800,00 E R$6999,99: AUMENTO DE 15%")
# print("Salario entre R$ 7000,00 e R$14999,99: AUMENTO DE 10%")
# print("Salario de R$ 15000,00 em diante:aumento de 5%")
# print("."*70)
# salario=float(input("Digite seu salario R$: "))
# aum20= 0.20*salario
# aum15= 0.15*salario
# aum10= 0.10*salario
# aum5= 0.5*salario


   
















































































# elif  salario >= 2800.99 and salario < 6999.99 :
#     print("voce recebeu um aumento de: ",0.15 * salario )
# elif salario >= 7000.00 and salario < 14999.99 :
#     print("voce recebeu um aumento de: ",0.10 * salario )
# else:
#     print("voce recebeu um aumento de: ",0.5 * salario ) 



