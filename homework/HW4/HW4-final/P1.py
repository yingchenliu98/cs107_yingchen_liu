# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
def numerical_diff(f,h):
    def diff(x):
        return (f( x + h ) - f( x )) / h
    return diff

print("Answer to Q-a:")
a1 = "h=1e-7 most closely approximates the true derivative. When h is too small, "+\
    "f(x+h) and f(x) will be almost the same. Due to round-off error, "+\
        "it may lead to catastrophic cancellation and stability problems as shown in the following plot."
a2 = "When h is large, the numerical approximation is not exact. The round-off error will decrease, but the truncation error will increase."+\
    "The truncation error is the error made by truncating an infinite sum and approximating it by a finite sum."+\
        "It leads to a less accurate approximation to the derivative."
print(a1, a2)
print("Answer to Q-b:")

b = "Automatic differentiation is able to reduce the function to a composite of "+\
    "primitives function like log, sin, cos, exp with arithmetic operations such "+\
        "as +,-,*,/. This step can break down a complex function into less complex ones."+\
            "It then uses chain rule to repeatedly calculating the derivatives and combines "+\
                "to get the derivative of the entire function."+\
                    "Automatic differentiation can avoid the problems by evaluating"+\
                       "derivatives exactly to machine precision without taking numerical estimates."
print(b)
    
f = lambda x: np.log(x)
f_d = lambda x: 1/x
hs = [1e-1, 1e-7, 1e-15]
x_sample = np.linspace(0.2,0.4)

plt.figure()
plt.plot(x_sample, f_d(x_sample), label='exact derivative', c='#bcbd22',  lw=7, alpha=0.5)
for h in hs:
    fd = numerical_diff(f, h)
    plt.plot(x_sample, fd(x_sample),label="$f'_{{FD}}(x)$ for h= {:.0e}".format(h))
plt.title('Plot to Compare the Finite Difference to \nthe True Derivative at different stepsize(h)')
plt.xlabel("x")
plt.ylabel("derivatives of f at x")
plt.legend()
plt.show()   
    
    
