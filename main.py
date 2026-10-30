def calcular_saldo_final(capital_inicial, tasa_anual, anios, aportacion_mensual):
    """Calcula el saldo final con interés compuesto mensual y aportaciones."""
    tasa_mensual = tasa_anual / 12
    saldo = capital_inicial
    
    for mes in range(anios * 12):
        saldo = saldo * (1 + tasa_mensual) + aportacion_mensual
        
    return saldo

if __name__ == "__main__":
    capital = 10_000
    tasa = 0.10
    anios = 5
    aportacion = 1_000

    saldo = calcular_saldo_final(capital, tasa, anios, aportacion)
    total_aportado = capital + aportacion * anios * 12
    intereses = saldo - total_aportado

    print(f"Saldo final:       ${saldo:,.2f}")
    print(f"Total aportado:    ${total_aportado:,.2f}")
    print(f"Intereses ganados: ${intereses:,.2f}")