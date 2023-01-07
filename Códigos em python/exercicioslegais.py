#criar uma variavel que recebe o valor por horas trabalhadas
valor_horas_trabalhadas = int(input("Digite o valor que recebe por hora: "))
#criar uma variavel que recebe a quantidade de horas trabalhadas no mes
horas_trabalhadas_mes = int(input("Digite a quantidade de horas que trabalha por mês: "))
#criar uma variavel que calculara o salario baseado nas horas e no valor por horas
salario = valor_horas_trabalhadas * horas_trabalhadas_mes
#criar uma variavel que calculara o imposto de renda
imposto_renda = 0
#criar uma variavel que calculara o valor do inss
inss = (salario * 10) / 100
#criar uma variavel que calculara o valor do fgts
fgts = (salario * 11) / 100
#criar uma variavel que calculara o novo salario
salario_liquido = 0

#verificar, a partir do salario, a quantidade de desconto que tera no salario
if(salario <= 900):
    salario_liquido = salario - inss
    print("Salário = {}".format(salario))
    print("Isento de imposto de renda")
    print("INSS = {}".format(inss))
    print("FGTS = {}".format(fgts))
    print("Salário líquido = {}".format(salario_liquido))
elif(salario > 900 and salario <= 1500):
    imposto_renda = (salario * 5) / 100
    salario_liquido = salario - inss - imposto_renda
    print("Salário = {}".format(salario))
    print("Imposto de renda = {}".format(imposto_renda))
    print("INSS = {}".format(inss))
    print("FGTS = {}".format(fgts))
    print("Salário líquido = {}".format(salario_liquido))
elif(salario > 1500 and salario <= 2500):
    imposto_renda = (salario * 10) / 100
    salario_liquido = salario - inss - imposto_renda
    print("Salário = {}".format(salario))
    print("Imposto de renda = {}".format(imposto_renda))
    print("INSS = {}".format(inss))
    print("FGTS = {}".format(fgts))
    print("Salário líquido = {}".format(salario_liquido))
else:
    imposto_renda = (salario * 20) / 100
    salario_liquido = salario - inss - imposto_renda
    print("Salário = {}".format(salario))
    print("Imposto de renda = {}".format(imposto_renda))
    print("INSS = {}".format(inss))
    print("FGTS = {}".format(fgts))
    print("Salário líquido = {}".format(salario_liquido))


#  criar duas variaveis que receberao notas de um aluno
#  nota1 = float(input("Digite a nota 1: "))
#  nota2 = float(input("Digite a nota 2: "))
#  criar uma variavel que calculara a media do aluno
#  media = (nota1 + nota2) / 2

#  #verificar, a partir da media, o conceito e a situação do aluno
#  if(media >= 9.0 and media <= 10):
#      print("Média = {}".format(media))
#      print("Conceito = A")
#      print("Aprovado")
#  elif(media >= 7.5 and media < 9):
#      print("Média = {}".format(media))
#      print("Conceito = B")
#      print("Aprovado")
#  elif(media >= 6.0 and media < 7.5):
#      print("Média = {}".format(media))
#      print("Conceito = C")
#      print("Aprovado")
#  elif(media >= 4.0 and media < 6.0):
#      print("Média = {}".format(media))
#      print("Conceito = D")
#      print("Reprovado")
#  elif(media >= 0 and media < 4.0):
#      print("Média = {}".format(media))
#      print("Conceito = E")
#      print("Reprovado")


#criar as variaveis equivalente aos lados do triângulo
#ladoA = int(input("Digite o valor do lado do triângulo: "))
#ladoB = int(input("Digite o valor do lado do triângulo: "))
#ladoC = int(input("Digite o valor do lado do triângulo: "))

#verificar se os lados formam um triângulo ou não
#if(((ladoA + ladoB) > ladoC) or ((ladoA + ladoC) > ladoB) or ((ladoB + ladoC) > ladoA)):
# #verifica, a partir dos lados do triângulo, qual nome ele recebe
#    if(ladoA == ladoB == ladoC):
#        print("Forma um triângulo Equilátero")
#    elif(ladoA == ladoB or ladoA == ladoC or ladoB == ladoC):
#        print("Forma um triângulo Isóceles")
#    elif(ladoA != ladoB != ladoC):
#        print("Forma um triângulo Escaleno")
#else:
#    print("Os valores informados não formam um triângulo")


#list = []
#soma = 0

#for i in range(1,5):
#    numero = int(input("Digite um número: "))
#    list.append(numero)   
#    soma += numero

#media = soma / 4    
#print(soma)
#print(media)


#list = []
#list_par = []
#list_impar = []

#for i in range(1,21):
#    numero = int(input("Digite um número: "))
#    list.append(numero)
    
#    if(numero %2 == 0):
#        list_par.append(numero)
#    else:
#        list_impar.append(numero)
        
#print("Vetor completo = {}".format(list))
#print("Vetor par = {}".format(list_par))
#print("Vetor impar = {}".format(list_impar))


#import calendar
#yy = 2023
#mm = 1
#print(calendar.month(yy,mm))