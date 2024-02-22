from funções import *

opcao = 0

while opcao != "1" "2" "3" "4" "5" "6":



    print("CARDÁPIO")
    cardapio = {"misto quente":10.00, "pão na chapa":7.00, "pão de queijo":6.00, "ovos mechidos":10.00, "ovos mechidos com bacon":12.00,
                "água":3.00, "suco":10.00, "refrigerante":8.00, "café expresso":4.00, "café com leite":6.00, "capuccino":8.00 }
    print(cardapio)

    print("____________________________")
    print("FAÇA O SEU PEDIDO")

    print("____________________________")
    print('''    [1]  - misto quente
    [2]  - pão na chapa
    [3]  - pão de queijo
    [4]  - ovos mechidos
    [5]  - ovos mechidos com bacon
    [6]  - água
    [7]  - suco
    [8]  - refrigerante
    [9]  - café expresso
    [10] - café com leite
    [11] - capuccino
    [12] - Cancelar pedido''')
    print("____________________________")

    opcao =  (input("Qual pedido deseja fazer [1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]: "))


    if opcao == "1":
        misto_quente()
        break

    elif opcao == "2":
        pao_na_chapa()
        break

    elif opcao == "3":
        pao_de_queijo()
        break

    elif opcao == "4":
        ovos_mechidos()
        break

    elif opcao == "5":
        ovos_mechidos_bacon()
        break

    elif opcao == "6":
        agua()
        break

    elif opcao == "7":
        sabor_suco = input("qual sabor do suco?: ")
        suco(sabor_suco)
        break

    elif opcao == "8":
        refrigerante()
        break

    elif opcao == "9":
        cafe_expresso()
        break

    elif opcao == "10":
        cafe_com_leite()
        break

    elif opcao == "11":
        capuccino()
        break

    elif opcao == "12":
        print("cancelando pedido...")
        break

    else:
        print("pedido inválido, tente novamente")