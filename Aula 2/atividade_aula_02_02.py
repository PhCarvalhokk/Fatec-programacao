nota = int(input("Digite sua nota: "))

if nota >= 90:
    print("Aprovado com Excelência.")
elif nota >= 70 and nota < 90:
    print("Aprovado.")
elif nota >= 50 and nota < 70:
    print("Recuperação.")
else:
    print("Reprovado.")