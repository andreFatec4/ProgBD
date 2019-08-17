salarioFunc = float(input('Digite o Salário do Funcionário: R$ '))
gratif = salarioFunc * 0.05
imposto = salarioFunc * 0.07
salarioLiquido = salarioFunc+gratif-imposto
print ("Salário a receber = R$", round(salarioLiquido, 2))