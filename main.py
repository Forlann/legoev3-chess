from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait
import keyboard  # biblioteca para capturar eventos do teclado

# Configuração dos motores
motor_garra = Motor(Port.A)
motor_carrinho = Motor(Port.B)

# Função para mover a garra
def mover_garra(direcao):
    if direcao == 'abrir':
        motor_garra.run_target(500, 90)  # exemplo de abrir a garra
    elif direcao == 'fechar':
        motor_garra.run_target(500, 0)  # exemplo de fechar a garra

# Função para mover o carrinho
def mover_carrinho(direcao):
    if direcao == 'frente':
        motor_carrinho.run_time(500, 1000)  # exemplo de mover para frente
    elif direcao == 'traseira':
        motor_carrinho.run_time(500, -1000)  # exemplo de mover para trás

# Loop para capturar comandos do teclado
while True:
    if keyboard.is_pressed('w'):
        mover_carrinho('frente')
        wait(100)  # pequeno delay para evitar múltiplas capturas
    elif keyboard.is_pressed('s'):
        mover_carrinho('traseira')
        wait(100)
    elif keyboard.is_pressed('a'):
        mover_garra('abrir')
        wait(100)
    elif keyboard.is_pressed('d'):
        mover_garra('fechar')
        wait(100)
