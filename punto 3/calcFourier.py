from antlr4 import *
from FourierLexer import FourierLexer
from FourierParser import FourierParser
import sympy as sp

def calcular_transformada(expr):
    # Definir las variables simbólicas
    t, w = sp.symbols('t w', real=True)
    
    # Convertir la expresión a una expresión simbólica
    expr = sp.sympify(expr)
    
    # Calcular la integral
    integral = sp.integrate(expr, (t, 0, sp.oo))
    
    # Simplificar la integral si es posible
    integral = sp.simplify(integral)
    
    return integral

# Leer la fórmula desde el archivo de texto
with open('formula.txt', 'r') as file:
    for line in file:
        expr = line.strip()
        # Calcular la Transformada de Fourier
        resultado = calcular_transformada(expr)
        print(resultado)
