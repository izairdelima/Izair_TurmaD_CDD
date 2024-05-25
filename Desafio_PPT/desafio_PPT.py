class PedraPapelTesoura:
    def __init__(self, jogador1, jogador2):
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.jogada1 = ""
        self.jogada2 = ""

    def resultado(self):

        decisao = 1
        rodadas = 1
        vitoria1 = 0
        vitoria2 = 0

        while decisao == 1:

            while rodadas != 4:

                if vitoria1 == 3 or vitoria2 == 3:
                    break

                print(f"Inicio da {rodadas}º rodada:")

                jogadaDoJogador1 = input(f"Qual é a sua Jogada {self.jogador1}?").lower()
                while jogadaDoJogador1 not in ["pedra", "papel", "tesoura"]:
                    jogadaDoJogador1 = input("Jogada inválida. Escreva Pedra, Papel e Tesoura: ").lower()

                jogadaDoJogador2 = input(f"Qual é a sua jogada {self.jogador2}?").lower()
                while jogadaDoJogador2 not in ["pedra", "papel", "tesoura"]:
                    jogadaDoJogador2 = input("Jogada inválida. Escreva Pedra, Papel e Tesoura: ").lower()

                if jogadaDoJogador1 == jogadaDoJogador2:
                    print(f"Empate")
                    print(f"{self.jogador1} - {vitoria1} X {vitoria2} - {self.jogador2}")

                elif jogadaDoJogador1 == "papel" and jogadaDoJogador2 == "pedra":
                    vitoria1 += 1
                    print(f"Jogador \n{self.jogador1} venceu a rodada")
                    print(f"{self.jogador1} - {vitoria1} X {vitoria2} - {self.jogador2}")

                elif jogadaDoJogador1 == "pedra" and jogadaDoJogador2 == "tesoura":
                    vitoria1 += 1
                    print(f"Jogador \n{self.jogador1} venceu a rodada")
                    print(f"{self.jogador1} - {vitoria1} X {vitoria2} - {self.jogador2}")

                elif jogadaDoJogador1 == "tesoura" and jogadaDoJogador2 == "papel":
                    vitoria1 += 1
                    print(f"Jogador \n{self.jogador1} venceu a rodada")
                    print(f"{self.jogador1} - {vitoria1} X {vitoria2} - {self.jogador2}")

                else:
                    vitoria2+=1
                    print(f"Jogador \n{self.jogador2} venceu a rodada")
                    print(f"{self.jogador1} - {vitoria1} X {vitoria2} - {self.jogador2}")

                rodadas += 1

            else:
                if vitoria1 > vitoria2:
                    print(f"{self.jogador1} É o melhor de 3")

                elif vitoria2 > vitoria1:
                    print(f"{self.jogador2} É o melhor de 3")

                else:
                    print("Empate no Jogo")

            decisao = int(input("Jogar novamente: 1- Sim 2-Não: "))

            while decisao <= 0 or decisao > 2:
                decisao = int(input("Escolha: 1- Sim 2-Não: "))

            if decisao == 1:
                vitoria1 = 0
                vitoria2 = 0
                rodadas = 1
            else:
                print("Saindo")