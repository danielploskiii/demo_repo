"""
Prosty program obliczający pierwiastki równania kwadratowego.
"""

import math

A = 3
B = 8
C = 1

DELTA = B**2 - 4 * A * C

if DELTA < 0:
    print("Brak rozwiązań")
elif DELTA == 0:
    X0 = -B / (2 * A)
    print("Jedno rozwiązanie równe:", X0)
else:
    pierwiastek = math.sqrt(DELTA)
    X1 = (-B - pierwiastek) / (2 * A)
    X2 = (-B + pierwiastek) / (2 * A)
    print("Dwa rozwiązania równe:", X1, X2)
