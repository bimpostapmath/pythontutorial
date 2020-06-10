from sympy import *
x, y, z = symbols('x y z')

# Subtitution 

expr= cos(x)+1
print(expr)
expr=expr.subs(x,y)
print(expr)
# even with numbers
expr=expr.subs(y,0)
print(expr)

# Plug in numebrs after converting the strings to expressions

str_expr="x**2+3*x+2*x-5"
# It is like the eval function
expr=sympify(str_expr)
print(expr)
expr.subs(x,2)

# evalf, print numercal expression

expr=sqrt(8)
# Right now it only prints out 2*sqrt(2)
print(expr)
print(expr.evalf())

# Now you don't have to memorize pi
print(pi.evalf(100))
expr = sin(2*x)+x
print(expr.evalf(subs={x:2.2}))
one = cos(1)**2 + sin(1)**2
# Error happens!
print((one - 1).evalf())
# Avoid the small error
(one - 1).evalf(chop=True)

import numpy
a = numpy.arange(10)
expr = sin(x)
# numpy here means using the numpy library
f = lambdify(x, expr, "numpy")
print(f(a))
