class Pessoa:
    def __init__(self,nome,idade,peso, comendo = False,falando=False,dormindo=False):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.comendo=comendo
        self.falando=falando
        self.dormindo=dormindo

    def comer (self, alimento):
        if self.falando == False and self.dormindo==False:
            if self.comendo==False:
                self.comendo=True
                print(f"{self.nome} foi comer {alimento}")
            elif self.comendo==True:
                print(f"{self.nome} já está comendo")
        else:
            print(f"{self.nome} já está fazendo outra coisa e não pode comer")

    def PararDeComer(self):
        if self.comendo == True:
            comendo=False
            print(f"{self.name} parou de comer")
        else:
            print("No momento não estou comendo para parar")

    def falar (self, mensagem):
        if self.comendo==False and self.dormindo==False:
            if self.falando==False:
                self.falando=True
                print(f"{self.nome} está falando: {mensagem}")
            elif self.falando==True:
                print(f"{self.nome} já está falando")
        else:
            print(f"{self.nome} já está fazendo outra coisa e não pode falar")


    def PararDeFalar(self):
        if self.falando==True:
            self.falando=False
            print(f"{self.nome} parou de falar")
        else:
            print("No momento não estou falando para parar")

    def dormir (self, horas):
        if self.comendo==False and self.falando==False:
            if self.dormindo==False:
                self.dormindo=True
                print(f"{self.nome} dorme por {horas} horas ")
            elif self.dormindo==True:
                print(f"{self.nome} já está dormindo")
        else:
            print(f"{self.nome} já está fazendo outra coisa e não pode dormir")

    def PararDeDormir(self):
        if self.dormindo==True:
            self.dormindo=False
            print(f"{self.nome} acordou")
        else:
            print("No momento não estou dormindo para parar")

p1=Pessoa("izair",28,71)
p1.falar("eu gosto de comer")
p1.comer("maça")
p1.falar("oi oi oi ")
p1.dormir(8)
p1.PararDeComer()
p1.PararDeDormir()
p1.PararDeFalar()
p1.comer("maçã")