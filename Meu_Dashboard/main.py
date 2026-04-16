import time

class Maquinas_industria():
    def __init__(self, nome, potencia_nominal_w, tarifa_kwh):
        self.nome_maquina = nome
        self.potencia_nominal = potencia_nominal_w
        self.tarifa = tarifa_kwh
        self.estados_possiveis = ["Operando","Desligada"]
        self.estado_atual = "Desligada"
        self.temperatura_atual = 0.0
        self.temperatura_media = 0.0
        self.temperatura_minima = 0.0
        self.temperatura_maxima = 0.0
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
    def definir_limites_temperatura(self, limite=120.0, alerta=90.0, critica=140.0):
        self.temp_limite = limite
        self.temp_alerta = alerta
        self.temp_critica = critica
    
    def verificar_temperatura(self):
        if self.temperatura_atual >= self.temp_critica:
            return "CRÍTICO - desligamento imediato"
    
        elif self.temperatura_atual >= self.temp_limite:
            return "ALTO RISCO - acima do limite"
    
        elif self.temperatura_atual >= self.temp_alerta:
            return "ALERTA - temperatura elevada"
    
        else:
            return "NORMAL"
    def atualizar_temperatura(self, nova_temp):
        self.temperatura_atual = nova_temp

        if self.temperatura_minima == 0 or nova_temp < self.temperatura_minima:
            self.temperatura_minima = nova_temp

        if nova_temp > self.temperatura_maxima:
            self.temperatura_maxima = nova_temp

        self.temperatura_media = (self.temperatura_media + nova_temp) / 2

    
    def desligar(self):
        if self.estado_atual == "Desligada":
            return f"{self.nome_maquina} parou de operar"
        self.estado_atual = "Desligada"
        self.final_operacao = time.time()

        tempo_operacao = self.final_operacao - self.inicio_operacao
        self.tempo_ligada += tempo_operacao    
        
        tempo_horas = tempo_operacao / 3600
        
        consumo = (self.potencia_nominal * tempo_horas) / 1000
        self.consumo_total += consumo

        custo = consumo * self.tarifa
        return (
            f"{self.nome_maquina} foi desligada.\n"
            f"Tempo ligada: {tempo_horas} h\n"
            f"Consumo: {consumo} kWh\n"
            f"Custo: R$ {custo}"
        )