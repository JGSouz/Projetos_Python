import Calculadora_definitiva
import pula_linha


def funcao_sub():
    sub()
    pula_linha.pula_linha()
    print("precisa realizar outro calculo? ")
    print("[1] Sim")
    print("[2] Não")
    resposta = int(input("digite o numero:"))
    if resposta == 1:
        Calculadora_definitiva.calculadora()
    else:
        print("Ok, obrigado pela preferencia")


def sub():
    print("Ok, digite o valor da operação")
    sub1 = int(input("Digite o primeiro valor:"))
    sub2 = int(input("Digite o segundo valor:"))
    print("o resultado é", sub1 - sub2)


if __name__ == "__main__":
    funcao_sub()
