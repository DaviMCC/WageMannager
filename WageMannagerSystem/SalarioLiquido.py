def faixa1():
    desconto = (0.075 * 1100.0)
    return desconto
def faixa2():
    desconto = (0.09 * 1103.60)
    return desconto
def faixa3():
    desconto = (0.12 * 1101.80)
    return desconto


def calcularsalarioliquido(salarioBruto):

        descontoINSS = 0.0
        descontoIRRF = 0.0

        if(salarioBruto >= 1100.00):
            if(salarioBruto == 1100.00):
                calculoTotal = salarioBruto - faixa1()
                print(F"Desconto INSS: R${faixa1():.2f}" + " ({0:.2f}%)".format(descontoINSS/calculoTotal * 100))
                return calculoTotal

            elif(salarioBruto > 1100.00 and salarioBruto <2203.45):
                descontoINSS = faixa1() + (0.09 * (salarioBruto - 1100.0))
                salarioDescontadoINSS = salarioBruto - descontoINSS

                if(salarioDescontadoINSS >= 1903.99):
                    descontoIRRF = (0.075 * salarioDescontadoINSS)
                    descontoIRRF = descontoIRRF - 142.80

                calculoTotal = salarioDescontadoINSS - descontoIRRF


                print(F"\nDesconto INSS: R${descontoINSS:.2f}" + " ({0:.2f}%)".format(descontoINSS/salarioBruto * 100))
                print(F"Desconto IRRF: R${descontoIRRF:.2f}" + " ({0:.2f}%)".format(descontoIRRF/salarioDescontadoINSS * 100))
                return calculoTotal

            elif(salarioBruto >= 2203.49 and salarioBruto <= 3305.22):
                descontoINSS = faixa1() + faixa2() + (0.12 * (salarioBruto - 2203.49))
                salarioDescontadoINSS = salarioBruto - descontoINSS

                if(salarioDescontadoINSS >= 2826.66):
                    descontoIRRF = (0.15 * salarioDescontadoINSS)
                    descontoIRRF = descontoIRRF - 354.80
                else:
                    descontoIRRF = (0.075 * salarioDescontadoINSS)
                    descontoIRRF = descontoIRRF - 142.80

                calculoTotal = salarioDescontadoINSS - descontoIRRF

                print(F"\nDesconto INSS: R${descontoINSS:.2f}" + " ({0:.2f}%)".format(descontoINSS/salarioBruto * 100))
                print(F"Desconto IRRF: R${descontoIRRF:.2f}" + " ({0:.2f}%)".format(descontoIRRF/salarioDescontadoINSS * 100))
                return calculoTotal

            elif(salarioBruto >= 3305.23 and salarioBruto <6433.57):
                descontoINSS = faixa1() + faixa2() + faixa3() + (0.14 * (salarioBruto - 3305.23))
                salarioDescontadoINSS = salarioBruto - descontoINSS

                if(salarioDescontadoINSS >= 3751.06 and salarioDescontadoINSS <= 4664.68):
                    descontoIRRF = (0.225 * salarioDescontadoINSS)
                    descontoIRRF = descontoIRRF - 636.13
                elif(salarioDescontadoINSS >= 4664.69):
                    descontoIRRF = (0.275 * salarioDescontadoINSS)
                    descontoIRRF = descontoIRRF - 869.36
                else:
                    descontoIRRF = descontoIRRF = (0.15 * salarioDescontadoINSS)
                    descontoIRRF = descontoIRRF - 354.80


                calculoTotal = salarioDescontadoINSS - descontoIRRF

                print(F"\nDesconto INSS: R${descontoINSS:.2f}" + " ({0:.2f}%)".format(descontoINSS/salarioBruto * 100))
                print(F"Desconto IRRF: R${descontoIRRF:.2f}" + " ({0:.2f}%)".format(descontoIRRF/salarioDescontadoINSS * 100))
                return calculoTotal

            elif(salarioBruto > 6433.57):
                descontoINSS =  751.99
                salarioDescontadoINSS = salarioBruto - descontoINSS

                if(salarioDescontadoINSS >= 4664.69):
                    descontoIRRF = (0.275 * salarioDescontadoINSS)
                    descontoIRRF = descontoIRRF - 869.36
                else:
                    descontoIRRF = descontoIRRF = (0.15 * salarioDescontadoINSS)
                    descontoIRRF = descontoIRRF - 354.80

            calculoTotal = salarioDescontadoINSS - descontoIRRF

            print(F"\nDesconto INSS: R${descontoINSS:.2f}" + " ({0:.2f}%)".format(descontoINSS/salarioBruto * 100))
            print(F"Desconto IRRF: R${descontoIRRF:.2f}" + " ({0:.2f}%)".format(descontoIRRF/salarioDescontadoINSS * 100))
            return calculoTotal


def calcularDescontos(salarioBruto):

    descontoINSS = 0.0
    descontoIRRF = 0.0
    deduzirIrrf = 0
    deduzirInss = 0
    aliquotaInss = 0
    aliquotaIrrf = " Isento"

    if(salarioBruto >= 1100.00):
        if(salarioBruto == 1100.00):
            aliquotaInss = 7.50
            aliquotaIrrf = " Isento"
            return faixa1(), descontoIRRF, deduzirIrrf, deduzirInss, aliquotaInss, aliquotaIrrf

        elif(salarioBruto > 1100.00 and salarioBruto <2203.45):
            descontoINSS = faixa1() + (0.09 * (salarioBruto - 1100.0))
            deduzirInss = 16.50
            salarioDescontadoINSS = salarioBruto - descontoINSS
            aliquotaInss = 7.50 + 9.00

            if(salarioDescontadoINSS >= 1903.99):
                descontoIRRF = (0.075 * salarioDescontadoINSS)
                descontoIRRF = descontoIRRF - 142.80
                deduzirIrrf = 142.80
                aliquotaIrrf = "7,5%"

            if(descontoIRRF == 0):
                deduzirIrrf = 0.0

            return descontoINSS, descontoIRRF, deduzirIrrf,deduzirInss,aliquotaInss, aliquotaIrrf

        elif(salarioBruto >= 2203.49 and salarioBruto <= 3305.22):
            descontoINSS = faixa1() + faixa2() + (0.12 * (salarioBruto - 2203.49))
            deduzirInss = 82.60
            salarioDescontadoINSS = salarioBruto - descontoINSS
            aliquotaInss = 7.50 + 9.00 + 12.00

            if(salarioDescontadoINSS >= 2826.66):
                descontoIRRF = (0.15 * salarioDescontadoINSS)
                descontoIRRF = descontoIRRF - 354.80
                deduzirIrrf = 354.80
                aliquotaIrrf = "15%"
            else:
                descontoIRRF = (0.075 * salarioDescontadoINSS)
                descontoIRRF = descontoIRRF - 142.80
                deduzirIrrf = 142.80
                aliquotaIrrf = "7.5%"

            if(descontoIRRF == 0):
                deduzirIrrf = 0.0

            return descontoINSS, descontoIRRF, deduzirIrrf, deduzirInss,aliquotaInss, aliquotaIrrf


        elif(salarioBruto >= 3305.23 and salarioBruto <6433.57):
                descontoINSS = faixa1() + faixa2() + faixa3() + (0.14 * (salarioBruto - 3305.23))
                deduzirInss = 148.71
                salarioDescontadoINSS = salarioBruto - descontoINSS
                aliquotaInss = 7.50 + 9.00 + 12.00 + 14.00

                if(salarioDescontadoINSS >= 3751.06 and salarioDescontadoINSS <= 4664.68):
                    descontoIRRF = (0.225 * salarioDescontadoINSS)
                    descontoIRRF = descontoIRRF - 636.13
                    deduzirIrrf = 636.13
                    aliquotaIrrf = "22,5%"
                elif(salarioDescontadoINSS >= 4664.69):
                    descontoIRRF = (0.275 * salarioDescontadoINSS)
                    descontoIRRF = descontoIRRF - 869.36
                    deduzirIrrf = 869.36
                    aliquotaIrrf = "27,5%"
                else:
                    descontoIRRF = descontoIRRF = (0.15 * salarioDescontadoINSS)
                    descontoIRRF = descontoIRRF - 354.80
                    deduzirIrrf = 354.80
                    aliquotaIrrf ="15%"

                if(descontoIRRF == 0):
                    deduzirIrrf = 0.0

                return descontoINSS, descontoIRRF, deduzirIrrf, deduzirInss,aliquotaInss, aliquotaIrrf


        elif(salarioBruto > 6433.57):
                descontoINSS =  751.99
                salarioDescontadoINSS = salarioBruto - descontoINSS
                aliquotaInss = 7.50 + 9.00 + 12.00 + 14.00

                if(salarioDescontadoINSS >= 4664.69):
                    descontoIRRF = (0.275 * salarioDescontadoINSS)
                    descontoIRRF = descontoIRRF - 869.36
                    deduzirIrrf = 869.36
                    aliquotaIrrf = "27,5%"

                else:
                    descontoIRRF = descontoIRRF = (0.15 * salarioDescontadoINSS)
                    descontoIRRF = descontoIRRF - 354.80
                    deduzirIrrf = 354.80
                    aliquotaIrrf = "15%"

                if(descontoIRRF == 0):
                    deduzirIrrf = 0.0

                return descontoINSS, descontoIRRF, deduzirIrrf, deduzirInss,aliquotaInss, aliquotaIrrf


def calculaPrintaSalarioLiquido():
    encerrar = False
    dados = []
    posicao = 0
    while not encerrar:
        nome=(input('\nNome do Funcionario.......: '))
        setor=input('Setor........: ')
        bonus=float(input('Bonus...:R$ '))
        salarioBruto=float(input('Salario Bruto...:R$ '))
        mesesTrabalhado=int(input('Meses trabalhados..: '))
        diasFerias =int(input('Dias de ferias.....: '))

        if (salarioBruto >= 1100):
            salarioLiquidoToT = calcularsalarioliquido(salarioBruto) + bonus
            descontos = calcularDescontos(salarioBruto)
            INSS, IRRF, deduzirIrrf, deduzirInss,aliquotaInss, aliquotaIrrfs = descontos
            print(f"\n--- O valor do salário liquido é: "
                  f"R${salarioLiquidoToT:.2f} ---\n")
            funcionario=[nome,setor,bonus,salarioBruto,mesesTrabalhado,diasFerias, salarioLiquidoToT, INSS, IRRF, deduzirIrrf, deduzirInss,aliquotaInss, aliquotaIrrfs]
            dados.insert(posicao, funcionario)
            posicao+= 1
            print("\n---[0] - Encerrar ---")
            print("---[1] - Efetuar outro calculo ---")
            print("Resp....:")
            resp = int(input())
            if(resp == 0):
                for funcionario in dados:
                    print("\n ----- Extrato de Salário  -----")
                    print('\nNome...:',funcionario[0])
                    print('Setor:...:',funcionario[1])
                    print('Bonus....: R$',funcionario[2])
                    print('Salario Bruto....: R$',funcionario[3])
                    print('Meses Trabalhos..:',funcionario[4])
                    print('Dias de Ferias...:',funcionario[5])
                    print(f'\nSalario  Liquido.....: R${funcionario[6]:.2f}')
                    print(f"--- Salário sem descontos: R${funcionario[3]:.2f}")
                    print("\n--- INSS ---")
                    print(F"--- Desconto INSS aplicado: R${funcionario[7]:.2f}" + " ({0:.2f}%)".format(funcionario[7]/funcionario[3] * 100))
                    print(f'--- Aliquota INSS: {funcionario[11]}%')
                    print('\n--- IRRF ---')
                    print(F"--- Desconto IRRF aplicado: R${funcionario[8]:.2f}" + " ({0:.2f}%)".format((IRRF/(funcionario[3] - funcionario[7]) * 100)))
                    print(f'--- Valor a deduzir IRRF: R${funcionario[9]:.2f}')
                    print(f'--- Aliquota IRRF: {funcionario[12]}')
                    print("\n --------------------------------------")
                    encerrar = True

        else:
            print("O salário minimo é R$1100,00")
            calculaPrintaSalarioLiquido()





