peso = float(input("Digite peso (Kg): "))
altura = float(input("Digite sua altura (m):"))

imc = peso / (altura**2)

print(f"Seu IMC é {imc:.2f}")