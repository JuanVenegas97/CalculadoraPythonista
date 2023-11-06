def arcocoseno(f_t,t):
    if t == 'R':
        return math.acos(float(f_t))
    else:
        return math.acos(float(f_t))*180/(math.pi)
