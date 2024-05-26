class JogoDaVelha():
    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.escolhaDoJogador1 = "X"
        self.escolhaDoJogador2 = "O"

    def resultado(self):
        matriz = [
            ["1", "2", "3"],
            ["4", "5", "6"],
            ["7", "8", "9"]
        ]

        listaDeJogada = []
        rodadas = 1
        vitoriaDoJogador1 = 0
        vitoriaDoJogador2 = 0

        print(f"{self.jogador1} = X \n{self.jogador2} = O")
        for x in range(0, 3):
            for y in range(0, 3):
                print(matriz[x][y], end="")
            print()

        while rodadas <=3:

            if vitoriaDoJogador1 == 2:
                print(f"Vitoria do {self.jogador1}")
                break
            elif vitoriaDoJogador2 == 2:
                print(f"Vitoria do {self.jogador2}")
                break

            print(f"Inicio da {rodadas} Rodada:")
            rodadas +=1

            for rodada in range(9):

            # Jogador 1
                jogadaDoJogador1 = input(f"Escolha entre 1 e 9 \nQual é a sua jogada {self.jogador1}: ")

                while jogadaDoJogador1 in listaDeJogada:
                    jogadaDoJogador1 = input(f"Essa jogada já foi escolhida. \nQual é a sua jogada {self.jogador1}: ")

                while jogadaDoJogador1 not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                        jogadaDoJogador1 = input(f"Jogada inválida, tente novamente. \nQual é a sua jogada {self.jogador1}: ")

                listaDeJogada.append(jogadaDoJogador1)
                print(listaDeJogada)

                #Posição da jogada do jogador 01

                if jogadaDoJogador1 == "1":
                    matriz[0][0] = self.escolhaDoJogador1
                elif jogadaDoJogador1 == "2":
                    matriz[0][1] = self.escolhaDoJogador1
                elif jogadaDoJogador1 == "3":
                    matriz[0][2] = self.escolhaDoJogador1
                elif jogadaDoJogador1 == "4":
                    matriz[1][0] = self.escolhaDoJogador1
                elif jogadaDoJogador1 == "5":
                    matriz[1][1] = self.escolhaDoJogador1
                elif jogadaDoJogador1 == "6":
                    matriz[1][2] = self.escolhaDoJogador1
                elif jogadaDoJogador1 == "7":
                    matriz[2][0] = self.escolhaDoJogador1
                elif jogadaDoJogador1 == "8":
                    matriz[2][1] = self.escolhaDoJogador1
                elif jogadaDoJogador1 == "9":
                    matriz[2][2] = self.escolhaDoJogador1

                # Verificar se o jogador 1 venceu
                if rodada >= 2:
                    if (matriz[0][0] == "X" and matriz[0][1] == "X" and matriz[0][2] == "X") \
                        or (matriz[1][0] == "X" and matriz[1][1] == "X" and matriz[1][2] == "X") \
                        or (matriz[2][0] == "X" and matriz[2][1] == "X" and matriz[2][2] == "X") \
                        or (matriz[0][0] == "X" and matriz[1][0] == "X" and matriz[2][0] == "X") \
                        or (matriz[0][1] == "X" and matriz[1][1] == "X" and matriz[2][1] == "X") \
                        or (matriz[0][2] == "X" and matriz[1][2] == "X" and matriz[2][2] == "X") \
                        or (matriz[0][0] == "X" and matriz[1][1] == "X" and matriz[2][2] == "X") \
                        or (matriz[0][2] == "X" and matriz[1][1] == "X" and matriz[2][0] == "X"):

                            print(f"{self.jogador1} Venceu")
                            vitoriaDoJogador1 += 1
                            print(f"{self.jogador1} - {vitoriaDoJogador1} X {vitoriaDoJogador2} - {self.jogador2}")
                            matriz = [
                                ["1", "2", "3"],
                                ["4", "5", "6"],
                                ["7", "8", "9"]
                            ]

                            listaDeJogada = []

                            for x in range(0, 3):
                                for y in range(0, 3):
                                    print(matriz[x][y], end="")
                                print()
                            print()
                            break
                elif rodada == 9:
                    print("Empate")

                for x in range(0, 3):
                    for y in range(0, 3):
                        print(matriz[x][y], end="")
                    print()

                # Jogador 2

                jogadaDoJogador2 = input(f"Qual é a sua jogada {self.jogador2}: ")

                while jogadaDoJogador2 in listaDeJogada:
                    jogadaDoJogador2 = input(f"Essa jogada já foi escolhida. \nQual é a sua jogada {self.jogador2}: ")

                while jogadaDoJogador2 not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    jogadaDoJogador2 = input(f"Jogada inválida, tente novamente. \nQual é a sua jogada {self.jogador2}: ")

                listaDeJogada.append(jogadaDoJogador2)
                print(listaDeJogada)

                # Posição da jogada do jogador 02

                if jogadaDoJogador2 == "1":
                    matriz[0][0] = self.escolhaDoJogador2
                elif jogadaDoJogador2 == "2":
                    matriz[0][1] = self.escolhaDoJogador2
                elif jogadaDoJogador2 == "3":
                    matriz[0][2] = self.escolhaDoJogador2
                elif jogadaDoJogador2 == "4":
                    matriz[1][0] = self.escolhaDoJogador2
                elif jogadaDoJogador2 == "5":
                    matriz[1][1] = self.escolhaDoJogador2
                elif jogadaDoJogador2 == "6":
                    matriz[1][2] = self.escolhaDoJogador2
                elif jogadaDoJogador2 == "7":
                    matriz[2][0] = self.escolhaDoJogador2
                elif jogadaDoJogador2 == "8":
                    matriz[2][1] = self.escolhaDoJogador2
                elif jogadaDoJogador2 == "9":
                    matriz[2][2] = self.escolhaDoJogador2

                # Verificar se o jogador 2 venceu

                if rodada >= 2:
                    if (matriz[0][0] == "O" and matriz[0][1] == "O" and matriz[0][2] == "O") \
                        or (matriz[1][0] == "O" and matriz[1][1] == "O" and matriz[1][2] == "O") \
                        or (matriz[2][0] == "O" and matriz[2][1] == "O" and matriz[2][2] == "O") \
                        or (matriz[0][0] == "O" and matriz[1][0] == "O" and matriz[2][0] == "O") \
                        or (matriz[0][1] == "O" and matriz[1][1] == "O" and matriz[2][1] == "O") \
                        or (matriz[0][2] == "O" and matriz[1][2] == "O" and matriz[2][2] == "O") \
                        or (matriz[0][0] == "O" and matriz[1][1] == "O" and matriz[2][2] == "O") \
                        or (matriz[0][2] == "O" and matriz[1][1] == "O" and matriz[2][0] == "O"):
                        print(f"{self.jogador2} Venceu")
                        vitoriaDoJogador2 += 1
                        print(f"{self.jogador1} - {vitoriaDoJogador1} X {vitoriaDoJogador2} - {self.jogador2}")

                        matriz = [
                            ["1", "2", "3"],
                            ["4", "5", "6"],
                            ["7", "8", "9"]
                        ]

                        listaDeJogada = []

                        for x in range(0, 3):
                            for y in range(0, 3):
                                print(matriz[x][y], end="")
                            print()
                        print()
                        break

                elif rodada == 9:
                    print("Empate")

                for x in range(0, 3):
                    for y in range(0, 3):
                        print(matriz[x][y], end="")
                    print()
        else:
            if vitoriaDoJogador1 < vitoriaDoJogador2:
                print(f"Vitoria do {jogadaDoJogador2}")
            elif vitoriaDoJogador1 > vitoriaDoJogador2:
                print(f"Vitoria do {jogadaDoJogador1}")
            elif vitoriaDoJogador1 == vitoriaDoJogador2:
                print(f"Jogo encerrado em empate")