import time

class Maquinas_industria():
    def __init__(self, nome, potencia_nominal_w, tarifa_kwh):
        self.nome_maquina = nome
        self.potencia_nominal = potencia_nominal_w
        self.tarifa = tarifa_kwh
        self.estado_atual = "desligada"
        self.temperatura = 0.0
        self.consumo_total = 0.0
        self.tempo_ligada = 0

    def Estado(self, novo_estado):
        self.estado_atual = novo_estado 
        novo_estado = []