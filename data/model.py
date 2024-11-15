# data/model.py
class Data:
    def __init__(self):
        # Inicializa listas para armazenar dados de cada categoria
        self.cores = []       # Lista de cores
        self.frutas = []      # Lista de frutas
        self.animais = []     # Lista de animais
        self.automoveis = []  # Lista de automóveis

        # Popula as listas com dados iniciais
        self.populate_data()

    def populate_data(self):
        # Adiciona cores à lista de cores com dicas
        self.add_cor("Vermelho", "A cor do fogo e do amor.")
        self.add_cor("Azul", "A cor do céu e do mar.")
        self.add_cor("Verde", "A cor da natureza e da esperança.")
        self.add_cor("Amarelo", "A cor do sol e do limão.")
        self.add_cor("Roxo", "A cor da realeza e da magia.")
        self.add_cor("Laranja", "A cor da laranja e da abóbora.")
        self.add_cor("Rosa", "A cor das flores e dos sonhos.")
        self.add_cor("Marrom", "A cor do chocolate e da terra.")
        self.add_cor("Cinza", "A cor das nuvens e do elefante.")
        self.add_cor("Preto", "A cor da noite e do gato.")

        # Adiciona frutas à lista de frutas com dicas
        self.add_fruta("Maçã", "A fruta proibida do paraíso.")
        self.add_fruta("Banana", "A fruta amarela que os macacos adoram.")
        self.add_fruta("Laranja", "A fruta cítrica que dá nome a uma cor.")
        self.add_fruta("Morango", "A fruta vermelha e doce que usamos para fazer geleia.")
        self.add_fruta("Uva", "A fruta que cresce em cachos e fazemos vinho.")
        self.add_fruta("Melancia", "A fruta gigante e refrescante, perfeita para o verão.")
        self.add_fruta("Pera", "A fruta com formato de lâmpada.")
        self.add_fruta("Abacaxi", "A fruta com espinhos por fora e doce por dentro.")
        self.add_fruta("Manga", "A fruta tropical com polpa amarela e saboroso.")
        self.add_fruta("Kiwi", "A fruta verde e peluda com sementes pretas.")

        # Adiciona animais à lista de animais com dicas
        self.add_animal("Leão", "O rei da selva com uma juba dourada.")
        self.add_animal("Elefante", "O maior animal terrestre com tromba grande.")
        self.add_animal("Tigre", "O felino com listras alaranjadas e negras.")
        self.add_animal("Girafa", "O animal com pescoço comprido e manchas marrons.")
        self.add_animal("Pinguim", "A ave que não voa e vive no gelo.")
        self.add_animal("Golfinho", "O mamífero marinho que salta e faz acrobacias.")
        self.add_animal("Panda", "O urso preto e branco com paixão por bambu.")
        self.add_animal("Canguru", "O marsupial que pula e carrega seus filhotes em uma bolsa.")
        self.add_animal("Falcão", "A ave de rapina com visão aguçada.")
        self.add_animal("Tartaruga", "O réptil com casco duro e vida longa.")

        # Adiciona automóveis à lista de automóveis com dicas
        self.add_automovel("Ferrari", "O carro esportivo italiano, símbolo de luxo e velocidade.")
        self.add_automovel("Lamborghini", "O rival da Ferrari, também famoso por seus carros esportivos.")
        self.add_automovel("Tesla", "O carro elétrico inovador de Elon Musk.")
        self.add_automovel("BMW", "A marca alemã conhecida por seus sedãs e esportivos.")
        self.add_automovel("Mercedes", "Outra marca alemã de luxo, com uma longa história.")
        self.add_automovel("Audi", "A marca dos quatro anéis, também alemã e com modelos esportivos e luxuosos.")
        self.add_automovel("Porsche", "A marca esportiva alemã, famosa pelo modelo 911.")
        self.add_automovel("Jaguar", "A marca britânica de luxo, com carros esportivos e sedãs elegantes.")
        self.add_automovel("Volvo", "A marca sueca conhecida por sua segurança e design.")
        self.add_automovel("Maserati", "A marca italiana de luxo, com carros esportivos e sedãs elegantes.")

    def add_cor(self, cor, dica="É uma cor"):
        # Adiciona uma nova cor à lista de cores com uma dica
        self.cores.append({"nome": cor, "dica": dica})

    def add_fruta(self, fruta, dica="É uma fruta"):
        # Adiciona uma nova fruta à lista de frutas com uma dica
        self.frutas.append({"nome": fruta, "dica": dica})

    def add_animal(self, animal, dica="É um animal"):
        # Adiciona um novo animal à lista de animais com uma dica
        self.animais.append({"nome": animal, "dica": dica})

    def add_automovel(self, automovel, dica="É um automóvel"):
        # Adiciona um novo automóvel à lista de automóveis com uma dica
        self.automoveis.append({"nome": automovel, "dica": dica})

    def get_cores(self):
        # Retorna a lista de cores com dicas
        return self.cores

    def get_frutas(self):
        # Retorna a lista de frutas com dicas
        return self.frutas

    def get_animais(self):
        # Retorna a lista de animais com dicas
        return self.animais

    def get_automoveis(self):
        # Retorna a lista de automóveis com dicas
        return self.automoveis
