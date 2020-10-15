class Animal:
    atrb_animal = 0

    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome + " eh um animal "

    def comer(self):
        print(self.nome + ", que eh um animal, esta comendo.")


class Mamifero (Animal):
    def __str__(self):
        return (self.nome + " eh um mamifero ")

    def beber_leite(self):
        print(self.nome + ", que eh um mamifero, esta bebendo leite.")


class Cao (Mamifero):
    def __str__(self):
        return self.nome + " eh um cachorro "

    def latir(self):
        print(self.nome + " esta latindo bem auto.")

    def comer(self):
        print(self.nome + " late quando come.")
        self.latir()


def test():
    a1 = Animal(" Tigrinho")
    a2 = Mamifero(" Oncinha")
    a3 = Cao(" Mameluco")
    print(a1) # 1: Sera impresso "Tigrinho eh um animal"
    print(a2) # 2: Sera impresso "Oncinha eh um mamifero"
    print(a3) # 3: Sera impresso "Mameluco eh um cachorro"
    a1.comer() # 4: Sera impresso "Tigrinho, que eh um animal, esta comendo."
    a2.beber_leite() # 5: Sera impresso "Oncinha, que eh um mamifero, esta bebendo leite."
    a2.comer() # 6: Sera impresso "Oncinha, que eh um animal, esta comendo."
    a3.latir() # 7: Sera impresso "Mameluco esta latindo bem auto."
    a3.beber_leite() # 8: Sera impresso "Mameluco, que eh um mamifero, esta bebendo leite."
    a3.comer() # 9: Sera impresso "Mameluco late quando come. Mameluco esta latindo bem auto."
    a1.beber_leite() # 10: Um erro sera produzido em tempo de execucao
    a1 = a3
    a1.latir() # 11: Sera impresso "Mameluco esta latindo bem auto."
