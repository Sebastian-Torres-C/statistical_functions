import math
import numpy as np

def media(array):
    """Calcula la media de un array, si no contiene valores validos
    retorna NaN.
    
    Retorna el resultado como un float.
    
    Si el array esta vacio, retornara NaN"""

    suma = 0

    try:
        if len(array) == 0:
            return np.nan
        for n in array:
            suma += n
    except TypeError:
        return np.nan

    return suma / len(array)

def mediana(array):
    """Calcula la mediana de un array, si no contiene valores validos
    retorna NaN. 
    
    Retorna el resultado como un float.
    
    Si el array esta vacio, retornara NaN"""

    try:
        array_ordenado = sorted(array)
    except TypeError:
        return np.nan

    n = len(array_ordenado)

    if n == 0:
        return np.nan

    mitad = n // 2

    if n % 2 == 0:
        mediana = float((array_ordenado[mitad - 1] + array_ordenado[mitad]) / 2)
    else:
        mediana = array_ordenado[mitad]

    return float(mediana)

def moda(array):
    """Calcula la moda de un array, si no contienen
    valores validos retorna NaN. 
    
    Retorna el resultado como dos arrays, el primero con las modas 
    y el segundo con sus frecuencias.
    
    Si alguno de los arrays esta vacio o si no comparten la misma cantidad de
    elementos, retornara NaN"""
    
    try:
        frecuencia = {}
        for n in array:
            if n in frecuencia:
                frecuencia[n] += 1
            else:
                frecuencia[n] = 1
    except TypeError:
        return np.nan

    if len(frecuencia) == 0:
        return np.nan

    max_numero = max(frecuencia.values())
    frecuencias_maximas = {}
    for key, value in frecuencia.items():
        if value == max_numero:
            frecuencias_maximas[key] = value
    array1 = []
    array2 = []
    for key in frecuencias_maximas.keys():
        array1.append(key)
    array2.append(max_numero)
    array1 = np.array(array1)
    array2 = np.array(array2)
    return array1, array2

def rango(array):
    """Calcula el rango de un array, si no contiene valores validos
    retorna NaN. 
    
    Retorna el resultado como un float.
    
    Si el array esta vacio, retornara NaN"""

    try:
        minimo = min(array)
        maximo = max(array)
    except (TypeError, ValueError):
        return np.nan
    
    if len(array) == 0:
        return np.nan

    return float(maximo - minimo)

def desviacion_estandar(array):
    """Calcula la desviacion estandar de un array, si no contiene valores validos
    retorna NaN.

    Retorna el resultado como un float.
    
    Si el array esta vacio, retornara NaN"""

    try:
        n = len(array)
        if n == 0:
            return np.nan
        media_valor = media(array)
        suma_cuadrados = 0
        for x in array:
            suma_cuadrados += (x - media_valor) ** 2
        desviacion = math.sqrt(suma_cuadrados / n)
    except TypeError:
        return np.nan

    return float(desviacion)

def desviacion_media_absoluta(array):
    """Calcula la desviacion media de un array, si no contiene valores validos
    retorna NaN. 
    
    Retorna el resultado como un float.
    
    Si el array esta vacio, retornara NaN"""

    try:
        n = len(array)
        if n == 0:
            return np.nan
        media_valor = media(array)
        suma_diferencias = 0
        for x in array:
            suma_diferencias += abs(x - media_valor)
        desviacion_media = suma_diferencias / n
    except TypeError:
        return np.nan

    return float(desviacion_media)

def varianza(array):
    """Calcula la varianza de un array, si no contiene valores validos
    retorna NaN. 
    
    Retorna el resultado como un float.
    
    Si el array esta vacio, retornara NaN"""

    try:
        n = len(array)
        if n == 0: 
            return np.nan
        media_valor = media(array)
        suma_cuadrados = 0
        for x in array:
            suma_cuadrados += (x - media_valor) ** 2
        varianza = suma_cuadrados / n
    except TypeError:
        return np.nan

    return float(varianza)

def percentil(array, percentil):
    """Calcula el percentil entregado en un array, si no contiene valores validos
    retorna NaN. 
    
    Retorna el resultado como un float.
    
    Si el array esta vacio, retornara NaN"""

    try:
        array_ordenado = sorted(array)
    except TypeError:
        return np.nan

    n = len(array_ordenado)

    if n == 0:
        return np.nan

    k = (n) * (percentil / 100)
    if k != int(k):
        return float((array_ordenado[int(k)]+array_ordenado[int(k)+1])/2)
    else:
        return float(array_ordenado[int(k)])
    
def rango_intercuartil(array):
    """Calcula el rango intercuartil de un array, si no contiene valores validos
    retorna NaN. 
    
    Retorna el resultado como un float.
    
    Si el array esta vacio, retornara NaN"""

    try:
        q1 = percentil(array, 25)
        q3 = percentil(array, 75)
        if len(array) == 0:
            return np.nan
        rango_intercuartil = q3 - q1
    except TypeError:
        return np.nan

    return float(rango_intercuartil)

def covarianza(array_x, array_y):
    """Calcula la covarianza entre dos arrays, si no contienen valores validos
    retorna NaN. 
    
    Retorna el resultado como un float.
    
    Si alguno de los arrays esta vacio o si no comparten la misma cantidad de
    elementos, retornara NaN"""

    try:
        n = len(array_x)
        if n == 0 or len(array_y) == 0 or n != len(array_y):
            return np.nan
        media_x = media(array_x)
        media_y = media(array_y)
        suma_total = 0
        for i in range(n):
            suma_total += (array_x[i] - media_x) * (array_y[i] - media_y)
        covarianza = suma_total / n
    except TypeError:
        return np.nan

    return float(covarianza)

def correlacion(array_x, array_y):
    """Calcula el coeficiente de correlacion entre dos arrays, si no contienen
    valores validos retorna NaN. 
    
    Retorna el resultado como un float.
    
    Si alguno de los arrays esta vacio o si no comparten la misma cantidad de
    elementos, retornara NaN"""

    try:
        n = len(array_x)
        if n == 0 or len(array_y) == 0 or n != len(array_y):
            return np.nan
        desviacion_x = desviacion_estandar(array_x)
        desviacion_y = desviacion_estandar(array_y)
        if desviacion_x == 0 or desviacion_y == 0:
            return np.nan
        covar = covarianza(array_x, array_y)
        correlacion = covar / (desviacion_x * desviacion_y)
    except TypeError:
        return np.nan

    return float(correlacion)

def freedman_and_diaconis(array):
    """Calcula el número de bins usando la regla de Freedman & Diaconis.

    Devuelve un entero con el número de bins o `np.nan` si la
    entrada no es válida.
    """

    try:
        n = len(array)
        if n == 0:
            return np.nan

        iqr = rango_intercuartil(array)
        if np.isnan(iqr) or iqr == 0:
            return np.nan

        # ancho de bin utilizando la formula de freedman & diaconis
        h = 2 * iqr / (n ** (1/3))
        rango_total = rango(array)

        if h <= 0 or rango_total == 0 or np.isnan(rango_total):
            return 1

        bins = rango_total / h
        bins_enteros = int(bins)

        # Redondeo al entero más cercano
        if bins - bins_enteros >= 0.5:
            bins_final = bins_enteros + 1
        else:
            bins_final = bins_enteros

        if bins_final < 1:
            bins_final = 1
        return int(bins_final)
    except TypeError:
        return np.nan
