import os
os.system("cls")

#ESTRUTURA CONDICIONAL IF ELSE (se senao) -> True or False (Verdadeiro ou Falso)
#OPERADORES CONDICIONAIS:  > >= < <= != == and or
# > (maior)
# >= ( maior OU igual)
# < (menor)
# <= (menor OU igual)
# == (igual) 
# != (diferente)
# and (e) -> Se apenas uma ou mais condiçoes for FALSA ele retorna FALSE 
# or (ou) -> Se apenas uma ou mais condições for VERDADE ele retorna TRUE

#if condicao :
# print("verdade")
#else: 
#print("falso")

# A IDENTAÇÃO (ESPAÇO) deve ser utilizado o TAB

# x=10  

# if x > 1000:
#     print("verdade")
# else:
#     print("falso")
#     print("falso")
#     print("falso")
#     print("falso")

# nome = "teste"
# if "testee" != nome:
#     print(1)
# else:
#     print(2)

    #ativ.01

# idade=float(input("Digite a sua idade"))
# if idade > 18:
#     print("maior de idade")
# else:
#     print("menor de idade")

# #ativ.02 (desafio)

# idade=float(input("Digite a sua idade: "))
# if idade == 0 or idade > 120:
#     print("idade invalida")
# else:
#     print("idade valida")


#ativ.03

# email=(input("Digite seu email: "))
# senha=(input("Digite sua senha: "))

# if "python@senai.com" == email:
#     if"12345678" == senha:

#         print("USUARIO AUTENTICADO")
# else:
#     print("USUARIO OU SENHA INVALIDA")    

#ativ. maças

# print("*"*15, "MAÇAS DA APPLEJACK", "*"*15 )
# print("R$: 0.30 -> MENOS QUE UMA DUZIA")
# print("R$:0.25 -> PELO MENOS DOZE")
# print("*"*15, "QUANTIDADE", "*"*15)

# qtd = int (input("digite a quantidade de maças que deseja levar:"))

# if qtd < 12 :
#     calc = qtd * 0.30
#     print("voce ira pagar (o,30 uni) : R$ " , calc)
# else:
#     calc=qtd * 0.25
#     print("voce ira pagar (0,25 uni): R$" , calc)

#ativ.01

# vogal= (input("digite uma vogal: "))


# if vogal == "a" or vogal=="e"or vogal=="i" or vogal=="o" or vogal=="u" or vogal== "A" or vogal== "E" or vogal== "I" or vogal== "O" or vogal== "U":
#     print("essa letra é uma vogal")
# else:
#     print("essa letra é consoante")

    #ativ.02

num1=float(input("digite um numero: "))
num2=float(input("digite outro numero: "))

if num1 > num2:
    print(f"o maior numero é: {num1}")
    print(f"o menor numero é: {num2}")
else:
    print(f"o maior numero é {num2}")
    print(f"o menor numero é: {num1}")
    