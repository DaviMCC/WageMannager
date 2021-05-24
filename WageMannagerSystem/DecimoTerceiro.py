from SalarioLiquido import calcularsalarioliquido
from SalarioLiquido import calcularDescontos

def calculardecimoterceiro (salarioBruto, mesesTrabalhados):

    primeiraParcela = (mesesTrabalhados * (salarioBruto / 12)) / 2
    totDesc = calcularDescontos(salarioBruto)
    INSS, IRRF = totDesc
    segundaParcela =  primeiraParcela  - (INSS + IRRF)
    tot = primeiraParcela + segundaParcela

    return primeiraParcela, segundaParcela, tot, INSS, IRRF

def calculaEprintaDecimoTerceiro():
    salarioBruto = float(input("Digite o salario bruto: "))

    if (salarioBruto >= 1100):

            mesesTrabalhados = int(input("Digite a quantidade de meses trabalhado:"))

            if(mesesTrabalhados < 1 or mesesTrabalhados > 12):

                print("O Décimo Terceiro requere no mínimo um mês trabalhado, e no máximo 12")
                calculaEprintaDecimoTerceiro()

            elif(mesesTrabalhados >= 1 or mesesTrabalhados <= 12):
                x = calculardecimoterceiro(salarioBruto, mesesTrabalhados)
                a, b, c , INSS, IRRF= x
                print(f"\n--- Primeira parcela: R${a:.2f}")
                print(f"--- Segunda parcela: R${b:.2f}")
                print(f"--- Desconto do INSS: R${INSS:.2f}")
                print(f"--- Desconto do IRRF: R${IRRF:.2f}")
                print(f"--- O valor total: R${c:.2f}\n")



    else:
            print("O salário minimo é R$1100,00")
            calculaEprintaDecimoTerceiro()


