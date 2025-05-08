import os
os.system("cls")
#ESTRUTURAS CONDICIONAIS IF ELSE (ELIF)
# SWITCH CASE -> (MATCH CASE) ESCOLHA CASO (A PARTIR DA VERSAO 3.10)
#match valor:
# case valor:


# linguagem="klo"

# match linguagem:
#     case "python":
#         print("é facil")
#     case "java":
#         print("muito codigo, python faz com menos linhas") 
#     case "c#":
#         print("massa")       
#     case "js":
#         print("sou do back")
#     case "html":
#         print("kauan nao dorme")
#     case 10:
#         print("entrou aqui") 
#     case "klo":
#         print("kloe cartiel cavarielli")    
#     case _:
#          print("outro caso")

#ATIVIDADE calendario

# print("*"*15, "CALENDARIO" ,  "*"*15)

# semana=int(input("Digite o numero do dia da semana: "))
# match semana:
#     case 1:
#         print("segunda")
#     case 2:
#         print("terca")
#     case 3:
#         print("quarta")
#     case 4:
#         print("quinta")
#     case 5:
#         print("sexta")
#     case 6:
#         print("sabado")
#     case 7:
#         print("domingo")
     
#ATIVIDADE LOJA DE CELULAR

# print("="*15,"KLOE CELL", "="*15)

# print("1- IPHONE 15 - R$5000,00")
# print("2- XIAOMI REDMI 13 PRO PLUS 512GB - 2500,00 ")
# print("3- SANSUNG S25 265 GB - 6000,00")

# print("="*20, "FRETE", "="*20)

# print("SP-> 10,00")
# print("MG->15,00")
# print("RS->20,00")
# print("="*50)
# prod=input("digite o nº do produto: ")
# estado=input("digite a sigla do estado: ")






# match prod:
#     case "1":
#         match estado:
#             case"SP":
#                 print("preço:5000,00")
#                 print("frete: R$:10")
#                 print("total:5010,00")
#             case"MG":
#                 print("preço:5000,00")
#                 print("frete: R$:15")
#                 print("total:5015,00")
#             case "RS":
#                 print("preço:5000,00")
#                 print("frete: R$:20")
#                 print("total:5020,00")
#     case"2":
#         match estado:
#             case"SP": 
#                 print("preço:2500,00")
#                 print("frete: R$:10")
#                 print("total:2510,00")  
#             case"MG":
#                 print("preço:2500,00")
#                 print("frete: R$:15")
#                 print("total:2515,00")
#             case "RS":
#                 print("preço:2500,00")
#                 print("frete: R$:20")
#                 print("total:2520,00")
#     case"3":
#         match estado:
#             case "SP":
#                 print("preço:6000,00")
#                 print("frete: R$:10")
#                 print("total:6010,00")  
#             case"MG":
#                 print("preço:6000,00")
#                 print("frete: R$:15")
#                 print("total:6015,00")
#             case "RS":
#                 print("preço:6000,00")
#                 print("frete: R$:20")
#                 print("total:6020,00")


# #PROFESSOR

# print(""" 
# MUNDO CELULAR
      
# 1-IPHONE -> 5000
# 2-MOTO G -> 3000
# 3-LENOVO -> 2500

# FRETE: 
#       SP -> 10,00
#       RS -> 20,00
#       RJ -> 30,00      
# """)

# celular = int(input("Digite a opção desejada: "))
# estado = input("Digite a sigla do estado para entrega: ").lower()
# valor=0
# frete=0
# valortotal=0
# match celular:
#     case 1:
#         valor=5000
#     case 2:
#         valor=3000
#     case 3:
#         valor=2500

# match estado:
#     case "sp":
#         frete=10
#     case "rs":
#         frete=20
#     case "rj":
#         frete=30

# valortotal= valor + frete

# print(f"VALOR CELULAR:R$ {valor:.2f}")
# print(f"VALOR FRETE R$: {frete:.2f}")
# print(f"VALOR TOTAL R$: {valor+frete:.2f}")
                         


# import random

# valor = 0
# #randint(valorinicial,valorfinal)
# valor = random.randint(0,100) #gera de 1 ate 99 aleatoriamente

# match valor:

#     case _ if valor <50 : 
#         print("menor que 50")
#     case _ if valor ==50:
#         print("= 50")
#     case _ if valor > 50:
#         print("maior que 50")


# # Desenhos pedra papel tesoura

# papel = """
#      _______
# ---'    ____)____
#            ______)
#           _______)
#          _______)
# ---.__________)
# """

# pedra = """
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# """


# tesoura = """
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)

# """

#atividade pedra papel tesoura

print("="*15,"PEDRA PAPEL TESOURA", "="*15)

player=input("DIGITE PEDRA PAPEL OU TESOURA: ")
import random
maquina=random.randint(1,3)

match maquina:
    case _ if  maquina ==1:
        print(r""" 

   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
        
    PEDRA
              
              """)

    case _ if maquina == 2:
        print(r""" 

    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
              
    PAPEL
              
              """)
    case _ if maquina == 3:
         print(r""" 

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

    TESOURA
              
              """)
         





         
match player:
    case _ if  player =="pedra":
        print(r""" 

   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
        
    PEDRA
              
              """)
        jogada=1

    case _ if player == "papel":
        print(r""" 

    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
              
    PAPEL
              
              """)
        jogada=2
    case _ if player == "tesoura":
         print(r""" 

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

    TESOURA
              
              """)
         jogada=3

print("="*60)

match jogada: 
    case _ if jogada==1 and maquina==1:
        print("EMPATOU MIGA")
    case _ if jogada==1 and maquina==2:
        print("VOCE PERDEU BOBONA")
    case _ if jogada==1 and maquina==3:
        print("VOCE GANHOU NEGAH!")
        
match jogada: 
    case _ if jogada==2 and maquina==1:
        print("VOCE GANHOU NEGAH!")
    case _ if jogada==2 and maquina==2:
        print("EMPATOU MIGA")
    case _ if jogada==2 and maquina==3:
        print("VOCE PERDEU MIGA")

match jogada: 
    case _ if jogada==3 and maquina==1:
        print("VOCE PERDEU BOBONA")
    case _ if jogada==3 and maquina==2:
        print("VOCE GANHOU NEGAH!")
    case _ if jogada==3 and maquina==3:
        print("EMPATOU MIGA")
        

         

       




         

        
        


        
        


       









                       









