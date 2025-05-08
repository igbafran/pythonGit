import os
os.system("cls")

#continuação Input com Int e Float
#int() -> converte para inteiro
#float()-> converte para n quebrado

#exemplo1
# numero = 10
# numero2 = input("digite um numero: ")
# print("o tipo de numero é," , type(numero2))
# soma= numero + int (numero2)
# print(f"soma de {numero} + {numero2} = " , soma)

#exemplo2
# num1 = input("digite um numero:")
# soma = float(num1) + 15
# print("A soma de ",num1 , "+", "15","=", soma)

#exemplo3
# n1 = float(input("digite um numero: "))
# n2 = float(input("digite outro numero: "))

# soma = n1+n2

# print(f"a soma de {n1} + {n2} = ", soma)

#ativ.1

# n1 = float(input("digite um numero: "))
# n2 = float(input("digite outro numero: "))

# multiplicacao = n1*n2

# print(f"a multiplicação de {n1} * {n2} =", multiplicacao)

#ativ.2

# n1=float(input("digite um numero: "))
# print(f"antecessor: {n1-1}")
# print(f"sucessor: {n1+1}")

#ativ.3

# n1= float(input("digite o seu ano de nascimento: "))
# print(f"sua idade é: {2025 - n1}")

#porcentagem

# print("25% de 100 =", 0.25* 100)
# print("4% de 400 =", 0.04 * 400)
# print("99% de 1525= ", 0.99 * 1525)

# #supondo que um produto custa 150 reais
# #e o caixa deu um desconto de 15%


#ativ.4
print("="*15, "SUPERMERCADO","="*15)
item1 =(input( "Digite o nome do produto1: "))
valor1 =float(input("Valor: "))
item2=(input("digite o nome do produto2:"))
valor2=float(input("valor: "))
desconto1= valor1 * 0.10
desconto2= valor2 * 0.25

valorfinal1 = round(valor1-desconto1)
valorfinal2 = round(valor2-desconto2)


print("="*15, "CAIXA", "="*15)



print(f"preco do {item1} custa {valor1} com 10% de desconto:  {valorfinal1}")
print(f"preco do {item2} custa {valor2} com 25% de desconto:  {valorfinal2}")

print("."*20, "TOTAL","."*20)
total= valorfinal1+valorfinal2
print(f"TOTAL DA COMPRA R$: :{total}")

#round(valor, quantidade de casas decimais) -> faz o arredondamento dos valores