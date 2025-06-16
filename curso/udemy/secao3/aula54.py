"""

Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista
"""

import os

lista_compras = []

while True:
    print("Selecione uma opção")
    opcao = input("[i]nserir [a]pagar [l]istar [s]air: ")

    if opcao == "i":
        os.system("clear")
        valor_digitado = input("Valor: ")
        lista_compras.append(valor_digitado)
    elif opcao == "a":
        os.system("clear")
        valor_digitado = int(input("Escolha o índice para apagar: "))
        try:
            lista_compras.pop(valor_digitado)
        except ValueError:
            print("Por favor digite um número inteiro")
        except IndexError:
            print(f"O índice {valor_digitado} não existe na lista")
        except Exception:
            print("Erro desconhecido")
    elif opcao == "l":
        os.system("clear")
        if not lista_compras:
            print("A lista esta vazia")
        else:
            for indice, valor in enumerate(lista_compras):
                print(f"{indice} {valor}")
    elif opcao == "s":
        break
    else:
        print("Opção inválida, por favor escolha i, a, l ou s")
