class Animal:

    def __init__(self,nome, especie, peso, tamanho, agua_doce=False, agua_salgada=True):
        self.nome = nome
        self.especie = especie
        self.peso = peso
        self.tamanho = tamanho
        self.agua_doce = agua_doce
        self.agua_salgada = agua_salgada

    def apresentar(self):

        print(f'Nome do animal: {self.nome}\n'
              f'Espécie do animal: {self.especie}\n'
              f'Peso do animal: {self.peso}\n'
              f'Tamanho do animal: {self.tamanho} ')

        if self.agua_doce:
            print(f'O animal é de água doce')
            self.agua_doce = True
        else:
            self.agua_doce = False
            print("O animal não é de água doce")

        if self.agua_salgada:
            print("O animal é de água salgada")
            self.agua_salgada = True
        else:
            self.agua_salgada = False
            print("O animal não é de água salgada")


    def agua_doce(self):
        if not self.agua_doce:
            self.agua_doce = True
            print(f"O animal {self.nome} é de água doce")
        else:
            print(f"O animal {self.nome} é de água salgada")

    def agua_salgada(self):
        if not self.agua_salgada:
            self.agua_salgada = True
            print(f"O animal {self.nome} é de água salgada")
        else:
            print(f"O animal {self.nome} é de água doce")

p1 = Animal("Bob", "Carpa", "15kg", "25cm")
p1.apresentar()
print("-" * 20)

class Peixe(Animal):
    def __init__(self, nome, especie, peso, tamanho):
        super().__init__(nome, especie, peso, tamanho)
        self.fome = True
        self.cacando = True
        self.dormindo = False

    def apresentar(self):
        print(f'O nome do peixe é {self.nome}\n'
              f'A espécie do peixe é {self.especie}\n'
              f'O peso do peixe é {self.peso}\n'
              f'O tamanho do peixe é{self.tamanho}\n')

        if self.dormindo:
            print(f'O peixe está dormindo.')
        else:
            print(f'O peixe está acordado.')

        if self.fome:
            print(f'O peixe está com fome.')
        else:
            print(f'O peixe não está com fome.')

        if self.cacando:
            print(f'O peixe está caçando.')
        else:
            print(f'O peixe não está caçando.')

    def comer(self):
        if self.fome:
            print("O peixe está comendo")
            self.fome = False
            self.cacando = False
        else:
            print("O peixe não está com fome")

    def cacando(self):
        if self.cacando:
            print("O peixe está caçando porque está com fome")
            self.fome = True
            self.dormindo = False
        else:
            print("O bebe não está caçando")
            self.fome = False

    def dormir(self):
        if self.dormindo:
            print("O peixe já está dormindo")
        elif self.fome:
            print("O peixe não está dormindo porque está com fome")
        else:
            print("O peixe foi dormir")
            self.dormindo = True

    def acordar(self):
        if self.dormindo:
            print("O peixe está acordando")
            self.fome = True
            self.dormindo = False
        else:
            print("O peixe já esta acordado")


peixe1 = Peixe("Nemo", "dourado", "90g", " 4cm")
peixe1.apresentar()
peixe1.comer()
peixe1.dormir()
peixe1.acordar()
peixe1.dormir()
print("-" * 20)