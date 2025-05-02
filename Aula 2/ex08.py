preco_og = int(input("Digite o preço original: "))
desconto = int(input("Digite o desconto: "))
preco_f = (preco_og - preco_og * (desconto/100))
print ("O produto que custava " + str(preco_og) + " " + "com desconto de " + str(desconto) + "% " + "agora custa " + str(preco_f))