# Variáveis iniciais
total_clientes = 100  # Total de clientes iniciais
cac = 150  # Custo de aquisição por cliente
ticket_medio_recompra = 200  # Ticket médio das recompras
margem_lucro = 0.30  # Margem de lucro por transação
desconto = 0.15  # Desconto aplicado (15%)
probabilidade_total_recompra = 0.20  # Probabilidade total de recompra por mês
probabilidade_sem_desconto = 0.05  # Porcentagem que paga o valor cheio
probabilidade_com_desconto = 0.15  # Porcentagem que usa o desconto
meses = 48  # Período de 4 anos (48 meses)
# Ajuste dos tickets médios
ticket_medio_com_desconto = ticket_medio_recompra * (1 - desconto)
ticket_medio_sem_desconto = ticket_medio_recompra  # Valor cheio
# Inicializando acumuladores
lucro_acumulado = -total_clientes * cac  # Começa negativado pelo CAC
receita_total = 0
for mes in range(1, meses + 1):
    # Clientes que compram com e sem desconto
    clientes_compram_com_desconto = total_clientes * probabilidade_com_desconto
    clientes_compram_sem_desconto = total_clientes * probabilidade_sem_desconto
    # Receita gerada com desconto e sem desconto
    receita_com_desconto = clientes_compram_com_desconto * ticket_medio_com_desconto
    receita_sem_desconto = clientes_compram_sem_desconto * ticket_medio_sem_desconto
    receita_mes = receita_com_desconto + receita_sem_desconto
    # Lucro gerado no mês
    lucro_recompra_com_desconto = receita_com_desconto * margem_lucro
    lucro_recompra_sem_desconto = receita_sem_desconto * margem_lucro
    lucro_mes = lucro_recompra_com_desconto + lucro_recompra_sem_desconto
    # Atualiza os acumuladores
    lucro_acumulado += lucro_mes
    receita_total += receita_mes
    # Exibe os dados do mês atual
    print(f"Mês {mes}:"
          f"  Receita do Mês: R${receita_mes:.2f}"
          f"  Lucro do Mês: R${lucro_mes:.2f}"
          f"  Lucro Acumulado: R${lucro_acumulado:.2f}")

# Resultado final
print(f"\nResumo após {meses} meses:")
print(f"  Receita Total: R${receita_total:.2f}")
print(f"  Lucro Total: R${lucro_acumulado:.2f}")