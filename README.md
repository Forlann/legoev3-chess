![image](https://github.com/user-attachments/assets/aa9cbaf1-70f8-4080-b9a9-a803ddfcd8df)

# Projeto de Garra Robótica com Lego EV3 Mindstorm

## Descrição

Este projeto foi desenvolvido para a disciplina de Robótica da faculdade Impacta Tecnologia, utilizando o **Lego EV3 Mindstorm**. O objetivo do projeto é criar uma garra robótica que executa 3 movimentos de acordo com uma das 3 cores detectadas(Vermelho, Verde e Amarelo) por um sensor de cor. A garra pode abrir e fechar, e a movimentação é controlada por três eixos.

O código implementado no EV3Brick permite que o robô execute diferentes sequências de movimentos baseadas na cor do objeto detectado pelo sensor. As cores que são reconhecidas são **vermelho**, **azul** e **verde**, e para cada cor há uma sequência de movimentos específica.

## Requisitos

* Lego EV3 Mindstorm
* Pybricks MicroPython
* Sensor de Cor (Porta S1)
* Motores para movimentação da garra e dos eixos X e Y

## Estrutura do Projeto

* **Motor A:** Controla o motor da garra
* **Motor B:** Controla o eixo Y
* **Motor C:** Controla o eixo X
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
* **sobe\_garra\_amarelo()**: Sobe o eixo y quando dectectado a cor amarela

### Sequência de Ações

* **Cor Vermelha**: Sobe a garra, eixo x vai para a direita, eixo y desce, fecha a garra, sobe o eixo y, eixo x vai para esquerda(volta ao centro), abre a garra.
* **Cor Amarelo**: eixo y desce, fecha a garra, sobe o eixo y, abre a garra.
* **Cor Verde**: Sobe a garra, eixo x vai para a esquerda, eixo y desce, fecha a garra, sobe o eixo y, eixo x vai para a direita(volta ao centro, abre a garra). 
## Como Rodar o Código

1. **Instale o Pybricks MicroPython** no seu Lego EV3.
2. **Conecte o motor e o sensor** nas portas corretas conforme o código:

   * Motor da garra na porta A
   * Eixo X na porta C
   * Eixo Y na porta D
   * Sensor de cor na porta S1

3. **Deixe a garra aberta** antes de rodar o código
4. **Carregue o código no seu EV3** e execute.
5. **Observe a detecção das cores** e a execução da sequência de movimentos com base na cor detectada.

## Grupo/Colaboradores

 - Kauê Forlan - 2202416
 - Henrique Diego
 - Gustavo Rodrigues - 2302446

Se você quiser contribuir com o projeto, fique à vontade para criar um *fork*, fazer alterações e enviar um *pull request*.
