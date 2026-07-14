class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def latir(self):
        return f"{self.nome} diz: Au au!"

meu_dog = Cachorro("Rex", "Labrador")

print(meu_dog.nome)
print(meu_dog.latir())