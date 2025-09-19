# Blackjack (CLI) em Python

Implementação simples do jogo Blackjack para rodar no terminal.
O jogador compete contra o computador (dealer). O baralho é modelado por valores inteiros e o Ás vale 11 (ou 1 quando necessário). Há detecção de Blackjack logo na mão inicial.

Projeto didático para praticar controle de fluxo, funções e listas.

✨ Recursos

Compra de cartas aleatórias (random.choice)

Regra do Ás flexível (11 → 1 se estourar)

Detecção de Blackjack (Ás + 10 nas 2 primeiras cartas)

Dealer compra até 17 pontos

Mensagens claras de resultado (ganhou, perdeu, empate)



🚀 Como executar

Pré-requisito: Python 3.9+

python blackjack.py

🕹️ Exemplo de execução
Suas cartas: [10, 9], pontuação atual: 19
Cartas do computador: 11
Escreva 's' para obter nova carta e 'n' para passar: n
Sua mão: [10, 9], score final: 19
Mão do computador: [11, 6, 10], score final: 27
Oponente perdeu

🔎 Regras implementadas

Blackjack: Ás (11) + carta de valor 10 nas duas primeiras cartas → é representado como score = 0 internamente.

Ás ajustável: se a soma passar de 21 e houver Ás valendo 11, ele passa a valer 1.

Dealer: compra até chegar em 17 ou mais (a não ser que tenha Blackjack).

Resultado: vitória, derrota, empate, e mensagens específicas para Blackjack/estouro.
