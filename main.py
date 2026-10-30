def calcular_saldo_final(capital_inicial, tasa_anual, anios, aportacion_mensual):
    """Calcula el saldo final con interés compuesto mensual y aportaciones."""
    tasa_mensual = tasa_anual / 12
    saldo = capital_inicial
    
    for mes in range(anios * 12):
        saldo = saldo * (1 + tasa_mensual) + aportacion_mensual
        
    return saldo

def pedir_numero(mensaje):
    """ Pide un número al usuario y repite la pregunta si la entrada no es válida."""
    while True:
        texto = input(mensaje)
        try:
            return float(texto)
        except ValueError:
            print("Eso no es un número válido. Intenta de nuevo.")
            
if __name__ == "__main__":
    capital = pedir_numero("Capital inicial:")
    tasa = pedir_numero("Tasa anual en % (ej. 12): ") / 100
    anios = int(pedir_numero("Plazo en años: "))
    aportacion = pedir_numero("Aportación mensual: ")
    inflacion = pedir_numero("Infalcion anual en %: ") / 100

    saldo = calcular_saldo_final(capital, tasa, anios, aportacion) / (1 + inflacion) ** anios
    total_aportado = capital + aportacion * anios * 12
    intereses = saldo - total_aportado

    print(f"Saldo final:       ${saldo:,.2f}")
    print(f"Total aportado:    ${total_aportado:,.2f}")
    print(f"Intereses ganados: ${intereses:,.2f}") 