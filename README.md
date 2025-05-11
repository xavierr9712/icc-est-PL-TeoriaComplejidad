# Práctica Teoria De La Complejidad

## 📌 Información General

- **Título:** Práctica Teoria De La Complejidad
- **Asignatura:** Estructura de Datos
- **Carrera:** Computación
- **Estudiantes:** Xavier Ortega, Dave Sigüenza
- **Fecha:** 11/5/2025
- **Profesor:** Ing. Pablo Torres

---

## 🛠️ Descripción

Este proyecto implementadiferentes algoritmos de ordenamiento en python, incluyendo:

- Método Burbuja
- Método Burbuja Mejorado
- Método Selección
- Método Inserción
- Método Shell

 Con estos estos metodos aplicamos el rendimiento y ejecucion con cada uno de los metodos.

## 🚀 Ejecución

Para ejecutar el proyecto:

1. Compila el código:
    ```bash
    python App.py
    ```
2. Ejecuta la aplicación:
    ```bash
    python App
    ```

## 🧑‍💻 Ejemplo

- Tamano: 5000, Algoritmo: bubble, Tiempo: 5.5144 segundos
- Tamano: 5000, Algoritmo: bubbleMejorado, Tiempo: 5.3468 segundos
- Tamano: 5000, Algoritmo: seleccion, Tiempo: 2.7478 segundos
- Tamano: 5000, Algoritmo: insercion, Tiempo: 2.5001 segundos
- Tamano: 5000, Algoritmo: shell, Tiempo: 0.0636 segundos
- Tamano: 10000, Algoritmo: bubble, Tiempo: 19.2417 segundos
- Tamano: 10000, Algoritmo: bubbleMejorado, Tiempo: 21.8693 segundos
- Tamano: 10000, Algoritmo: seleccion, Tiempo: 14.3431 segundos
- Tamano: 10000, Algoritmo: insercion, Tiempo: 10.5348 segundos
- Tamano: 10000, Algoritmo: shell, Tiempo: 0.1426 segundos
- Tamano: 30000, Algoritmo: bubble, Tiempo: 188.7330 segundos
- Tamano: 30000, Algoritmo: bubbleMejorado, Tiempo: 212.0724 segundos
- Tamano: 30000, Algoritmo: seleccion, Tiempo: 103.7407 segundos
- Tamano: 30000, Algoritmo: insercion, Tiempo: 97.8260 segundos
- Tamano: 30000, Algoritmo: shell, Tiempo: 0.5066 segundos
- Tamano: 50000, Algoritmo: bubble, Tiempo: 499.3565 segundos
- Tamano: 50000, Algoritmo: bubbleMejorado, Tiempo: 515.2262 segundos
- Tamano: 50000, Algoritmo: seleccion, Tiempo: 246.3416 segundos
- Tamano: 50000, Algoritmo: insercion, Tiempo: 250.7001 segundos
- Tamano: 50000, Algoritmo: shell, Tiempo: 0.9780 segundos
- Tamano: 100000, Algoritmo: bubble, Tiempo: 1958.9461 segundos
- Tamano: 100000, Algoritmo: bubbleMejorado, Tiempo: 2033.6539 segundos
- Tamano: 100000, Algoritmo: seleccion, Tiempo: 1008.3195 segundos
- Tamano: 100000, Algoritmo: insercion, Tiempo: 1032.7190 segundos
- Tamano: 100000, Algoritmo: shell, Tiempo: 2.1921 segundos

## EJEMPLO DE ADICIÓN DE DATOS EN ESTE INFORME

![alt text](<COMPARACION DE ALGORITMOS DE ORDENAMIENTO.png>)

## TABLA DE RESULTADOS TODOS LOS METODOS 

![alt text](<COMPARACION DE ALGORITMOS DE ORDENAMIENTO-.png>)

##  CONCLUCIONES CON TERMINOLOGIA DE NOTACION 

- A través del proceso de implementación, se adquirió una comprensión más profunda de los pasos de cada algoritmo de ordenación. Este conocimiento va más allá de simplemente conocer los algoritmos, ya que permite traducirlos a código funcional.
se identifica el algoritmo más eficiente en base al número de iteraciones.    
El análisis cuantitativo de los tiempos de ejecución permitió identificar claramente a Shell Sort como el algoritmo más eficiente entre los evaluados, especialmente para conjuntos de datos más grandes. Esto concuerda con la idea de que los algoritmos con menor complejidad temporal generalmente requieren menos operaciones (iteraciones) para ordenar un conjunto de datos determinado.

 - El ordenamiento de burbuja presento el peor rendimiento, con tiempos de ejecución que aumentaron a medida que aumentaba el tamaño de la matriz. Esto concuerda con su complejidad temporal de O(n^2), donde el número de operaciones escala cuadráticamente con el tamaño de la entrada

 - El ordenamiento de burbuja mejorado mostró cierta mejora al incorporar un mecanismo para terminar anticipadamente si no se producen intercambios en una pasada, lo que podría alcanzar O(n) en el mejor de los casos (datos ya ordenados). Sin embargo, su dificultad promedio y en el peor de los casos sigue siendo O(n^2), lo que limita su escalabilidad.

 - El ordenamiento por selección también mostró un comportamiento O(n^2), con un desempeño levemente mejor que el ordenamiento de burbuja en la mayoría de los casos, pero aún escalando deficientemente con entradas más grandes.

 - El ordenamiento por inserción, si bien tiene una difcultad en el peor de los casos de O(n^2), tuvo un rendimiento relativamente bueno con conjuntos de datos más pequeños. Esto probablemente se deba a su mejor rendimiento en el mejor de los casos de O(n) cuando la entrada está casi ordenada.

 - Shell Sort superó consistentemente a todos los demás algoritmos, especialmente al aumentar el tamaño de entrada. Este rendimiento superior se atribuye a su complejidad temporal, que es mejor que O(n^2), aunque la complejidad exacta depende de la secuencia de gaps utilizada

##  CONCLUCION XAVIER ORTEGA

 - El análisis de los tiempos de ejecución dio como resultado a Shell Sort como el algoritmo más eficiente entre los evaluados, especialmente para conjuntos de datos más grandes. Esto concuerda con la idea de que los algoritmos con menor complejidad temporal generalmente requieren menos operaciones (iteraciones) para ordenar un conjunto de datos determinado.

  ## CONCLUSIÓN DAVE SIGÜENZA
 - Luego de implementar y comparar distintos algoritmos de ordenamiento, se pudo comprobar que Shell Sort es el más eficiente para manejar grandes volúmenes de datos, mientras que métodos como Burbuja y Selección resultan poco prácticos por su alto costo en tiempo de ejecución.