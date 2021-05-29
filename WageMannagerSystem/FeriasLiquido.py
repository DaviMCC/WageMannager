from SalarioLiquido import calcularsalarioliquido
from SalarioLiquido import calcularDescontos
def feriasLiquido(salarioBruto):

        feriasTot = salarioBruto + (salarioBruto / 3);
        salarioLiquido = calcularsalarioliquido(feriasTot)

        return salarioLiquido, feriasTot


def calculaEprintaFeriasLiquido():
    encerrar = False
    dados = []
    posicao = 0
    while not encerrar:
        nome=(input('\nNome do Funcionario.......: '))
        setor=input('Setor........: ')
        bonus=float(input('Bonus...: '))
        salarioBruto=float(input('Salario Bruto...: '))
        mesesTrabalhado=int(input('Meses trabalhados..: '))
        diasFerias =int(input('Dias de ferias.....: '))

        if (salarioBruto >= 1100):
            feriasLiquidotot, totSemDesconto = feriasLiquido(salarioBruto)
            feriasLiquidotot+= + bonus
            descontos = calcularDescontos(salarioBruto)
            INSS, IRRF, deduzirIrrf, deduzirInss, aliquotaInss, aliquotaIrrfs = descontos
            print(f"\n--- O valor do salário de ferias liquido é: "
                      f"R${feriasLiquidotot:.2f} ---\n")
            funcionario=[nome,setor,bonus,salarioBruto,mesesTrabalhado,diasFerias, feriasLiquidotot, INSS, IRRF, totSemDesconto,deduzirIrrf, deduzirInss,aliquotaInss, aliquotaIrrfs]
            dados.insert(posicao, funcionario)
            posicao+= 1
            print("\n---[0] - Encerrar ---")
            print("---[1] - Efetuar outro calculo ---")
            print("Resp....:")
            resp = int(input())
            if(resp == 0):
                for funcionario in dados:
                    print("\n ----- Extrato de Salário de Férias  -----")
                    print('\nNome.....:',funcionario[0])
                    print('Setor:....:',funcionario[1])
                    print('Bonus.....: R$',funcionario[2])
                    print('Salario Bruto....: R$',funcionario[3])
                    print('Meses Trabalhos..:',funcionario[4])
                    print('Dias de Ferias...:',funcionario[5])
                    print(f'\nSalario de Ferias Liquido.....: R${funcionario[6]:.2f}')
                    print(f"--- Salário sem descontos: R${funcionario[9]:.2f}")
                    print(f"\n--- INSS ---")
                    print(F"--- Desconto INSS aplicado: R${funcionario[7]:.2f}" + " ({0:.2f}%)".format(funcionario[7]/funcionario[3] * 100))
                    print(f'--- Aliquota INSS: {funcionario[12]}%')
                    print(f'\n--- IRRF ---')
                    print(F"--- Desconto IRRF aplicado: R${funcionario[8]:.2f}" + " ({0:.2f}%)".format((funcionario[8]/(funcionario[3] - funcionario[7]) * 100)))
                    print(f'--- Valor a deduzir IRRF: R${funcionario[11]:.2f}')
                    print(f'--- Aliquota IRRF: {funcionario[13]}')
                    print("\n --------------------------------------")
                    encerrar = True
        else:
            print("O salário minimo é R$1100,00")
            calculaEprintaFeriasLiquido()

