# 📊 Homework de Funciones Financieras - HW-4

## 🎯 Resumen del Ejercicio

Este ejercicio implementa tres funciones financieras fundamentales con un sistema de pruebas completo que alcanza **100% de cobertura de código**.

## 🔧 Funciones Implementadas

### 1. `calculate_compound_interest(principal, rate, periods)`
Calcula el interés compuesto usando la fórmula: `A = P(1 + r)^n`

### 2. `calculate_annuity_payment(present_value, rate, periods)`
Calcula el pago de anualidad con la fórmula: `PMT = PV × [r(1 + r)^n] / [(1 + r)^n - 1]`

### 3. `calculate_internal_rate_of_return(cash_flows, iterations=100)`
Calcula la Tasa Interna de Retorno usando el método de Newton-Raphson

## 🚀 Cambios Realizados

### Fase 1: Corrección del archivo `finance.py`
**Problema inicial:** Solo 9 de las 17 pruebas pasaban
- ✅ **Corregí la función de interés compuesto** - Faltaba el exponente en la fórmula
- ✅ **Mejoré el manejo de casos especiales** - Agregué validaciones para tasa cero y períodos cero
- ✅ **Optimicé la función TIR** - Implementé mejor manejo de convergencia y casos edge
- ✅ **Añadí documentación completa** - Docstrings detallados para todas las funciones

### Fase 2: Creación del archivo `test_finance.py`
**Desafío:** Crear un sistema de pruebas robusto y completo
- 📝 **17 casos de prueba comprehensivos** cubriendo:
  - Casos normales y valores típicos
  - Casos extremos (tasas cero, períodos cero, valores negativos)
  - Validación de tipos de datos y firmas de funciones
  - Casos edge que podrían causar errores matemáticos

### Fase 3: Sistema de Coverage Avanzado
**Objetivo:** Implementar múltiples estrategias de medición de cobertura
- 🔍 **Triple sistema de fallback:**
  1. Coverage como módulo Python (método preferido)
  2. Coverage como CLI (comando externo)
  3. Pruebas simples sin coverage (respaldo)

## 📈 Resultados Finales

### ✅ Cobertura de Código: **100%**
```
Name         Stmts   Miss  Cover   Missing
------------------------------------------
finance.py      15      0   100%
------------------------------------------
TOTAL           15      0   100%
```

### ✅ Pruebas: **17/17 PASANDO**
- 🧪 **0 fallos**
- ⚠️ **0 errores**
- ⚡ **Ejecución en ~0.003 segundos**

## 🛠️ Características Técnicas

### Manejo Robusto de Errores
- Validación de entrada para todos los parámetros
- Manejo de casos donde la derivada es cero en TIR
- Protección contra divisiones por cero

### Configuración de Entorno
- Entorno virtual Python 3.13.5
- Dependencias: `coverage`, `unittest`
- Estructura de proyecto limpia y organizada

### Sistema de Pruebas Inteligente
- **Auto-detección** de disponibilidad de coverage
- **Múltiples estrategias** de ejecución
- **Reportes visuales** con indicadores claros de estado

## 📁 Estructura del Proyecto

```
HW-6/
├── finance.py              # Funciones financieras principales
├── tests/
│   └── test_finance.py     # Suite completa de pruebas
├── requirements.txt        # Dependencias del proyecto
├── pytest.ini            # Configuración de pytest
└── README.md              # Este archivo
```
