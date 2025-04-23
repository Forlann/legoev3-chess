from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color

# Inicialização dos dispositivos
ev3 = EV3Brick()
motor_rodas = Motor(Port.A)
motor_garra = Motor(Port.B)
motor_eixo = Motor(Port.C)
sensor_cor = ColorSensor(Port.S1)

# Função para mover o robô para frente
def mover_para_frente():
    motor_rodas.run_time(500, 1000)  # Move as rodas para frente por 500ms

# Função para girar o robô no próprio eixo
def girar_eixo():
    motor_eixo.run_time(500, 500)  # Gira o eixo por 500ms

# Função para abrir ou fechar a garra
def acao_garra(abrir=True):
    if abrir:
        motor_garra.run_target(1000, 90)  # Abre a garra
    else:
        motor_garra.run_target(1000, 0)  # Fecha a garra

# Loop principal
while True:
    cor_detectada = sensor_cor.color()

    if cor_detectada == Color.RED:
        girar_eixo()
    elif cor_detectada == Color.BLUE:
        acao_garra(abrir=True)
    elif cor_detectada == Color.GREEN:
        girar_eixo()
    else:
        mover_para_frente()
