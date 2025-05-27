#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color, Stop
from pybricks.parameters import Button  
from pybricks.tools import wait
import time

# Inicialização dos dispositivos
ev3 = EV3Brick()
motor_garra = Motor(Port.A)
motor_y = Motor(Port.B)
motor_x = Motor(Port.C)
sensor_cor = ColorSensor(Port.S1)

#ATENÇÃO: SEMPRE DEIXAR A GARRA ABERTA PARA A LÓGICA DO CÓDIGO
def sobe_garra_amarelo():
    motor_y.run_angle(300, -550, then=Stop.HOLD, wait=True)
# Função para abrir ou fechar a garra
def acao_garra(abrir=True):
    if abrir:
        motor_garra.run_time(100, 1000, then=Stop.HOLD, wait=True)  # Abre a garra
        # motor_garra.run_angle(300, -250, then=Stop.HOLD, wait=True)
    else:
        motor_garra.run_time(-100, 1000, then=Stop.HOLD, wait=True)  # Fecha a garra
        # motor_garra.run_angle(300, -250, then=Stop.HOLD, wait=True)

# Funções para movimentação dos eixos
def eixo_y_cima():
    motor_y.run_angle(300, -250, then=Stop.HOLD, wait=True)
    # motor_y.run_time(300, 3000, then=Stop.HOLD, wait=True)

def eixo_y_baixo():
    motor_y.run_angle(300, 500, then=Stop.HOLD, wait=True)
    # motor_y.run_time(300, 3000, then=Stop.HOLD, wait=True)

def eixo_x_right():
    motor_x.run_angle(300, 320, then=Stop.HOLD, wait=True)

def eixo_x_left():
    motor_x.run_angle(300, -320, then=Stop.HOLD, wait=True)

# Função para executar uma sequência de ações com base na cor detectada
def acao_baseada_na_cor(cor):
    if cor == Color.RED:
        # Exemplo de sequência para a cor vermelha
        print("Cor vermelha detectada - Executando sequência")
        eixo_y_cima()
        eixo_x_right()
        eixo_y_baixo()
        acao_garra(abrir=True)  # Fecha a garra
        eixo_y_cima()
        eixo_x_left()
        wait(2000)
        acao_garra(abrir=False)  # Abre para soltar
        wait(2000)  
        print(motor_x.angle(), motor_y.angle())
        motor_y.run_target(300, 0, then=Stop.HOLD, wait=True)
        motor_x.run_target(300, 0, then=Stop.HOLD, wait=True)

    elif cor == Color.YELLOW:
        # Exemplo de sequência para a cor azul
        print("Cor amarela detectada - Executando sequência")
        eixo_y_baixo()
        acao_garra(abrir=True)
        wait(2000)
        sobe_garra_amarelo()
        wait(2000)
        acao_garra(abrir=False)
        print(motor_x.angle(), motor_y.angle())
        motor_y.run_target(300, 0, then=Stop.HOLD, wait=True)
        motor_x.run_target(300, 0, then=Stop.HOLD, wait=True)
    elif cor == Color.GREEN:
        # Exemplo de sequência para a cor verde
        print("Cor verde detectada - Executando sequência")
        eixo_y_cima()
        eixo_x_left()
        eixo_y_baixo()
        acao_garra(abrir=False)
        eixo_y_cima()
        eixo_x_right()
        wait(2000)
        acao_garra(abrir=True)
        wait(2000)
        print(motor_x.angle(), motor_y.angle())
        motor_y.run_target(300, 0, then=Stop.HOLD, wait=True)
        motor_x.run_target(300, 0, then=Stop.HOLD, wait=True)


# Loop principal
while True:

    # if Button.CENTER in ev3.buttons.pressed():
    #     print("Botão CENTER pressionado. Encerrando o programa.")
    #     break

    cor_detectada = sensor_cor.color()
    print("Cor detectada:", cor_detectada)
    acao_baseada_na_cor(cor_detectada)
    
    wait(2000)  # Evita leituras excessivas