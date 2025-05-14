#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color, Stop
import time

# Inicialização dos dispositivos
ev3 = EV3Brick()
motor_garra = Motor(Port.A)
motor_y = Motor(Port.B)
motor_x = Motor(Port.C)
sensor_cor = ColorSensor(Port.S1)

# Função para abrir ou fechar a garra
def acao_garra(abrir=True):
    if abrir:
        motor_garra.run_target(1000, 90)  # Abre a garra
    else:
        motor_garra.run_target(1000, 0)  # Fecha a garra

# Funções para movimentação dos eixos
def eixo_y_cima():
    motor_y.run_angle(300, 360, then=Stop.HOLD, wait=True)

def eixo_y_baixo():
    motor_y.run_angle(300, -360, then=Stop.HOLD, wait=True)

def eixo_x_right():
    motor_x.run_angle(300, 360, then=Stop.HOLD, wait=True)

def eixo_x_left():
    motor_x.run_angle(300, -360, then=Stop.HOLD, wait=True)

# Função para executar uma sequência de ações com base na cor detectada
def acao_baseada_na_cor(cor):
    if cor == Color.RED:
        # Exemplo de sequência para a cor vermelha
        print("Cor vermelha detectada - Executando sequência")
        acao_garra(abrir=True)
        time.sleep(1)
        acao_garra(abrir=False)
        eixo_x_right()
        time.sleep(1)
        eixo_x_left()
        time.sleep(1)
        eixo_y_cima()
        time.sleep(1)
        eixo_y_baixo()
        time.sleep(1)
    elif cor == Color.BLUE:
        # Exemplo de sequência para a cor azul
        print("Cor azul detectada - Executando sequência")
        eixo_x_right()
        time.sleep(1)
        eixo_x_left()
        time.sleep(1)
    elif cor == Color.GREEN:
        # Exemplo de sequência para a cor verde
        print("Cor verde detectada - Executando sequência")
        eixo_y_cima()
        time.sleep(1)
        eixo_y_baixo()
        time.sleep(1)

# Loop principal
while True:
    cor_detectada = sensor_cor.color()
    print("Cor detectada:", cor_detectada)
    acao_baseada_na_cor(cor_detectada)
    time.sleep(0.5)  # Evita leituras excessivas
