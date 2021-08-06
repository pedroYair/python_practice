"""
    https://unipython.com/uso-de-expresiones-regulares-en-python/
    https://docs.python.org/es/3/library/re.html

    blanco|negro = blanco o negro

    ? = una o ninguna aparicion
    pedro? = pedr o pedro

    + = 1 o muchas apariciones
    pedro+ = pedro o pedrooooo

    * = ninguna o muchas veces
    p*edro = edro o ppppedro

    {n} = permite indicar la cantidad de veces que debe aparecer el caracter

    {n1, n2} = apariciones desde n1 hasta n2

    {, n} = apariciones desde 0 hasta n

    {n, } = apariciones desde n en adelante

    --------------------------------------------------
    AGRUPACION

    () = operador de grupo
    (p|m)adre = padre o madre
    (sub)?marino: submarino o marino

    []: representa clases de caracteres; es decir los agrupa en clases
    acci[oó]n encontrará “accion” o “acción”

    ---------------------------------------------------
    . representa cualquier caracter a excepcion de \n

    Caracteres predefinidos

    \d Cualquier carácter que sea dígito

    \D Cualquier carácter que no sea dígito

    \w Cualquier carácter alfanumérico

    \W Cualquier carácter no alfanumérico

    \s Espacio en blanco

    \S Cualquier carácter que no sea espacio



"""

