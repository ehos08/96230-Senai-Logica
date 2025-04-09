import os 
os.system("cls||clear")
def calculo_imc(peso, altura):
    """Calcula o IMC dado o peso e a altura."""
    return peso / (altura ** 2)

def classificar_imc(imc):
    """Classifica o IMC em categorias."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    elif 30 <= imc < 34.9:
        return "Obesidade Grau 1"
    elif 35 <= imc < 39.9:
        return "Obesidade Grau 2"
    else:
        return "Obesidade Grau 3"


peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))
imc = calculo_imc(peso, altura)
print(f"Seu IMC é: {imc:.2f} {classificar_imc(imc)}")
