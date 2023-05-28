import Calculadora_definitiva
import pula_linha


def tabua():
    tabuada = int(input("Qual o valor desejado?"))
    tabuada_limite = int(input("Qual o valor limite desejado?"))
    tabu1 = tabuada
    tabu2 = 1
    while tabu2 <= tabuada_limite:
        resultado = tabu1 * tabu2
        print(tabu1, " * ", tabu2, "= ", resultado)
        tabu2 = tabu2 + 1


def funcao_tabua():
    tabua()
    pula_linha.pula_linha()
    print("precisa realizar outro calculo? ")
    print("[1] Sim")
    print("[2] Não")
    resposta = int(input("digite o numero:"))
    if resposta == 1:
        Calculadora_definitiva.calculadora()
    else:
        print("Ok, obrigado pela preferencia")


if __name__ == "__main__":
    funcao_tabua()
