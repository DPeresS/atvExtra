
from doctest import OutputChecker

opcao=0
while(opcao<1 or opcao>4):
    print("Calculadora Simples")
    print("--------------------")
    print("")
    n1=float(input("Digite o primeiro número: "))
    n2=float(input("Digite o segundo número: "))
    print("")
    print("Escolha uma operação:")
    print("1. Adição ( + )")
    print("2. Subtração ( - )")
    print("3. Multiplicação ( * )")
    print("4. Divisão ( / )")
    opcao=int(input("Opção: "))
    if(opcao<1 or opcao>4):
        OutputChecker.clear()
print("")
if(opcao==1):
     print("Resultado:",  n1, "+", n2, "=", n1+n2)
elif(opcao==2):
     print("Resultado:",  n1, "-", n2, "=", n1-n2)
elif(opcao==3):
     print("Resultado:",  n1, "x", n2, "=", n1*n2)
elif(opcao==4 and n2!=0):
     print("Resultado:",  n1, "/", n2, "=", n1/n2)
else:
    print("Resultado: Não é possível dividir ", n1, " por 0.")
