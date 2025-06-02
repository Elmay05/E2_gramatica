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

# Implementación y pruebas
Ya que tenemos nuestra gramatica, realizamos nuestra implementación, Implemenatmos un programa en Pyhon que analiza las entradas (las oraciones) llamando a la función con alguna oración, de igual manera en este podremos encontrar pruebas automatizadas, si alguna prueba falla, imprime 'No se puede analizar', este programa lo puedes ver en el archivo de este repositorio

### Pruebas correctas
1. she is running in the park and He is sleeping in the cinema or You are eating near the school
2. you are sleeping behind the park
3. we are eating at the school
4. he is climbing on the house
5. she is thinking around the cinema
6. they are running by the school and we are sleeping
7. he is eating near the house or she is thinking at the school
8. it is climbing in the park and you are sleeping by the cinema or I am thinking on the school

### Pruebas incorrectas
1. I is running // Is no es parte de la gramatica para 'I'->am
2. They is sleeping // Is no es parte de la gramatica para 'They'->are 
3. We are eating the house // Le falta la preposicion 
4. She sleeping near the park //Le falta el verbo to be
5. He is near the park // Le falta la preposicion 
6. It is climbing in park // Le falta el articulo 'the'
7. You are //la oración está incompleta
8. Running in the school // Le falta el sujeto y el verbo to be

## Ejecutar el programa
Para ejecutar el programa hay 2 opciones, la primera es instalar Thonny si aún no lo ha echo, dercargue el archivo [grammartest.py](https://github.com/Elmay05/E2_gramatica/blob/main/grammartest.py), instale nltk en python y luego ejecute el programa.
Para instalarlo acceda a herramientas>administrar plugins y en la barra de busqueda escribir nltk, haz click en buscar e instalalo.
Si esto sigue sin funcionar, entra a herramientas>Abre el shell del sistema; y escribe: pip install nltk 
La segunda forma, y en caso de fallas, ejecute el programa aquí, está paso por paso:

[https://colab.research.google.com/drive/1lhAGX3vsNjjDJZiCJrH6ZVNm1FwJlgYx?usp=sharing](https://colab.research.google.com/drive/1lhAGX3vsNjjDJZiCJrH6ZVNm1FwJlgYx?usp=sharing)

Al ejecutar el programa, la salida mostrará los arboles analizados para las pruebas exitosas y el mensaje de error para las pruebas fallidas pero que contienen la gramatica anteriormente mencionada.
![image](https://github.com/user-attachments/assets/7cbf9a8e-bcde-41b8-a16c-da35ed3a73fa)

# Analisis
En este proyecto implementamos un analizador sintactico capaz de detectar si alguna de las oraciones se encuentra en una estructura gramatical predefinida, en nuestro caso, implementando el idioma ingles con presente continuo.
Ahora, segun wikipedia, "La jerarquía de Chomsky  es una clasificación jerárquica de distintos tipos de gramáticas formales que generan lenguajes formales. Esta jerarquía fue descrita por Noam Chomsky en 1956"
[liga](https://es.wikipedia.org/wiki/Jerarqu%C3%ADa_de_Chomsky)

Esta jerarquia consta de 4 niveles:
* Tipo 0 Indecidible: gramaticas sin restricciones (recursivamente enumeradas) esta incluye las gramaticas formales, genera todos los lenguajes reconocidos por una maquina de Turning
* Tipo 1 NP-Completo: Generan los lenguajes sensibles al contexto, los lenguajes descritos en estas gramaticas son todos los reconocidos por una maquina de Turning determinista, con cinta de memoria acortada por un cierto número entero de veces sobre la longitud de entrada (autómatas linealmente acotados
* Tipo 2 O(n^3): Gramatiacas libres de contexto, generan lenguajes independientes del contexto, estos lenguajes pueden ser reconocidos por un autómata con pila.
* Tipo 3 O(n): Gramáticas regulares, generan los lengujajes regulares, son los que pueden ser aceptados por un auómata finito, estos lenguajes se debe optener por medio de expresiones regulares.

Dado que ambas gramaticas con libres de contexto, ambas pertenecen al nivel tipo 2, esto se debe a que en todas las reglas de producción, el lado izquierdo es el único simbolo no terminal
### Gramatica con ambiguedad y recursion derecha
Esta surge por la forma en qeu se definen las operaciónes 'and' y 'or' en la regla O -> O 'and' O | O 'or' O permitiendo varios arboles de derivación para una misma cadena
### Gramatica sin ambiguedad
Esta se consigue al agregar nos no terminales (T, F, Oa, Ta) forazando una precedencia y asociatividad específica para los operadores 'and' y 'or'.

### Complejidad asintotica
Gracias a que ambas pertenecen al campo "libre de contexto", segun la jerarquia de Chomsky, estas tienen una complejidad asintotica de O(n^3).
Es importante mencionar que la gramatica sin ambigüedad, al tener una estructura que clarifica la prodecendia y asociatividad, es mas adecuada para los tipos de parsers LL o LR, pudiendo lograr una complejidad asintotica de O(n), eliminar la ambigüedad es un paso importante para poder construir este ipo de parsers deterministas y eficientes

# Bibliografias
(inglés, sa). Rae.es. Recuperado el 25 de abril de 2025, de https://dle.rae.es/ingl%C3%A9s

colaboradores de Wikipedia. (2024, 29 noviembre). Jerarquía de Chomsky. Wikipedia, la Enciclopedia Libre. https://es.wikipedia.org/wiki/Jerarqu%C3%ADa_de_Chomsky


