from view.view import ConsoleUI
from data.model import Data
from control.controller import Controller

if __name__ == "__main__":
    data = Data()
    view = ConsoleUI(None)  # Inicialmente None para evitar erro de referência circular
    controller = Controller(data, view)
    view.controller = controller  # Definir o controlador após a criação
    view.iniciar_jogo()
