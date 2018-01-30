#Quadratic Equation
import math

def solve_quadratic(a, b, c):
    discRoot = math.sqrt(b * b - 4 * a * c)
    x1 = (-b + discRoot) / (2 * a)
    x2 = (-b - discRoot) / (2 * a)
    print("The solution is: x=", x1, "and x=", x2)

solve_quadratic(2, 3, -4.5)
