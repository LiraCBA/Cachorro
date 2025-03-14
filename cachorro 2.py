class Cachorro:
    def __init__(self, nome, raça, comida):
        self.nome = nome
        self.raça = raça
        self.comida = comida
        self.feliz = False
        self.acordado = False
        self.energia = 100  # Atributo energia, inicializado com 100

    def acordar(self):
        self.acordado = True
        print(f"{self.nome} está acordado!") 

    def dormir(self):
        self.acordado = False
        self.energia = 100  # Restaura a energia para 100 ao dormir
        print(f"{self.nome} está dormindo! Energia restaurada para 100.")

    def comer(self):
        if self.acordado:
            self.comida -= 1
            print(f"{self.nome} comeu! Restam {self.comida} porções de comida.")
        else:
            print(f"{self.nome} está dormindo e não pode comer!") 

    def latir(self):
        if self.acordado:
            print(f"{self.nome} está latindo: AU AU AU")
        else:
            print(f"{self.nome} está dormindo e não está latindo")

    def brincar(self):
        if self.energia >= 20:  # Só pode brincar se tiver pelo menos 20 de energia
            self.energia -= 20  # Reduz 20 pontos de energia ao brincar
            self.feliz = True
            print(f"{self.nome} está brincando e está feliz! Energia restante: {self.energia}")
        else:
            print(f"{self.nome} não tem energia suficiente para brincar!")

    def exercitar(self):
        if self.energia >= 20:  # Exige mais energia para o exercício
            self.energia -= 20  # Reduz 20 pontos de energia ao se exercitar
            self.feliz = True
            print(f"{self.nome} está se exercitando e ficou ainda mais feliz! Energia restante: {self.energia}")
        else:
            print(f"{self.nome} não tem energia suficiente para se exercitar!")

# Exemplo de uso com o nome "LanderVelha"
cachorro1 = Cachorro("LanderVelha", "Versinha", 6)

# O cachorro tenta se exercitar
cachorro1.acordar()  # O cachorro acorda
cachorro1.exercitar()  # O cachorro se exercita e gasta 30 de energia

# O cachorro tenta brincar após o exercício
cachorro1.brincar()   # O cachorro pode brincar com energia suficiente

# O cachorro tenta se exercitar novamente, mas não tem energia suficiente
cachorro1.energia = 10  # Reduzimos a energia manualmente para simular pouca energia
cachorro1.exercitar()  # Não tem energia suficiente para se exercitar

# O cachorro dorme, restaurando sua energia
cachorro1.dormir()    # Energia restaurada para 100
cachorro1.exercitar() # Agora o cachorro pode se exercitar novamente

cachorro1.exercitar() # Agora o cachorro pode se exercitar novamente

cachorro1.exercitar() # Agora o cachorro pode se exercitar novamente

cachorro1.exercitar() # Agora o cachorro pode se exercitar novamente

cachorro1.exercitar() # Agora o cachorro pode se exercitar novamente

cachorro1.exercitar() # Agora o cachorro pode se exercitar novamente
