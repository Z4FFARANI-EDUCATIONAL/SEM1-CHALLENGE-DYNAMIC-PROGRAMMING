![banner](./assets/banner.png)

# INTEGRANTES:
- **[Guilherme Santos Nunes](https://github.com/sannunez)**
- **[Kaique Zaffarani](https://github.com/Z4ffarani)**
- **[Kairo da Silva Silvestre de Carvalho](https://github.com/KairoSilvestre)**
- **[Pedro Josué Pereira Almeida](https://github.com/Pedro-Josue)**
- **[Rafael Menezes Viana](https://github.com/vianafs)**

<br>

# PROJETO
A **[FIAP](https://www.fiap.com.br)**, com o objetivo de auxiliar a rede de saúde integrada **[DASA](https://dasa.com.br)** na distribuição eficiente de estoques – entre outros processos internos – incentivou a criação de um sistema de controle de estoques de medicamentos.

O projeto permite consultar, cadastrar e gerenciar dados como preços, locais de armazenamento, estoques ideais e simulações logísticas de movimentação de itens com base nos métodos FIFO (First in, first out), LIFO (Last in, first out), e busca binária.

A ferramenta visa apoiar decisões sobre compras, redistribuições e balanceamento de estoque entre unidades de saúde. O sistema é operado via terminal e utiliza um arquivo `JSON` para armazenamento dinâmico dos dados.

<br>

# INSTRUÇÕES
1. Em um terminal, clonar o repositório:
```bash
git clone https://github.com/Z4FFARANI-EDUCATIONAL/SEM1-CHALLENGE-DYNAMIC-PROGRAMMING
```

2. No terminal, navegar até a pasta do projeto:
```bash
cd SEM1-CHALLENGE-DYNAMIC-PROGRAMMING
```

3. No terminal, executar o arquivo `controle_estoque.py` acessará as funcionalidades.
   
4. O programa permite visualizar medicamentos disponíveis, consultar dados por nome, unidade ou tipo, além de realizar cadastros e atualizações em tempo real.

5. Simulações com FIFO, LIFO, e busca binária podem ser acessadas em respectivos menus após opção de simulação, demonstrando tanto ordem de retirada, quanto busca de quantidade de medicamentos.

<br>

# FUNÇÕES
`controle_estoque.py`:
- `listar_medicamentos()` | Percorre todas as chaves do arquivo `estoque.json` e imprime uma lista.

- `consultar_medicamento(nome)` | Verifica se o nome está registrado em `estoque.json`. Se sim, imprime todo o dicionário interno com dados do medicamento (tipo, usos, preços, locais etc.). Se não, exibe uma mensagem de erro.

- `buscar_quantidade(lugar)` | Itera por todos os medicamentos. Para cada um, verifica se `lugar` existe nas unidades registradas. Se sim, extrai a quantidade atual e o ideal e imprime no formato `nome: qtd/ideal`.

- `verificar_preco_ideal(nome)` | Verifica se o medicamento existe. Compara `preco` e `preco_ideal`. Retorna a avaliação textual conforme o resultado da comparação.

- `calcular_valores_totais(nome)` | Verifica existência. Soma todas as quantidades de todas as unidades. Multiplica pelo `preco` do medicamento. Exibe total de unidades e valor total.

- `cadastrar_medicamento(nome, tipo, usos, preco, preco_ideal)` | Cria ou sobrescreve uma nova entrada no arquivo `estoque.json`. Estrutura interna: informações fixas + subdicionário `unidades` inicialmente vazio.

- `adicionar_lugar(nome, lugar, qtd, ideal)` | Acessa um medicamento existente. Adiciona/atualiza uma chave de unidade `lugar` com valores de `quantidade` e `ideal`.

- `atualizar_quantidade(nome, lugar, nova_qtd)` | Garante que o medicamento e o local existem. Substitui a quantidade atual pela nova informada.

- `atualizar_ideal(nome, lugar, novo_ideal)` | Mesmo processo da função anterior, mas atualiza o valor ideal da unidade.

- `fifo_simulacao(lista)` | Recebe uma lista (simulando entradas em ordem). Remove o primeiro elemento com `pop(0)`. Imprime o item removido até a lista esvaziar.

- `menu_fifo()` | Menu em loop para manipular a lista FIFO. Adiciona itens no final da lista. Remove do início (`pop(0)`). Sai com a opção `[3]`.

- `lifo_simulacao(lista)` | Mesma lógica da FIFO, mas remove o último item inserido (`pop()`).

- `menu_lifo()` | Interface interativa similar ao `menu_fifo()`, mas segue a lógica de pilha (último a entrar é o primeiro a sair).

- `busca_binaria(lista, alvo)` | Recebe uma lista ordenada numericamente e um valor `alvo`. Usa os ponteiros `inicio` e `fim` para buscar o meio iterativamente. Retorna o índice do valor ou `-1` se não encontrado.

<br>

# OBSERVAÇÕES
- Os dados presentes no arquivo `estoque.json` são generalizados, não condizem com a real distribuição de medicamentos e não são manipuladas externamente do sistema.
- A estrutura do dicionário presente em `estoque.json` pode ser expandida para incluir mais dados relevantes.
- O projeto pode ser adaptado facilmente para integrar com sistemas maiores ou interfaces gráficas.
- Cada execução de código do projeto é única (sem salvamento), sendo apenas operada via terminal, com feedback imediato ao usuário.

<br>

# TECNOLOGIAS
**[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/downloads/)**

<br>

# REFERÊNCIAS
- **[Exemplo com título exatamente igual]()**
