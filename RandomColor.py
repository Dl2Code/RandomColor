from random import randint


def getcolor(n):
    
    colors = []
    for _ in range(n):
        value = lambda: randint(0, 255)
        colors.append('#%02X%02X%02X' % (value(), value(), value()))
    
    return colors
