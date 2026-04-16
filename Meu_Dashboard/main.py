import time

class Maquinas_industria():
    def __init__(self, nome, potencia_nominal_w, tarifa_kwh):
        self.nome_maquina = nome
        self.potencia_nominal = potencia_nominal_w
        self.tarifa = tarifa_kwh
        self.estados_possiveis = ["Operando","Desligada"]
        self.estado_atual = "Desligada"
        self.temperatura = 0.0
        self.consumo_total = 0.0
        self.tempo_ligada = 0
    def estado(self, novo_estado):
        if novo_estado in self.estados_possiveis:
            self.estado_atual = novo_estado
        else:
            return "Estado inválido"
    def ligar(self):
        if self.estado_atual == "Operando":
            return f"{self.nome_maquina} já está operando"
        self.estado_atual = "Operando"
        self.inicio_operacao = time.time()
        return f"{self.nome_maquina} está ligada"       
    def desligar(self):
        if self.estado_atual == "Desligada":
            return f"{self.nome_maquina} parou de operar"
        self.estado_atual = "Desligada"
        self.final_operacao = time.time()

        tempo_operaçao = self.final_operacao - self.inicio_operacao
        self.tempo_ligada += tempo_operaçao    
        
        tempo_horas = tempo_operaçao / 3600
        
        consumo = (self.potencia_nominal * tempo_horas) / 1000
        self.consumo_total += consumo

        custo = consumo * self.tarifa
        return (
            f"{self.nome_maquina} foi desligada.\n"
            f"Tempo ligada: {tempo_horas} h\n"
            f"Consumo: {consumo:.2f} kWh\n"
            f"Custo: R$ {custo:.4f}"
        )