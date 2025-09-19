# Blackjack - Jogo simples em Python
# O objetivo é simular uma partida de Blackjack entre o jogador e o computador.

import random  # Biblioteca usada para gerar escolhas aleatórias (como puxar cartas do baralho).

# ---------------- FUNÇÃO: Puxar uma carta ----------------
def deal_card():
    # Lista de valores possíveis das cartas no Blackjack:
    # O Ás é representado por 11 (mas pode valer 1, dependendo da situação),
    # As cartas de 2 a 10 valem seu número,
    # Valete, Dama e Rei valem 10.
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    # Sorteia uma carta aleatória da lista
    card = random.choice(cards)
    return card


# ---------------- FUNÇÃO: Calcular a pontuação ----------------
def calculate_scores(cards):
    # Caso especial: Blackjack (Ás + 10) logo no início (2 cartas) → pontuação é marcada como 0
    # Usamos "0" como valor especial para identificar Blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Ajuste do Ás: se o jogador estourar (>21) e tiver um Ás valendo 11,
    # esse Ás passa a valer 1 para não ultrapassar 21.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    # Retorna a soma final das cartas
    return sum(cards)


# ---------------- FUNÇÃO: Comparar resultados ----------------
def compare(seu_score, pc_score):
    # Empate se os dois tiverem a mesma pontuação
    if seu_score == pc_score:
        return "Empate"
    # O computador fez Blackjack
    elif pc_score == 0:
        return "Perdeu, o oponente tem Blackjack"
    # O jogador fez Blackjack
    elif seu_score == 0:
        return "Ganhou, você tem Blackjack"
    # O jogador estourou (acima de 21)
    elif seu_score > 21:
        return "Você perdeu"
    # O computador estourou
    elif pc_score > 21:
        return "Oponente perdeu"
    # Vitória do jogador por ter pontuação maior
    elif seu_score > pc_score:
        return "Você ganhou"
    # Caso contrário, o jogador perde
    else:
        return "Você perdeu"


# ---------------- FUNÇÃO: Jogar o jogo ----------------
def play_game():
    # Listas para armazenar as cartas de cada jogador
    user_cards = []
    computer_cards = []

    # Flag para indicar se o jogo acabou
    is_game_over = False

    # Inicialização das pontuações (serão recalculadas depois)
    computer_score = -1
    user_score = -1

    # Cada jogador recebe 2 cartas no início
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Loop principal do jogo (enquanto não terminar)
    while not is_game_over:
        # Calcula as pontuações atuais
        user_score = calculate_scores(user_cards)
        computer_score = calculate_scores(computer_cards)

        # Mostra ao jogador suas cartas e a primeira carta do computador
        print(f"Suas cartas: {user_cards}, pontuação atual: {user_score}")
        print(f"Cartas do computador: {computer_cards[0]}")

        # Condições de parada imediata (Blackjack ou estouro)
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Pergunta ao jogador se quer outra carta
            user_should_deal = input("Escreva 's' para obter uma nova carta e 'n' para passar: ")
            if user_should_deal == "s":
                # Se escolher sim, adiciona nova carta
                user_cards.append(deal_card())
            else:
                # Se escolher não, encerra sua jogada
                is_game_over = True

    # Regras do computador: ele compra cartas até ter pelo menos 17 pontos,
    # exceto se já tiver Blackjack (0)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_scores(computer_cards)

    # Mostra resultado final
    print(f"Sua mão de cartas é: {user_cards}, e o seu score final: {user_score}")
    print(f"Mão de cartas do computador é: {computer_cards}, e o seu score final: {computer_score}")

    # Chama a função de comparação e mostra o resultado do jogo
    print(compare(user_score, computer_score))
