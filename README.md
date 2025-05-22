# TrabalhoLivreOO

Trabalho Livre Da materia De Orientaçao a Obejetos

O codigo é um jogo da cobrinha com um sistema de login. 
ao iniciar a "main.py" deve abrir uma tela para por usuario e senha, e caso o usario não exista basta clicar em "Novo Usuario" e o usuario sera adicionado.
caso o usuario ja exista basta fazer login. apos o login abrira uma nova janela com 2 botoes 1 para iniciar o jogo outro para ver uma lista do top 5 usuarios com os maiores record
  ao iniciar o jogo abrira uma tela do pygame e começara a rodar o jogo, para se mover utilize os botoes "WASD". o objetivo e pegar a fruta (quadrado vermelho) e quanto mais frutas o player pegar maior vai ser sua pontuaçao, caso o player colida com seu proprio corpo ele perdera e a tela do pygame fechara e voltara para o menu com os 2 botoes


# possiveis erros
  o jogo tem um problema caso o player consiga executar comandos especificos muito rapido ele pode fechar, exemplo ir para baixo e para esquerda muito rapido

# bibliotecas utilizadas

PyQt6
  utilizado para fazer a interface grafica da maior parte das janelas

  para instalar utilize

  pip install PyQt6
  
Pygame
  utilizado para fazer a parte grafica da tela do jogo

  para instalar utilize

  pip install pygame
