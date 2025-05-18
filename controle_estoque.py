import json

with open('estoque.json', 'r') as file:
    estoque = json.load(file)


def listar_medicamentos():
    print("\nMedicamentos disponíveis:")
    for nome in estoque:
        print(f"- {nome.capitalize()}")


def consultar_medicamento(nome):
    print()
    medicamento = estoque.get(nome.lower())
    if medicamento:
        print(json.dumps(medicamento, indent=4, ensure_ascii=False))
    else:
        print("❌ Medicamento não encontrado.")


def buscar_quantidade(lugar):
    print(f"\nQuantidades na unidade '{lugar}':")
    encontrado = False
    for nome, dados in estoque.items():
        local = dados["presente"].get(lugar.lower())
        acima_ideal = local['quantidade'] > local['ideal'] if local else False
        diferenca = local['quantidade'] - local['ideal'] if local else 0
        if local:
            print(f"- {nome.capitalize()}: {local['quantidade']} unidades | {f'{diferenca} extras' if acima_ideal else 'Ideal'}")
            encontrado = True
    if not encontrado:
        print("❌ Nenhum medicamento encontrado nessa unidade.")


def verificar_preco_ideal(nome):
    med = estoque.get(nome.lower())
    if med:
        atual = med['preco_unidade']
        ideal = med['preco_unidade_ideal']
        diferenca = atual - ideal
        print(f"\n💲 Atual: R$ {atual:.2f} | Ideal: R$ {ideal:.2f}")
        print("✅ Dentro do ideal." if atual <= ideal else f"⚠️  Acima do ideal | Diferença: R$ {diferenca:.2f}")
    else:
        print("❌ Medicamento não encontrado.")


def calcular_valores_totais(nome):
    med = estoque.get(nome.lower())
    if med:
        total = sum(l['quantidade'] * med['preco_unidade'] for l in med['presente'].values())
        qtd_total = sum(l['quantidade'] for l in med['presente'].values())
        print(f"\n📦 Total: {qtd_total} unidades | Valor: R$ {total:.2f}")
    else:
        print("❌ Medicamento não encontrado.")


def cadastrar_medicamento(nome, tipo, usos, preco, preco_ideal):
    if nome.lower() in estoque:
        print("❌ Medicamento já existe.")
        return
    estoque[nome.lower()] = {
        "tipo": tipo,
        "caso_uso": usos,
        "preco_unidade": preco,
        "preco_unidade_ideal": preco_ideal,
        "presente": {}
    }
    print("\n✅ Medicamento cadastrado.")


def adicionar_lugar(nome, lugar, qtd, ideal):
    med = estoque.get(nome.lower())
    if med:
        med['presente'][lugar.lower()] = {"quantidade": qtd, "ideal": ideal}
        print("\n✅ Unidade adicionada.")
    else:
        print("❌ Medicamento não encontrado.")


def atualizar_quantidade(nome, lugar, nova_qtd):
    med = estoque.get(nome.lower())
    if med and lugar.lower() in med['presente']:
        med['presente'][lugar.lower()]['quantidade'] = nova_qtd
        print("\n✅ Quantidade atualizada.")
    else:
        print("❌ Informação não encontrada.")


def atualizar_ideal(nome, lugar, novo_ideal):
    med = estoque.get(nome.lower())
    if med and lugar.lower() in med['presente']:
        med['presente'][lugar.lower()]['ideal'] = novo_ideal
        print("\n✅ Valor ideal atualizado.")
    else:
        print("❌ Informação não encontrada.")


# ======================== SIMULAÇÕES ========================


def fifo_simulacao(lista):
    print("\n🔄 Simulação:")
    while lista:
        print(f"➡️  Saindo: {lista.pop(0)}")


def menu_fifo():
    fila_fifo = []

    while True:
        print("\nFIRST IN, FIRST OUT | DASA\n")
        print("[1] Adicionar medicamento")
        print("[2] Executar FIFO")
        print("[3] Listar fila")
        print("[0] Voltar")

        try:
            opcao = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("❌ Digite um número válido.")
            continue

        if opcao == 1:
            nome = input("Nome do medicamento: ").strip()
            fila_fifo.append(nome)
            print(f"\n✅ '{nome}' adicionado à fila.")
        elif opcao == 2:
            if fila_fifo:
                fifo_simulacao(fila_fifo.copy())
                fila_fifo.clear()
            else:
                print("\n⚠️  Fila vazia.")
        elif opcao == 3:
            print("\n📦 Fila atual:", fila_fifo if fila_fifo else "vazia")
        elif opcao == 0:
            break
        else:
            print("❌ Opção inválida.")


def lifo_simulacao(lista):
    print("\n🔄 Simulação:")
    while lista:
        print(f"⬅️  Saindo: {lista.pop()}")


def menu_lifo():
    pilha_lifo = []

    while True:
        print("\nLAST IN, LAST OUT | DASA\n")
        print("[1] Adicionar medicamento")
        print("[2] Executar LIFO")
        print("[3] Listar pilha")
        print("[0] Voltar")

        try:
            opcao = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("❌ Digite um número válido.")
            continue

        if opcao == 1:
            nome = input("Nome do medicamento: ").strip()
            pilha_lifo.append(nome)
            print(f"\n✅ '{nome}' adicionado à pilha.")
        elif opcao == 2:
            if pilha_lifo:
                lifo_simulacao(pilha_lifo.copy())
                pilha_lifo.clear()
            else:
                print("\n⚠️  Pilha vazia.")
        elif opcao == 3:
            print("\n📦 Pilha atual:", pilha_lifo if pilha_lifo else "vazia")
        elif opcao == 0:
            break
        else:
            print("❌ Opção inválida.")


def busca_binaria(lista, alvo):
    lista.sort()
    print("\nLista ordenada:", lista, "| Alvo:", alvo)
    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            print(f"✅ Alvo encontrado: {alvo} na posição {meio + 1}")
            return
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    print("❌ Elemento não encontrado.")


# ======================== MENU ========================


def menu():
    while True:
        print("\nCONTROLE DE ESTOQUE | DASA\n")
        print("[1] Listar medicamentos")
        print("[2] Consultar medicamento")
        print("[3] Buscar quantidade por unidade")
        print("[4] Verificar preço ideal")
        print("[5] Calcular valores totais")
        print("[6] Simulações (FIFO | LIFO | Busca binária)")
        print("[0] Sair")

        try:
            escolha = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("❌ Entrada inválida. Digite um número.")
            continue

        if escolha == 1:
            listar_medicamentos()
        elif escolha == 2:
            nome = input("Nome do medicamento: ")
            consultar_medicamento(nome)
        elif escolha == 3:
            lugar = input("Unidade: ")
            buscar_quantidade(lugar)
        elif escolha == 4:
            nome = input("Nome do medicamento: ")
            verificar_preco_ideal(nome)
        elif escolha == 5:
            nome = input("Nome do medicamento: ")
            calcular_valores_totais(nome)
        elif escolha == 6:
            try:
                print("\nSIMULAÇÕES | DASA")
                print("\n[1] FIFO\n[2] LIFO\n[3] Busca binária\n")
                tipo = int(input("Escolha a simulação: "))

                if tipo == 1:
                    menu_fifo()
                elif tipo == 2:
                    menu_lifo()
                elif tipo == 3:
                    lista = input("Digite quantidades de medicamentos separados por vírgula: ").split(',')
                    try:
                        lista = [int(x.strip()) for x in lista]
                        alvo = int(input("Número a buscar: "))
                        busca_binaria(lista, alvo)
                    except ValueError:
                        print("❌ Certifique-se de digitar apenas números inteiros.")
                else:
                    print("❌ Opção inválida. Digite 1, 2 ou 3.")
            except ValueError:
                print("❌ Escolha inválida. Digite um número inteiro.")
        elif escolha == 0:
            print("Encerrando...")
            break
        else:
            print("❌ Opção inválida.")

if __name__ == "__main__":
    menu()