# 1 passo
class Pessoa:
    # init = inicia o objeto(paramento dos atributos)
    # dentro dele coloca os atributos
    def __init__(self, nome, data_nascimento, codigo, estudando=True, trabalhando=False):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.codigo = codigo
        self.estudando = estudando
        self.trabalhando = trabalhando
        self.salario = 0

    # apresenta listagem dos atributos
    def apresentar(self):
        # primeira opção
        print(f'Nome: {self.nome}\n'
              f'Data: {self.data_nascimento}\n'
              f'Codigo: {self.codigo} ')

        if self.estudando:
            print(f'Está Estudando.')
        else:
            print(f'Não está estudando.')

        if self.trabalhando:
            print(f'Está trabalhando.')
        else:
            print(f'Não está trabalhando.')

    def estudar(self):
        if not self.estudando:
            self.estudando = True
            print(f" {self.nome} começou a estudar")

        elif self.estudando and self.trabalhando:
            self.salario += 1000
            print(
                f"{self.nome}"
                f" começou a estudar e aumentou seu salario para "
                f"R${self.salario:.2f}"
            )

        else:
            print(f"{self.nome} ja esta estudando")

    def trabalhar(self):
        if not self.trabalhando:
            self.trabalhando = True
            self.salario += 100
            print(f"{self.nome} começou a trabalhar")
        else:
            print(f" {self.nome} já está trabalhando")


# p1 = objeto do tipo pessoa
p1 = Pessoa("Lucas", "23/09/1990", "udsnv")
p1.apresentar()
p1.trabalhar()
p1.estudar()
print("-" * 20)


class Bebe(Pessoa):
    def __init__(self, nome, data_nascimento, registro):
        super().__init__(nome, data_nascimento, registro)
        self.fome = False
        self.chorando = False
        self.dormindo = False

    def apresentar(self):
        print(f'O nome do bebe é {self.nome}\n'
              f'A data de nascimento do bebe é {self.data_nascimento}\n'
              f'O número de registro  {self.codigo}\n')

        if self.fome:
            print(f'O bebe está com fome.')
        else:
            print(f'O bebe não está com fome.')

        if self.chorando:
            print(f'O bebe está chorando.')
        else:
            print(f'O bebe não está chorando.')

        if self.dormindo:
            print(f'O bebe está dormindo.')
        else:
            print(f'O bebe não está dormindo.')


    def mamar(self):
        if self.fome:
            print("O bebe está mamando")
            self.fome = False
            self.chorando = False
        else:
            print("O bebe não está com fome")


    def chorar(self):
        if self.chorando:
            print("O bebe está chorando porque está com fome")
            self.fome = True
            self.dormindo = False
        else:
            print("O bebe não está chorando")
            self.fome = False


    def dormir(self):
        if self.dormindo:
            print("O bebe já está dormindo")
        elif self.fome:
            print("O bebe não está dormindo porque está com fome")
        else:
            print("O bebe foi dormir")
            self.dormindo = True

    def acordar(self):
        if self.dormindo:
            print("O bebe está acordando")
            self.fome = True
            self.dormindo = False
        else:
            print("O bebe já esta acordado")

bebe1 = Bebe("Anna", "08/12/2023", "AKW10" )
bebe1.apresentar()
bebe1.mamar()
bebe1.dormir()
bebe1.acordar()
bebe1.acordar()
bebe1.mamar()
