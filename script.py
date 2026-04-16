import plotly.graph_objects as go
import numpy as np
import pandas as pd

# Gerando dados da simulação
tempo = np.linspace(0, 30, 300)
energia = np.where(tempo <= 5, 1500, 500)
temperatura = 80 * (1 - np.exp(-0.15 * tempo))

# Criando a figura
fig = go.Figure()

# Adicionando a linha de Energia (Eixo Y1)
fig.add_trace(go.Scatter(
    x=tempo, y=energia,
    name="Consumo Elétrico (W)",
    line=dict(color='#00d1ff', width=3, shape='hv'), # 'hv' cria o degrau do pico
    fill='tozeroy', # Preenchimento abaixo da linha
    fillcolor='rgba(0, 209, 255, 0.1)'
))

# Adicionando a linha de Temperatura (Eixo Y2)
fig.add_trace(go.Scatter(
    x=tempo, y=temperatura,
    name="Temperatura (°C)",
    yaxis="y2",
    line=dict(color='#ff4b4b', width=4, shape='spline'), # 'spline' deixa a curva suave
))

# Layout Moderno
fig.update_layout(
    title="Dashboard de Operação da Máquina",
    template="plotly_dark", # Tema escuro
    hovermode="x unified",
    xaxis=dict(title="Tempo (segundos)", gridcolor='#333'),
    yaxis=dict(title="Energia (Watts)", side="left", gridcolor='#333'),
    yaxis2=dict(title="Temperatura (°C)", overlaying="y", side="right", showgrid=False),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

fig.show()
