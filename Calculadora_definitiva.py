import soma
import subtração
import divisão
import multiplicação
import tabuada
import pula_linha


def calculadora():
    print("*******************************************************************")
    print("Escolha a Operação desejada")
    print("[1] -- Soma")
    print("[2] -- Subitração")
    print("[3] -- Divisão")
    print("[4] -- Multiplicação")
    print("[5] -- Tabuada")
    print("[6] -- Sair")
    chave1 = int(input("Digite o Numero da operação desejada:"))
    print("*******************************************************************")

    pula_linha.pula_linha()

    if chave1 == 1:
        soma.funcao_soma()

    elif chave1 == 2:
        subtração.funcao_sub()

    if chave1 == 3:
        divisão.funcao_div()

    elif chave1 == 4:
        multiplicação.funcao_mult()

    if chave1 == 5:
        tabuada.funcao_tabua()

    elif chave1 == 6:
        funcao_fim()


def funcao_fim():
    saida()


def saida():
    print("Ok, obrigado pela preferencia")


if __name__ == "__main__":
    calculadora()
