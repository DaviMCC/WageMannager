from SalarioLiquido import calcularsalarioliquido

def feriasLiquido(salarioBruto):

        feriasTot = salarioBruto + (salarioBruto / 3);
        salarioLiquido = calcularsalarioliquido(feriasTot)

        return salarioLiquido


def calculaEprintaFeriasLiquido():
    salarioBruto = float(input("Digite o salario bruto: "))
    if (salarioBruto >= 1100):
        print(f"\n--- O valor do salário de ferias liquido é: "
              f"R${feriasLiquido(salarioBruto):.2f} ---\n")
    else:
        print("O salário minimo é R$1100,00")
        calculaEprintaFeriasLiquido()

