#1
num = float(input("Digite um número: "))

if num > 0:
    print("O número é positivo.")
elif num < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")

#2
num = int(input("Digite um número inteiro: "))

if num % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

#3
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

#4
idade = int(input("Digite sua idade: "))

if idade < 12 or idade > 60:
    print("O valor do ingresso é R$ 15,00.")
else:
    print("O valor do ingresso é R$ 30,00.")

#5
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O maior número é {num1}.")
elif num2 > num1:
    print(f"O maior número é {num2}.")
else:
    print("Os números são iguais.")

#6
nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    print("Aprovado.")
elif nota >= 5 or nota <= 6.9:
    print("Recuperação.")
else:
    print("Reprovado.")    

#7
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

IMC = peso/(altura**2)

if IMC < 18.5:
    print("Abaixo do peso.")
elif IMC >= 18.5 and IMC < 25:
    print("Peso normal.")
elif IMC >= 25 and IMC < 30:
    print("Sobrepeso.")
elif IMC >= 30:
    print("Obesidade.")

#8
a = float(input("Digite o primeiro lado do triângulo: "))
b = float(input("Digite o segundo lado do triângulo: "))
c = float(input("Digite o terceiro lado do triângulo: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Triângulo Equilátero.")
    elif a == b or a == c or b == c:
        print("Triângulo Isósceles.")
    else:
        print("Triângulo Escaleno.")
else:
    print("Os valores informados não formam um triângulo.")

#9
salario = float(input("Digite seu salário: "))

if salario < 2000:
    bonus = salario * 0.20
elif 2000 <= salario <= 5000:
    bonus = salario * 0.10
else:
    bonus = salario * 0.05

print(f"Seu bônus será de R$ {bonus:.2f}.")

#10
ano = int(input("Digite um ano: "))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print("Ano bissexto.")
else:
    print("Não é bissexto.")

#11
import random

numero_secreto = random.randint(1, 10)
tentativa = int(input("Tente adivinhar o número (entre 1 e 10): "))

if tentativa > numero_secreto:
    print("Muito alto!")
elif tentativa < numero_secreto:
    print("Muito baixo!")
else:
    print("Parabéns! Você acertou.")

#12
temp = float(input("Digite a temperatura em °C: "))

if temp < 15:
    print("Frio")
elif 15 <= temp <= 25:
    print("Agradável")
else:
    print("Quente")

#13
valor_compra = float(input("Digite o valor da compra: "))

if valor_compra > 100:
    print("Frete grátis!")
else:
    print("Frete de R$ 15,00.")

#14
nota = float(input("Digite a nota (0 a 10): "))

if 9 <= nota <= 10:
    print("Conceito A")
elif 7 <= nota < 9:
    print("Conceito B")
elif 5 <= nota < 7:
    print("Conceito C")
elif 3 <= nota < 5:
    print("Conceito D")
else:
    print("Conceito E")

#15
idade = int(input("Digite sua idade: "))
cartao_e = input("Possui cartão estudantil? (S/N): ")

if idade < 6 or idade > 65:
    print("Grátis.")
elif cartao_e == "S":
    print("Meia entrada.")
else:
    print("Inteira.")

#16
salario_bruto = float(input("Digite o salário bruto: "))

if salario_bruto <= 1900:
    print("Isento.")
elif 1900 < salario_bruto <= 2800:
    print("Alíquota de 7.5%.")
elif 2800 < salario_bruto <= 3700:
    print("Alíquota de 15%.")
elif 3700 < salario_bruto <= 4600:
    print("Alíquota de 22.5%.")
else:
    print("Alíquota de 27.5%.")

#17
valor = int(input('Digite o valor do saque: '))

notas_cem = int(valor / 100)
valor %= 100
notas_cinquenta = int(valor / 50)
valor = valor % 50
notas_vinte = int(valor / 20)
valor = valor % 20
notas_dez = int(valor / 10)
valor %= 10

print('Notas de R$ 100: ' + str(notas_cem))
print('Notas de R$ 50: ' + str(notas_cinquenta))
print('Notas de R$ 20: ' + str(notas_vinte))
print('Notas de R$ 10: ' + str(notas_dez))

#18
usuario_correto = "admin"
senha_correta = "1234"

tentativas = 3  

while tentativas > 0:
    
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Login bem sucedido!")
        break
    else:
        tentativas -= 1
        print(f"Usuário ou senha incorretos! Você tem mais {tentativas} tentativa(s).")

    
    if tentativas == 0:
        print("Conta bloqueada. Número máximo de tentativas excedido.")
    
#19
idade_atleta = int(input("Digite a idade do atleta: "))

if idade_atleta <= 12:
    print("Categoria Infantil.")
elif idade_atleta > 12 or idade_atleta < 18:
    print("Categoria Juvenil.")
elif idade_atleta >= 18 or idade_atleta <= 40:
    print("Categoria Adulto.")
else:
    print("Categoria Veterano")

#20
idade = int(input("Digite a idade: "))
gestante = input("Está grávida? (S/N): ")
deficiente = input("Possui alguma deficiência? (S/N): ")

if idade >= 60 or deficiente == 'S':
    print("Prioridade Máxima")
elif gestante == 'S':
    print("Prioridade Média")
else:
    print("Atendimento Normal")