def move(piece, board, player):
    col = int(input(f"Sua vez jogador {player}, insira uma coluna de 1 a 7: ")) # Solicita ao jogador a coluna onde deseja fazer a jogada
    for i in range(5, -1, -1): # Percorre as linhas do tabuleiro de baixo para cima
        if board[i][col-1] == 0: # Verifica se a posição está vazia
            board[i][col-1] = piece # Faz a jogada na posição escolhida
            return True
    if checkWin(piece, board, player): # Verifica se houve uma vitória após a jogada
        return True
    return False

def printBoard(board):
    while True: # Loop infinito para exibir o tabuleiro e processar as jogadas
        for a in board: # Percorre as linhas do tabuleiro
            for termo in a: # Percorre os termos de cada linha do tabuleiro
                if termo == 0 or termo == "X" or termo == "Y": # Verifica se é uma posição vazia ou contém uma peça dos jogadores
                    move("X", board, "1") # Faz a jogada do jogador 1
                    for linha in board: # Exibe o tabuleiro atualizado após a jogada
                        for termo in linha:
                            print(termo, end=" ")
                        print()
                    if checkWin("X", board, "1"): # Verifica se o jogador 1 venceu após a jogada
                        return # Encerra o loop quando checkWin retorna True
                    if checkTie(board): # Verifica se o jogo empatou após a jogada
                        return # Encerra o loop quando checkTie retorna True
                    move("Y", board, "2") # Faz a jogada do jogador 2
                    for linha in board: # Exibe o tabuleiro atualizado após a jogada
                        for termo in linha:
                            print(termo, end=" ")
                        print()
                    if checkWin("Y", board, "2"): # Verifica se o jogador 2 venceu após a jogada
                        return # Encerra o loop quando checkWin retorna True
                    if checkTie(board): # Verifica se o jogo empatou após a jogada
                        return # Encerra o loop quando checkTie retorna True

def checkWin(piece, board, player):
    # Verifica vitória na horizontal
    for seq in board:
        for i in range(4):
            if seq[i] == piece and seq[i + 1] == piece and seq[i + 2] == piece and seq[i + 3] == piece:
                print("Parabéns, {}! Você venceu!".format(player)) # Exibe mensagem de vitória do jogador
                return True

    # Verifica vitória na vertical
    for col in range(7):
        for i in range(3):
            if board[i][col] == piece and board[i + 1][col] == piece and board[i + 2][col] == piece and \
                    board[i + 3][col] == piece:
                print("Parabéns, {}! Você venceu!".format(player)) # Exibe mensagem de vitória do jogador
                return True

    # Verifica vitória na diagonal (direção descendente)
    for seq in range(3):  # Loop para percorrer as sequências de 3 a 0
        for col in range(4):  # Loop para percorrer as colunas de 0 a 3
            if board[seq][col] == piece and board[seq + 1][col + 1] == piece and board[seq + 2][col + 2] == piece and \
                    board[seq + 3][col + 3] == piece:  # Verifica se há 4 peças iguais em sequência descendente
                print("Parabéns, {}! Você venceu!".format(player))  # Exibe mensagem de vitória com nome do jogador
                return True  # Retorna True indicando vitória

        # Verifica vitória na diagonal (direção ascendente)
    for seq in range(3, 6):  # Loop para percorrer as sequências de 3 a 6
        for col in range(4):  # Loop para percorrer as colunas de 0 a 3
            if board[seq][col] == piece and board[seq - 1][col + 1] == piece and board[seq - 2][col + 2] == piece and \
                    board[seq - 3][col + 3] == piece:  # Verifica se há 4 peças iguais em sequência ascendente
                print("Parabéns, {}! Você venceu!".format(player))  # Exibe mensagem de vitória com nome do jogador
                return True  # Retorna True indicando vitória

    return False  # Retorna False indicando que não houve vitória na diagonal


def checkTie(board):
    # Verifica se ainda há espaços vazios no tabuleiro
    for linha in board:
        if 0 in linha:  # Verifica se há algum espaço vazio (valor 0) na linha
            return False  # Retorna False indicando que ainda não houve empate
    print("Empate! O jogo terminou empatado!")  # Exibe mensagem de empate
    return True  # Retorna True indicando que houve empate


def main():
    board = [[0, 0, 0, 0, 0, 0, 0],  # Inicializa o tabuleiro com valores padrão (0)
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0]]
    printBoard(board)  # Chama função para exibir o tabuleiro


main()  # Chama função principal do jogo
