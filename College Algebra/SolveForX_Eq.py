from sympy import *

x, y = symbols('x y')

# First equation set equal to zero, ready to solve
# first = 2*x + 10
first = 2*x + 10 - y

# Sympy syntax for equation equal to zero or any symbol, ready to factor
# eq1 = Eq(first,y)
eq1 = Eq(first,0)

# Sympy solve for x
sol = solve(eq1,x)

for s in sol:
    print("x =",s)
