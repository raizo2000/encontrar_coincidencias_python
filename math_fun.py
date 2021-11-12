'''
| Funciones suplementarias. 
'''


def power_set(name_list: list) -> None:
    '''
    | Calcula y devuelve el conjunto potencia del 
    | conjunto nombres de la lista.
    '''
    if len(name_list) == 0:
        return [[]]

    r = power_set(name_list[:-1])
    return r + [s + [name_list[-1]] for s in r]


def combinations(name_list: list, number: int) -> None:
    '''
    | Calcula y devuelve una lista con todas las
    | combinaciones posibles que se pueden hacer
    | con los elementos contenidos en name_list 
    | tomando un numero de elementos a la vez.
    '''
    return [s for s in power_set(name_list) if len(s) == number]


def counter_list(list_value) -> None:
    '''
    | Recibe una lista, y devuelve un diccionario 
    | con todas las repeticiones de
    | cada valor
    '''
    return {i: list_value.count(i) for i in list_value}
