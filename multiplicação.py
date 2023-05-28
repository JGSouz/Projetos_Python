import Calculadora_definitiva
import pula_linha


def funcao_mult():
    mult()
    pula_linha.pula_linha()
    print("precisa realizar outro calculo? ")
    print("[1] Sim")
    print("[2] Não")
    resposta = int(input("digite o numero:"))
    if resposta == 1:
        Calculadora_definitiva.calculadora()
    else:
        print("Ok, obrigado pela preferencia")


def mult():
    print("Ok, digite o valor da operação")
    mul1 = int(input("Digite o primeiro valor:"))
    mul2 = int(input("Digite o segundo valor:"))
    resul = (mul1 * mul2)
    print("o resultado é", resul)


if __name__ == "__name__":
    funcao_mult()
