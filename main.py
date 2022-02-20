import math

def value_check():
    a = float(input('Input paramenter "a":\n '))
    if a == 0:
        print('Impossible to solve! Value "a" cannot be 0.\n')
        value_check()
        return 

    b = float(input('Input paramenter "b":\n '))
    c = float(input('Input paramenter "c":\n '))
    return equation_solver(a, b, c)

def equation_solver(a, b, c):
    root1 = 0
    root2 = 0

    print("The equation looks like this:", f"{a}*x^2 + ({b})*x + ({c}') = 0. Checking distcriminant...\n")

    disrciminant = b * b - (4 * a * c)
    if disrciminant < 0:
        print('No roots.\n')
    elif disrciminant == 0:
        print("D = 0, hence only one root exists\n")
    else:
        print('Two roots exist. Calculating...\n')
    
    root1 = (-b + math.sqrt(disrciminant)) / (2 * a)
    root2 = (-b - math.sqrt(disrciminant)) / (2 * a)

    if root1 == root2:
        print('roots are: only one root: ', root1)
    else:
        print('roots are: root #1: ', root1, 'root #2: ', root2)
        return 0


if __name__ == '__main__':
    value_check()
