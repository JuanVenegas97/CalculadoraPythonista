def logaritmo(a, base):
    if a > 0 and base > 0 and base != 1:
        return math.log(a, base)
    else:
        return "Error: Argumentos inválidos para el logaritmo"