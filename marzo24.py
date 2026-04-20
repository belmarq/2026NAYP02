def suma( *args, **kwargs):
    '''Suma dos números a y b'''
    print( sum(args) + sum(kwargs.values()) )

suma(2, 4, **{"a": 3, "b": 5})