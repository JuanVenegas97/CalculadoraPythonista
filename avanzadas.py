def tangente(a,t):
    if t == 'R':
        return math.tan(float(a))
    else:
        return math.tan(math.radians(float(a)))