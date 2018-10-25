par = []
impar = []
inter = []


def f(x):
    """
    Dado un punto 'x', evalua la función.
    :param x: Punto a evaluar.
    :return: Valor numérico de la función en el punto dado.
    """
    return x/((x + 1)*(x + 2))


def divinter(a, b, n):
    """
    Dado el límite inferior y superior de un intervalo divide este en 'n' segmentos iguales.
    :param a: Límite inferior.
    :param b: Límite superior.
    :param n: Cantidad de segmentos.
    :return: None.
    """
    ha = h(a, b, n)
    inter.append(a)
    for i in range(n):
        inter.append(inter[len(inter) - 1] + ha)


def h(a, b, n):
    """
    Dado los valores de 'a', 'b' y 'n', evalua la función 'h'.
    :param a: Límite inferior.
    :param b: Límite superior
    :param n: Cantidad de subintervalor.
    :return: Diferencia de el superior al inferior dividido entre dos.
    """
    return (b - a)/n


def detimpar(n):
    """
    Dado un número 'n', genera una lista de 'n' números impares.
    :param n: Cantidad de números impares.
    :return: None.
    """
    impar.append(1)
    for i in range(int(n/2) - 1):
        impar.append(impar[len(impar) - 1] + 2)


def detpar(n):
    """
    Dado un número 'n', genera una lista de 'n' números pares.
    :param n: Cantiadd de números pares.
    :return: None.
    """
    par.append(2)
    for i in range(int(n/2) - 1):
        par.append(par[len(par) - 1] + 2)


def simpsonsimple(a, b):
    """
    Método de Simpson simple
    :param a: Límite inferior.
    :param b: Límite superior
    :return: Valor de la aproximación de la integral.
    """
    xm = (a + b)/2
    return (h(a, b, 2)/3)*(f(a) + 4*f(xm) + f(b))


def simpsoncompound(a, b, n):
    """
    Método de Simpson compuesto.
    :param a: Límite inferior.
    :param b: Límite superior
    :param n: Cantidad de subintervalor.
    :return: Valor de la aproximación de la integral.
    """
    detimpar(n)
    detpar(n)
    divinter(a, b, n)
    e = 0
    p = 0
    for i in range(int(n/2)):
        e = e + f(inter[impar[i]])
    for j in range(int(n/2) - 1):
        p = p + f(inter[par[j]])
    return ((h(a, b, n))/3)*(f(a) + 4*e + 2*p + f(b))
