# Jogo Palavras Secretas

Este é um jogo de palavras secretas desenvolvido em Python utilizando a arquitetura MVC (Model-View-Controller). O jogo desafia o usuário a adivinhar palavras de diferentes categorias com base em dicas fornecidas.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

raiz/ 
 │ ├── data/ 
  │ └── model.py 
   ├── controller/ 
    │ └── controller.py 
     ├── view/ 
      │ └── view.py 
          └── main.py

- **data/model.py**: Contém a classe `Data` que gerencia os dados das categorias.
- **controller/controller.py**: Contém a classe `Controller` que gerencia a lógica do jogo.
- **view/view.py**: Contém a classe `ConsoleUI` que cuida da interação com o usuário.
- **main.py**: Inicializa o jogo e conecta os componentes.

## Funcionalidades

- Seleção aleatória de palavras de diferentes categorias: cores, frutas, animais e automóveis.
- Dicas são fornecidas para ajudar o usuário a adivinhar a palavra.
- Feedback interativo que atualiza a palavra oculta com letras adivinhadas corretamente.
- Validação de entrada para garantir que apenas uma letra válida seja digitada.
- Contador de tentativas e erros.
- Opção para jogar novamente com o terminal limpo para uma experiência de usuário organizada.

## Como Executar

1. Clone o repositório: https://github.com/TechExplorer32/jogo-palavra-secreta
2. Navegue até o diretório do projeto: cd jogo-palavras-secretas
3. Execute o jogo: python main.py

## Exemplo de Uso

```plaintext
==============================================
   Bem-vindo ao Jogo Palavras Secretas     
==============================================
Este jogo permite a você explorar diversas categorias de dados.
Você pode visualizar informações sobre cores, frutas, animais e automóveis.
==============================================
Desenvolvido com ❤️ por Matheus Franco
==============================================

Pressione Enter para começar o jogo...
Categoria: Frutas
Dica: A fruta proibida do paraíso.
Palavra: **** (4 letras)

Digite uma letra: a
Parabéns! A letra 'a' está na palavra: **a*

...

Deseja continuar? (s/n): s
