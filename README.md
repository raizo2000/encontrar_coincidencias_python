# Encontrar datos coincidentes con PYTHON

_El objetivo de este ejercicio es generar una tabla que contenga pares de empleados y la frecuencia con la que han coincidido en la oficina._

## Comenzando :frog:

_Para la resolución del ejercicio, se procedió a utilizar diccionarios y listas,_ 
_de tal manera que la data dentro del archivo **employees.txt** se convierta en_ 
_un diccionario, donde sus **KEYS** y sean equivalentes a cada Nombre de los empleados_ 
_y sus **VALUES** tomen cada uno de los días en los que laboraron._

```
Key: RENE          Values: ['MO10:00-12:00', 'TU10:00-12:00', 'TH01:00-03:00', 'SA14:00-18:00', 'SU20:00- 21:00']
Key: ASTRID        Values: ['MO10:00-12:00', 'TH12:00-14:00', 'SU20:00-21:00']
Key: ANDRES        Values: ['MO10:00-12:00', 'TH12:00-14:00', 'SU20:00-21:00']
Key: JOHANA        Values: ['MO10:00-12:00', 'TU10:00-12:00', 'SU20:00-21:00']
Key: ANGELA        Values: ['TU10:00-12:00', 'TH12:00-14:00', 'SA14:00-18:00']
Key: GABY          Values: ['TH12:00-14:00', 'SA14:00-18:00', 'SU20:00- 21:00']
..
```
_Con la Data limpia, extraemos las **KEYS** y comparamos los índices comunes,_ 
_para formar una nueva estructura que nos permitirá obtener la salida deseada:_

```
RENE-ASTRID   : 2
RENE-ANDRES   : 2
RENE-HERNAN   : 1
..
```

### Arquitectura 📋

_La arquitectura implementa busca organizar el código de tal manera que un usuario_
_en general solo deba ingresar la ruta de la data, para ello se aplica el parte del_ 
_patrón Iterator para traspasar los elementos necesarios y utilizar un método como_
_eje de todo el sistema._


## Enfoque y Metodología 📦

_El enfoque planteado para la resolución fue la manipulación de diccionarios e índices_ 
_que permitan filtrar la Data en la salida deseada, para ello se planteó de manera gráfica_ 
_como sería el tratamiento de los datos una vez obtenido el diccionario aplicando las bases_ 
_de la metodología Desing Thinking, ya que se obtuvo una secuencia de pasos conceptual._

```
input = {'aa':['q','w','a'],
         'bb':['a','z'],
         'cc':['q','w','z']
        }

{'a':['aa','bb'],
 'w':['aa','cc'],
 'q':['aa','cc'],
 'z':['bb','cc'],
}

{'a':['aa-bb'],
 'w':['aa-cc'],
 'q':['aa-cc'],
 'z':['bb-cc'],
}

output= {'aa,bb':1,'aa,cc':4,'bb,cc':2}
```

## Construido con 🛠️

_**Sistema desarrollado en Windows**_

_Debes tener instalado:_ 
```
Python 3.8.4 o superior.
```
### Ejecución 🔧


_Para ejecutar el sistema, debes entrar a la carpeta raíz, mediante tu consola **(CMD)**._
_**Ejemplo:**_
```
C:\ejercicio>
```
_Ejecutar el comando:_
```
python main.py
```
_El sistema procederá a ejecutarse._

```
C:\ejercicio>python main.py

RENE-ASTRID   : 2
RENE-ANDRES   : 2
RENE-HERNAN   : 1
RENE-JOHANA   : 2
RENE-ANGELA   : 2
RENE-GABY     : 1
ASTRID-ANDRES : 3
ASTRID-JOHANA : 1
ASTRID-ANGELA : 1
ASTRID-GABY   : 1
ANDRES-JOHANA : 1
ANDRES-ANGELA : 1
ANDRES-GABY   : 1
HERNAN-JOHANA : 1
HERNAN-ANGELA : 1
JOHANA-ANGELA : 1
ANGELA-GABY   : 2
```

## Autores ✒️

_Desarrollado por:_

* **Andrés Ricardo Guanoluisa Plasencia** - [raizo2000](https://gist.github.com/raizo2000)
---
⌨️ con ❤️ por [raizo2000](https://gist.github.com/raizo2000) :frog:
