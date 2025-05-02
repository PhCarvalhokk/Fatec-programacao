peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

IMC = peso/(altura**2)

if IMC < 18.5:
    print("Abaixo do peso.")
elif IMC >= 18.5 and IMC < 25:
    print("Peso normal.")
elif IMC >= 25 and IMC < 30:
    print("Sobrepeso.")
elif IMC >= 30 and IMC < 35:
    print("Obesidade grau 1.")
elif IMC >= 35 and IMC < 40:
    print("Obesidade grau 2.")
else: 
    print("Obesidade grau 3.")