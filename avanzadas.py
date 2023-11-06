def seno(a,t):
    if t == 'R':
        return math.sin(float(a))
    else:
        return math.sin(math.radians(float(a)))