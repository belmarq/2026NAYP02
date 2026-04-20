def suma(a,b):
    '''Suma dos números a y b'''
    return a + b

def incremento(a, incremento=1):
    '''Incrementa el valor de a por un valor dado (por defecto 1)'''
    return a + incremento
    
a = 2
b = 4
print(f"Suma: {suma(a,b)}")
print(f"Incremento: {incremento(a,2)}")