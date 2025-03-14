class Cachorro:
    def __init__(self, nome, raça, comida):
        self.nome = nome
        self.raça = raça
        self.comida = comida
        self.feliz = False
        self.acordado = False

    def acordar (self):
        self.acordado = True
        print(f"{self.nome} está acordado!") 

    def dormir (self):
        self.acordado = False
        print(f"{self.nome} está dormindo!") 
        

    def comer (self):
        if self.acordado:
            self.comida -= 1
            print(f"{self.nome}comeu!") 
        else:
            print(f"{self.nome} está dormindo e não pode comer!") 

        
    def latir (self):
        if self.acordado:
            print(f"{self.nome}está latindo: AU AU AU")
        else:
            print(f"{self.nome}está dormindo e não está latindo") 

    def brincar (self):
        self.feliz = True
        print(f"{self.nome}está brincando e está feliz")

cachorro1 = Cachorro("lisboa", "versinha", 6)
cachorro1.brincar()
cachorro1.comer()
cachorro1.acordar()
cachorro1.dormir()