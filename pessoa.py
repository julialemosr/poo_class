
class Pessoa:
    def __init__(self, nome, data_nascimento, codigo, estudando=True, trabalhando=False):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__codigo = codigo
        self._estudando = estudando
        self._trabalhando = trabalhando
        self._salario = 0

    #get é uma convenção, significa pegar
    #set significa definir

    def get_nome(self):
        return self.__nome
    def get_data_nascimento(self):
        return self.__data_nascimento
    def get_codigo(self):
        return self.__codigo
    def get_salario(self):
        return self._salario


    def is_trabalhando(self):
        return self._trabalhando
    def is_estudando(self):
        return self._estudando


    def set_salario(self,salario, valor):
        if valor >= 0:
            self._salario = valor
        else:
            print("salário inválido")

    def set_estudar(self,status):
        self._estudando = status
        if status:
            self.set_salario(self.get_salario() + 400)


    def set_trabalhando(self, status):
        if self._trabalhando and status:
            print("Você está trabalhando!")
        elif not self._trabalhando and not status:
            print("Que vida boa")
        elif not self._trabalhando and status:
            self._trabalhando = status
            self.set_salario(100)
        else:
            self._trabalhando = status
            self.set_salario(0)


    def apresentar(self):
        print("+", "-" * 20, "+")
        print(f'0lá, sou {self.get_nome()} \n'
              f'meu aniversario é dia: {self.get_data_nascimento()} \n'
              f'n de reg {self.get_codigo()}')
        print(f"Estudando: {'Sim' if self.is_estudando() else 'Não'}")
        print(f"Trabalhando: {'Sim' if self.is_trabalhando() else 'Não'}")
        if self.is_trabalhando():
            print(f"Salario: R$ {self.get_salario():.2f}")
        print("+", "-" * 20, "+")
        print("\n")

    def estudar(self):
        if not self._estudando:
            self._estudando = True
            print(f" {self.__nome} começou a estudar")

        elif self._estudando and self._trabalhando:
            self._salario += 1000
            print(
                f"{self.__nome}"
                f" começou a estudar e aumentou seu salario para "
                f"R${self._salario:.2f}"
            )

        else:
            print(f"{self.__nome} ja esta estudando")

    def trabalhar(self):
        if not self._trabalhando:
            self._trabalhando = True
            self._salario += 100
            print(f"{self.__nome} começou a trabalhar")
        else:
            print(f" {self.__nome} já está trabalhando")


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
        print(f'O nome do bebe é {self.__nome}\n'
              f'A data de nascimento do bebe é {self.__data_nascimento}\n'
              f'O número de registro  {self.__codigo}\n')

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

bebe1.mamar()
bebe1.dormir()
bebe1.acordar()
bebe1.acordar()
bebe1.mamar()
