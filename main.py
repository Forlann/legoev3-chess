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
motor_x = Motor(Port.C)
motor_y = Motor(Port.D)
motor_z = Motor(Port.B)
sensor_cor = ColorSensor(Port.S1)

# Função para abrir ou fechar a garra
def acao_garra(abrir=True):
    if abrir:
        motor_garra.run_time(100, 2000, then=Stop.HOLD, wait=True)  # Abre a garra
    else:
        motor_garra.run_time(-100, 2000, then=Stop.HOLD, wait=True)  # Fecha a garra

# Funções para movimentação dos eixos
def eixo_y_cima():
    motor_y.run_angle(300, 360, then=Stop.HOLD, wait=True)

def eixo_y_baixo():
    motor_y.run_angle(300, -180, then=Stop.HOLD, wait=True)

def eixo_x_right():
    motor_x.run_angle(300, 360, then=Stop.HOLD, wait=True)

def eixo_x_left():
    motor_x.run_angle(300, -360, then=Stop.HOLD, wait=True)

# Função para executar uma sequência de ações com base na cor detectada
def acao_baseada_na_cor(cor):
    if cor == Color.RED:
        # Exemplo de sequência para a cor vermelha
        print("Cor vermelha detectada - Executando sequência")
        eixo_y_cima()
        acao_garra(abrir=True)
        acao_garra(abrir=False)
        eixo_x_right()
        eixo_x_left()
        eixo_y_baixo()
        acao_garra(abrir=True)
    elif cor == Color.BLUE:
        # Exemplo de sequência para a cor azul
        print("Cor azul detectada - Executando sequência")
        eixo_x_right()
        wait(1000)
        eixo_x_left()
        wait(1000)
    elif cor == Color.GREEN:
        # Exemplo de sequência para a cor verde
        print("Cor verde detectada - Executando sequência")
        eixo_y_cima()
        wait(1000)
        eixo_y_baixo()
        wait(1000)

# Loop principal
while True:

    # if Button.CENTER in ev3.buttons.pressed():
    #     print("Botão CENTER pressionado. Encerrando o programa.")
    #     break

    cor_detectada = sensor_cor.color()
    print("Cor detectada:", cor_detectada)
    acao_baseada_na_cor(cor_detectada)
    
    wait(5000)  # Evita leituras excessivas