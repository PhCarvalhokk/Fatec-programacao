idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))

if idade > 60: 
    print("Você tem direito ao benefício.")
elif idade > 18 and salario <= 2000:
    print("Você tem direito ao benefício.")
else:
    print("Você não tem direito ao benefício.")