from SalarioLiquido import calcularsalarioliquido
from SalarioLiquido import calcularDescontos

def calculardecimoterceiro (salarioBruto, mesesTrabalhados):

    primeiraParcela = (mesesTrabalhados * (salarioBruto / 12)) / 2
    totDesc = calcularDescontos(salarioBruto)
    INSS, IRRF, deduzirIrrf, deduzirInss, aliquotaInss, aliquotaIrrfs= totDesc
    segundaParcela = primeiraParcela - (INSS + IRRF)
    tot = primeiraParcela + segundaParcela
    totsemdesc = primeiraParcela * 2

    return primeiraParcela, segundaParcela, tot, INSS, IRRF, totsemdesc,deduzirIrrf, deduzirInss, aliquotaInss, aliquotaIrrfs

def calculaEprintaDecimoTerceiro():
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
            if(mesesTrabalhado < 1 or mesesTrabalhado > 12):
                print("O Décimo Terceiro requere no mínimo um mês trabalhado, e no máximo 12")
                calculaEprintaDecimoTerceiro()

            elif(mesesTrabalhado >= 1 or mesesTrabalhado <= 12):
                x = calculardecimoterceiro(salarioBruto, mesesTrabalhado)
                a, b, c , INSS, IRRF, totsemdesc, deduzirIrrf, deduzirInss,aliquotaInss, aliquotaIrrfs = x
                print(f"\n--- Valor total Décimo Terceiro: R${c:.2f}\n")
                funcionario=[nome,setor,bonus,salarioBruto,mesesTrabalhado,diasFerias, c, INSS, IRRF, a, b, totsemdesc, deduzirIrrf, deduzirInss, aliquotaInss, aliquotaIrrfs]
                dados.insert(posicao, funcionario)
                posicao+= 1
                print("\n---[0] - Encerrar ---")
                print("---[1] - Efetuar outro calculo ---")
                print("Resp....:")
                resp = int(input())
                if(resp == 0):
                    for funcionario in dados:
                        print("\n ----- Extrato de Décimo Terceiro -----")
                        print('\nNome.......:',funcionario[0])
                        print('Setor:....',funcionario[1])
                        print('Bonus...: R$',funcionario[2])
                        print('Salario Bruto...: R$',funcionario[3])
                        print('Meses Trabalhados....:',funcionario[4])
                        print('Dias de Ferias.....:',funcionario[5])
                        print(f'\nSalario Décimo Terceiro Total.....: R${funcionario[6]:.2f}')
                        print(f"--- Salário sem descontos: R${funcionario[11]:.2f}")
                        print(f"--- Primeira parcela: R${funcionario[9]:.2f}")
                        print(f"--- Segunda parcela: R${funcionario[10]:.2f}")
                        print(f"\n--- INSS ---")
                        print(F"--- Desconto INSS aplicado: R${funcionario[7]:.2f}" + " ({0:.2f}%)".format(funcionario[7]/funcionario[3] * 100))
                        print(f'--- Aliquota INSS: {funcionario[14]}%')
                        print(f'\n--- IRRF ---')
                        print(F"--- Desconto IRRF aplicado: R${funcionario[8]:.2f}" + " ({0:.2f}%)".format((funcionario[8]/(funcionario[3] - funcionario[7]) * 100)))
                        print(f'--- Valor a deduzir IRRF: R${funcionario[13]:.2f}')
                        print(f'--- Aliquota IRRF: R${funcionario[15]}')
                    print("\n --------------------------------------")
                    encerrar = True


        else:
                print("O salário minimo é R$1100,00")
                calculaEprintaDecimoTerceiro()

