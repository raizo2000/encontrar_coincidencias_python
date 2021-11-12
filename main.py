'''
| @Autor: Ricardo Plasencia
| La empresa ACME ofrece a sus empleados la flexibilidad de trabajar 
| las horas que deseen. Pero debido a algunas circunstancias externas, 
| necesitan saber qué empleados han estado en la oficina dentro del 
| mismo período de tiempo.
| El objetivo de este ejercicio es generar una tabla que contenga pares 
| de empleados y la frecuencia con la que han coincidido en la oficina.
'''

from math_fun import combinations, counter_list


class Archive:
    def call_archive(self, route: str) -> None:
        '''
        | Llama a la data y la comvierto en
        | en un diccionario, utilizando un
        | gestor de contexto.
        '''
        employee_dic = {}
        with open(route) as file_object:
            for employee in file_object:
                values = employee.split("=", 1)
                employee_dic[values[0].strip()] = values[1].strip()
        '''
        | Divide los Values del diccionario 
        | por ",".
        '''
        employee_fl = {
            key: list(
                map(str, value.split(","))
            ) for key, value in employee_dic.items()
        }

        return employee_fl

    def clear_dicctionary(self, dicionary: dict) -> None:
        '''
        | Llama al diccionario generado
        | y limpia los valores no repetidos de cada
        | Value.
        '''

        '''
        | Obtiene tolos los values y Keys en una lista
        '''
        duplicate_val = [item for sublist in dicionary.values()
                         for item in sublist]
        dups = []

        for i in duplicate_val:
            if duplicate_val.count(i) > 1:
                dups.append(i)

        duplicate_val = set(dups)

        '''
        | new_d -> Mantiene solo los elementos duplicados.
        '''
        new_d = {}
        name = []
        for key, values in dicionary.items():
            for value in values:
                if value in duplicate_val:
                    new_d.setdefault(key, []).append(value)
                    name.append(new_d)

        return new_d

    def employee_matches(self, dictionary: dict) -> None:
        '''
        | Utiliza un diccionario y su copia para comparar
        | los values e ir agrupando cada una de las Keys 
        | coincidentes en una nueva lista.
        '''
        keys = dictionary.keys()
        name = combinations(list(keys), 2)
        it = dictionary.items()
        it_copy = dictionary.items()
        matches = []
        for i, i_values in it:
            for j, j_values in it_copy:
                if(i == j):
                    continue
                if([i, j] in name):
                    for ind_i in range(0, len(i_values)):
                        for ind_j in range(0, len(j_values)):
                            if(i_values[ind_i] == j_values[ind_j]):
                                result = {
                                    "Names": i+"-"+j
                                }
                                matches.append(result)
                                break
        return matches

    def counter_elements(self, list_data: list) -> None:
        '''
        | Llama una lista para agrupar y contar 
        | los datos similares.
        '''
        list_resutl = []
        for n in list_data:
            list_resutl.append(n["Names"])
        filter_data = counter_list(list_resutl)

        for key, value in filter_data.items():
            print(key+' '*(13-len(key)), ':', value)


class Operations:
    def match_classifier(self, route: str) -> None:
        '''
        | Concadena las diversas funciones.
        '''
        archive = Archive()
        first_filter = archive.call_archive(route)
        second_filter = archive.clear_dicctionary(first_filter)
        third_filter = archive.employee_matches(second_filter)
        archive.counter_elements(third_filter)


if __name__ == "__main__":
    employes_route = 'files/employees.txt'
    operation = Operations()
    operation.match_classifier(employes_route)
