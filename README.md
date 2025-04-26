# E2_gramatica
Omar Emilio Casillas Alday - A01712114
# Descripción
El idioma que elegí es el inglés, que, según  dle rae, esta es una lengua germánica occidental que se habla como lengua materna en muchas partes de Oceanía, África, Asia, el Reino Unido, Irlanda y América del Norte, este se usa como lenguaje de comunicación en todo el mundo
https://dle.rae.es/ingl%C3%A9s 

## Estructura del lenguaje
El ingles es un idioma con variedad de reglas gramaticales estructuradas. Sin embargo, para simplificar la gramatica se analizarán oraciones en presente continuo afirmativo.
El presente coninuo del ingles se utiliza para describir acciones que están ocurriendo en el momento en que se habla o para planes a futuros ya decididos, esta se forma con el verbo "to be" segun sea el pronombre:

* I 'AM'
* You 'ARE'
* He 'IS'
* She 'IS'
* It 'IS'
* We 'ARE'
* You 'ARE'
* They 'ARE'

Despues se agrega el verbo principal con la terminación -ing

Afirmativa:
Sujeto + am/is/are + verbo principal + -ing. 

Negativa:
Sujeto + am/is/are + not + verbo principal + -ing. 

Interrogativa:
am/is/are + Sujeto + verbo principal + -ing?. 

Para la implementación de esta solución, vamos a utilizar un analizador LL(1), este es un analizador sinácico descendente, no requiere la implementación de retroceso, para utilizarla ocupamos formatear la gramática para que pueda considerarse determinista.

# Modelos
Comenzamos construyendo una gramática adecuada ya que esta es funcamental para un análisis exitoso, para lograrlo ocuparemos nuestros primeros 3 pasos;
* Crear una gramatica
* Eliminar ambigüedad
* Eliminar recursión izquierda

### Crear una gramatica
En esta fase se identifican las unidades sintacticas básicas y las reglas que rigen la formación de oraciones, en este caso se definieron:
* Una manera de juntar oraciones
* Pronombres con sus respectivos verbos to-be
* Verbos con ing
* Preposiciones
* Lugares
* La conjuncion de preposiciones y lugares
  
![image](https://github.com/user-attachments/assets/86b3f6ba-8ece-4430-8526-df88f12375cf)
Esta gramatica tiene un detalle, el cual es que para una oración, puedes crear varios arboles demostrando que es una gramatica ambigüa
![image](https://github.com/user-attachments/assets/3ac77876-281a-4c9a-babf-18197f3122c0)


### Eliminar ambigüedad
Para lograr eliminar la ambigüedad, ocupamos añadir estados intermedios y producciones que indiquen precedencia, esto para eliminar el "o" (por aquí o por aquí) entre estados equivalentes.
![image](https://github.com/user-attachments/assets/f5a13f4b-5bd8-4f4c-9d25-0a838d8e2904)
De esta manera, para una oración, ya crece solo por un lado del arobl evitando tener 2 tipos diferentes de arboles, aunque aún tenemos un problema el cual es la resursividad izquierda.
![image](https://github.com/user-attachments/assets/454fea64-b56c-4f26-a016-b981a30349f7)


### Eliminar recursividad izquierda
Este punto es importante, eso principalmente por que la forma en que los parsers procesan el lenguaje es definido por esa gramática, en nuestro caso el LL, este analizador descentente comienza por el simbolo inicial de la gramática e inenta derivar la cadena de entrada expandiendo los no terminales según las reglas de producción, se puede crear una llamada recursiva infinita haciendo que el parser intente expandir los no terminales indefinidamente sin consumir ninguna parte de la entrada, de igual manera ayuda al parser a tomar desiciones deterministas sobre qué producción aplicar basándose en el siguiente símbolo de entrada.
![image](https://github.com/user-attachments/assets/0f3099c9-f9cd-4f15-a502-93e8ffe91917)

De esta manera, por el lado izquierdo siempre encontrará los elementos terminales, mientras que del lado derecho irán saliendo los no terminales hasta terminar con la oración se corta con un emptu ε.
![image](https://github.com/user-attachments/assets/b8136bc9-7aed-4251-aacf-75f885167ca6)

### Primer y siguiente estado
Para finalizar, realizamos nuesta tabla de primer y siguiente estado para preparar la construcción del parser, First ayuda cuando tienes un no terminal y quieres saber que producción usar, comparas el token de entrada con los conjuntos de First de cada producción, si la entrada está aquí, la usas, Follow ayuda cuando en el no terminal se encuentra vacio (ε) en el First, si es el caso, usas estos.
![image](https://github.com/user-attachments/assets/04b2a6ba-4eff-4c13-bcf1-bb0c34dd7077)

Ahora ya podemos construir la matriz con este First y Follow, esta es como el 'cerebro' del parser, se compone de Filas=No terminales y de Columnas=Terminales en cada celda decides que producción aplicar dependiendo del no terminal actual y el token de entrada.

La matriz para esta evidencia está un poco grande que en foto no se podrá apreciar muy bien, pero puedes consultarlo en este archivo[Estados y transiciones.xlsx
](https://github.com/Elmay05/E2_gramatica/blob/main/Estados%20y%20transiciones.xlsx)

# Implementación


# Pruebas


# Analisis



# Bibliografias
(inglés, sa). Rae.es. Recuperado el 25 de abril de 2025, de https://dle.rae.es/ingl%C3%A9s

