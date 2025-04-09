from ev3dev2.motor import MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C
from ev3dev2.motor import SpeedPercent
from time import sleep

# Motores conectados nas portas A, B e C
motor_garra = MediumMotor(OUTPUT_A)     # abre/fecha
motor_elevador = MediumMotor(OUTPUT_B)  # sobe/desce
motor_extra = MediumMotor(OUTPUT_C)     # outra função (ex: rotação)

# Funções da garra
def abrir_garra():
    motor_garra.on_for_degrees(SpeedPercent(20), 90)
    
def fechar_garra():
    motor_garra.on_for_degrees(SpeedPercent(20), -90)

def subir():
    motor_elevador.on_for_degrees(SpeedPercent(30), 180)

def descer():
    motor_elevador.on_for_degrees(SpeedPercent(30), -180)

# Teste simples
abrir_garra()
sleep(1)
fechar_garra()
sleep(1)
subir()
sleep(1)
descer()
