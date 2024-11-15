import random
from data.model import Data
from view.view import ConsoleUI

class Controller:
    def __init__(self, data, view):
        self.data = data
        self.view = view

    def obter_item_aleatorio(self):
        categorias = ["cores", "frutas", "animais", "automoveis"]
        categoria = random.choice(categorias)

        if categoria == "cores":
            itens = self.data.get_cores()
        elif categoria == "frutas":
            itens = self.data.get_frutas()
        elif categoria == "animais":
            itens = self.data.get_animais()
        elif categoria == "automoveis":
            itens = self.data.get_automoveis()

        item_aleatorio = random.choice(itens)
        return categoria, item_aleatorio

    def iniciar_jogo(self):
        input("Pressione Enter para começar o jogo...")
        categoria, item = self.obter_item_aleatorio()
        palavra = item['nome'].lower()
        dica = item['dica']
        palavra_oculta = ["*" for _ in palavra]
        tentativas_restantes = 6
        letras_usadas = []
        erros = 0

        self.view.exibir_estado_inicial(categoria, dica, palavra_oculta)

        while tentativas_restantes > 0 and "*" in palavra_oculta:
            letra = self.view.receber_letra()

            if not self.validar_entrada(letra):
                self.view.exibir_mensagem("Entrada inválida. Por favor, digite apenas uma letra.")
                continue

            if letra in letras_usadas:
                self.view.exibir_mensagem("Você já usou essa letra. Tente outra.")
                continue

            letras_usadas.append(letra)

            if self.verificar_letra(letra, palavra, palavra_oculta):
                self.view.exibir_mensagem(f"Parabéns! A letra '{letra}' está na palavra: {''.join(palavra_oculta)}")
            else:
                tentativas_restantes -= 1
                erros += 1
                self.view.exibir_mensagem(f"A letra '{letra}' não está na palavra. Você tem {tentativas_restantes} tentativas restantes e cometeu {erros} erro(s).")

        if "*" not in palavra_oculta:
            self.view.exibir_mensagem(f"Parabéns! Você adivinhou a palavra: {''.join(palavra_oculta)}")
        else:
            self.view.exibir_mensagem(f"Que pena! Você não conseguiu adivinhar a palavra: {palavra}")

    def verificar_letra(self, letra, palavra, palavra_oculta):
        acertou = False
        for i in range(len(palavra)):
            if palavra[i] == letra:
                palavra_oculta[i] = letra
                acertou = True
        return acertou

    def validar_entrada(self, entrada):
        return len(entrada) == 1 and entrada.isalpha()
