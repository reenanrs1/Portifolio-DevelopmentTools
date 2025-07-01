def calcular_imc(peso, altura):
    try:
        imc = peso / (altura ** 2)
        return imc
    except ZeroDivisionError:
        return None

def classificar_imc(imc):
    if imc is None:
        return "Altura inválida. Não foi possível calcular o IMC."
    elif imc < 18.5:
        return "Baixo peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso adequado"
    elif 25.0 <= imc <= 29.9:
        return "Sobrepeso"
    elif 30.0 <= imc <= 34.9:
        return "Obesidade grau I"
    elif 35.0 <= imc <= 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

try:
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))
    imc = calcular_imc(peso, altura)
    print(f"Seu IMC é: {imc:.2f}")
    print("Classificação:", classificar_imc(imc))
except ValueError:
    print("Erro: insira apenas números válidos.")
