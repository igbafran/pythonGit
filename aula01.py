# print("HELLO WORLD!")
# print("Gabriella")
# #difernça entre texto e numero
# print(10+10) #realiza a soma
# print("10"+"10") #concatena = junta 10 com 10 =1010

# #operações matematicas
# #soma +
# #subtração -
# #multiplicação *
# #divisao /

# #exemplo
# print(2+2)
# print(10-5)
# print(10*2)
# print(20/2)

#PARAMETROS NO PRINT
#print(a,b,c,d,e...) até no maximo 128 paramentros
# print("escola senai")
# print("escola","senai") 
# print("10+10=", 10+10 )
# print("Gabriella Dos Santos França 16 47305012840")
# print("gabriella dos santos frança","16","47305012840")

#formatações Sep e End
#sep -> operador de separação
#troca o caractere padrão na virgula pelo setado dentro do sep
#end -> operador final
#colocar o caractere no final do print
#\n -> quebra linha
#limpar a tela
import os
os.system("cls")

# print("#"*5, "SEJA BEM VINDO","#"*5)
# print("aula" , "de" , "python", sep="@")
# print("aula","de" , "python", sep="@" ,end="! \n")
# print("no senai")

# print("outro \nexemplo")

#atividade1
print("curso","de","python", sep="_" , end="%"*2)
print("\n*no", "senai", "rio","claro")
print("_-_-_logica","de","programção" , sep="_-_-_")

#atividade2
print("python" , "versao" "3" , sep="@"*3 , end="[] \n")
print("logica" , "de" , "programação",sep="#"*3)
print("&uso" , "do" , "print" , sep="&" , end="()")