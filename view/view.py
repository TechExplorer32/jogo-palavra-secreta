import os
class ConsoleUI:
    def __init__(self, controller):
        self.controller = controller
        self.show_welcome_message()

    def show_welcome_message(self):
        print("==============================================")
        print("      Bem-vindo ao Jogo Palavras Secretas     ")
        print("==============================================")
        print("Este jogo permite a você explorar diversas categorias de dados.")
        print("Você pode visualizar informações sobre cores, frutas, animais e automóveis.")
        print("==============================================")
        print("Desenvolvido com   ❤️   por Matheus Franco")
        print("==============================================\n")

    def exibir_item(self, categoria, item):
        print(f"Categoria: {categoria.capitalize()}")
        print(f"{item['nome']}: {item['dica']}\n")

    def iniciar_jogo(self):
        while True:
            self.controller.iniciar_jogo()
            if input("Deseja continuar? (s/n): ").lower() != 's':
                break
        print("Obrigado por jogar!")

    def exibir_estado_inicial(self, categoria, dica, palavra_oculta):
        print(f"Categoria: {categoria}")
        print(f"Dica: {dica}")
        print(f"Palavra: {' '.join(palavra_oculta)} ({len(palavra_oculta)} letras)\n")

    def exibir_estado(self, categoria, dica, palavra_oculta, letras_usadas, tentativas_restantes):
        print(f"Categoria: {categoria}")
        print(f"Dica: {dica}")
        print(f"Palavra: {' '.join(palavra_oculta)}")
        print(f"Letras usadas: {', '.join(letras_usadas)}")
        print(f"Tentativas restantes: {tentativas_restantes}\n")

    def receber_letra(self):
        return input("Digite uma letra: ").lower()

    def exibir_mensagem(self, mensagem):
        print(mensagem + "\n")
    def limpar_terminal(self):
        os.system("cls" if os.name == 'nt' else 'clear')
