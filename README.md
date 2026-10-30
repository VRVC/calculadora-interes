# Calculadora de interés compuesto

Calcula el saldo final de una inversión con interés compuesto mensual
y aportaciones periódicas.

## ¿Qué hace?

Dado un capital inicial, una tasa anual, un plazo en años y una aportación mensual, simula mes a mes el crecimiento del saldo y muestra:

 - Saldo final
 - Total aportado
 - Intereses ganados

 # Cómo usarlo

 1. Clona el repositorio
   ```
   git clone https://github.com/VRVC/calculadora-interes.git
   cd calculadora-interes
   ```
 2. Crea y activa un entorno virtual (Windows):
   ```
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```
 3. Ejecuta:
   ```
   python main.py
   ```
 4. Ingresa tus datos:

 ## Ejemplo

 Con $10,000 iniciales, tasa del 12% anual, 5 años y $1,000 mensuales:

 ```
 Saldo final:       $99.836.64
 Total aportado:    $70,000.00
 Intereses ganados: $29,836.64
 ```

 # Próximas mejoras

 - [x] Pedir los datos al usuario en lugar de tenerlos fijos en el código
 - [ ] Ajustar el resultado por inflación
 - [ ] Graficar la evolución del saldo