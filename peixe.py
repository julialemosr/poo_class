class Animal_aquatico:
    def __init__(self, nome, especie, peso, tamanho, agua_doce=False, agua_salgada=True):
        self.__nome = nome
        self.__especie = especie
        self.__peso = peso
        self.__tamanho = tamanho
        self._agua_doce = agua_doce
        self._agua_salgada = agua_salgada

    def get_nome(self):
        return self.__nome

    def get_especie(self):
        return self.__especie

    def get_peso(self):
        return self.__peso

    def get_tamanho(self):
        return self.__tamanho

    def is_agua_salgada(self):
        return self._agua_salgada

    def is_agua_doce(self):
        return self._agua_doce

    def set_agua_salgada(self, status):
        if self._agua_salgada and status:
            print("O animal já está na água salgada.")
        elif not self._agua_salgada and status:
            print("O animal vai para a água salgada.")
        elif self._agua_salgada and not status:
            self._agua_salgada = status
            print("O animal não deve estar na água salgada.")
        else:
            print("O animal nunca esteve em água salgada.")

    def set_agua_doce(self, status):
        if self._agua_doce and status:
            print("Ele já está na água doce.")
        elif not self._agua_doce and status:
            print("O animal vai para a água doce.")
        elif self._agua_doce and not status:
            self._agua_doce = status
            print("O animal não deve estar na água doce.")
        else:
            print("O animal nunca esteve na água doce.")

    def apresentar(self):
        print("+", "-" * 20, "+")
        print(f'O nome do animal é: {self.get_nome()} \n'
              f'A espécie do animal é: {self.get_especie()} \n'
              f'O peso do animal é: {self.get_peso()} \n'
              f'O tamanho do animal é: {self.get_tamanho()} \n')
        print(
            f"água salgada: {'Sim, o animal está na água salgada.' if self.is_agua_salgada() else 'O animal não está na água salgada.'}")
        print(
            f"água doce: {'Sim, o animal está na água doce.' if self.is_agua_doce() else 'O animal não está na água doce.'}")
        print("\n")

    def agua_doce(self):
        if not self._agua_doce:
            self._agua_doce = True
            print(f"O animal {self.__nome} é de água doce")
        else:
            print(f"O animal {self.__nome} é de água salgada")

    def agua_salgada(self):
        if not self._agua_salgada:
            self._agua_salgada = True
            print(f"O animal {self.__nome} é de água salgada")
        else:
            print(f"O animal {self.__nome} é de água doce")


p1 = Animal_aquatico("Bob", "Carpa", "15kg", "25cm")
p1.apresentar()
print("-" * 20)


class Peixe(Animal_aquatico):

    def __init__(self, nome, especie, peso, tamanho):
        super().__init__(nome, especie, peso, tamanho)
        self.fome = True
        self.cacando = True
        self.dormindo = False

    def apresentar(self):
        print(f'O nome do peixe é {self.__nome}\n'
              f'A espécie do peixe é {self.__especie}\n'
              f'O peso do peixe é {self.__peso}\n'
              f'O tamanho do peixe é{self.__tamanho}\n')

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

    def cacar(self):
        if self.cacando:
            self.fome = True
            self.dormindo = False
            print("O peixe está caçando porque está com fome")
        else:
            self.fome = False
            print("O peixe não está caçando")

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
peixe1.acordar()
peixe1.cacar()
peixe1.comer()
peixe1.dormir()
peixe1.acordar()
peixe1.dormir()
print("-" * 20)
