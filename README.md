# Projeto de Garra Robótica com Lego EV3 Mindstorm

## Descrição

Este projeto foi desenvolvido para a disciplina de Robótica da faculdade, utilizando o **Lego EV3 Mindstorm**. O objetivo do projeto é criar uma garra robótica que executa movimentos de acordo com a cor detectada por um sensor de cor. A garra pode abrir e fechar, e a movimentação é controlada por três eixos.

O código implementado no EV3Brick permite que o robô execute diferentes sequências de movimentos baseadas na cor do objeto detectado pelo sensor. As cores que são reconhecidas são **vermelho**, **azul** e **verde**, e para cada cor há uma sequência de movimentos específica.

## Requisitos

* Lego EV3 Mindstorm
* Pybricks MicroPython
* Sensor de Cor (Porta S1)
* Motores para movimentação da garra e dos eixos X, Y e Z

## Estrutura do Projeto

* **Motor A:** Controla o motor da garra
* **Motor B:** Controla o eixo Z
* **Motor C:** Controla o eixo X
* **Motor D:** Controla o eixo Y
* **Sensor S1:** Detecta a cor do objeto

## Como Funciona

O código implementa a lógica para abrir/fechar a garra e mover os eixos com base na cor do objeto detectado pelo sensor de cor.

### Funções principais

* **acao\_garra(abrir=True)**: Função para abrir ou fechar a garra.
* **eixo\_y\_cima()**: Move o eixo Y para cima.
* **eixo\_y\_baixo()**: Move o eixo Y para baixo.
* **eixo\_x\_right()**: Move o eixo X para a direita.
* **eixo\_x\_left()**: Move o eixo X para a esquerda.
* **acao\_baseada\_na\_cor(cor)**: Executa uma sequência de movimentos com base na cor detectada.

### Sequência de Ações

* **Cor Vermelha**: Abre e fecha a garra, move o eixo Y para cima e para baixo, e o eixo X para a direita e esquerda.
* **Cor Azul**: Movimenta o eixo X para a direita e para a esquerda.
* **Cor Verde**: Move o eixo Y para cima e para baixo.

## Como Rodar o Código

1. **Instale o Pybricks MicroPython** no seu Lego EV3.
2. **Conecte o motor e o sensor** nas portas corretas conforme o código:

   * Motor da garra na porta A
   * Eixo X na porta C
   * Eixo Y na porta D
   * Sensor de cor na porta S1
3. **Carregue o código no seu EV3** e execute.
4. **Observe a detecção das cores** e a execução da sequência de movimentos com base na cor detectada.

## Grupo/Colaboradores

Se você quiser contribuir com o projeto, fique à vontade para criar um *fork*, fazer alterações e enviar um *pull request*.
