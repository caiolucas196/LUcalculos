# Variáveis iniciais
total_clientes = 100  # Total de clientes iniciais
cac = 150  # Custo de aquisição por cliente
ticket_medio_primeira_compra = 100  # Ticket médio da primeira compra
ticket_medio_recompra = 200  # Ticket médio das recompras
margem_lucro = 0.30  # Margem de lucro por transação
probabilidade_recompra_mes1 = 0.20  # Probabilidade de recompra no mês 1
probabilidade_recompra_mes10 = 0.05  # Probabilidade de recompra no mês 10

def calcular_probabilidade(mes):
    """Calcula a probabilidade de recompra para um mês específico (1 ao 10)."""
    if mes == 1:
        return probabilidade_recompra_mes1
    elif 1 < mes <= 10:
        return max(probabilidade_recompra_mes1 - (0.015 * (mes - 1)), probabilidade_recompra_mes10)
    return probabilidade_recompra_mes10

# Simulação do lucro acumulado
lucro_acumulado = -total_clientes * cac  # Começa negativado pelo CAC
clientes_restantes = total_clientes
mes = 0

while lucro_acumulado < 0:
    mes += 1
    probabilidade_recompra = calcular_probabilidade(mes)
    recompras = clientes_restantes * probabilidade_recompra
    receita_recompra = recompras * ticket_medio_recompra
    lucro_recompra = receita_recompra * margem_lucro
    lucro_acumulado += lucro_recompra

    # Atualiza o número de clientes restantes (perda de 1,5% por mês)
    clientes_restantes -= clientes_restantes * 0.015

    # Exibe os dados do mês atual
    print(f"Mês {mes}:"
          f"  Probabilidade de Recompra: {probabilidade_recompra * 100:.2f}%"
          f"  Clientes Restantes: {clientes_restantes:.2f}"
          f"  Lucro do Mês: R${lucro_recompra:.2f}"
          f"  Lucro Acumulado: R${lucro_acumulado:.2f}")
# Resultado final
print(f"Os clientes se tornam lucrativos após: {mes} meses.")