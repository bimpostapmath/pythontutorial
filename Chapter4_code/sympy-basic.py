from __future__ import division
from sympy import *
# Initialize symbols, either one or more
a=symbols('x')
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
# Print Pretty things
init_printing()
# Printing Polynomials
print(x+1)
print(Integral(sqrt(1/x),x))
# Relationship
print(True^False)
print(True^True)
