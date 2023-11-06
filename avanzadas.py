def atangente(f_t,t):
    if t == 'R':
        return math.atan(float(f_t))
    else:
        return math.atan(float(f_t))*180/(math.pi)

