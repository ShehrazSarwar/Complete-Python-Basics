# If only import sympy then use sympy.factor() & sympy.symbols
from sympy import symbols,factor

x, y = symbols('x y')

# Equation set equal to zero, ready to solve
# eq = 2*x + 10*y + 4
eq = x**3 - 2*x**2 - 5*x + 6

print(factor(eq))