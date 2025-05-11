import random

import matplotlib.pyplot as plt

from SortMethods import SortMethods
from Benchmarking import Benchmarking


class App:

    def __init__(self):
        self.tamanos = [5000, 10000, 30000, 50000, 100000]  # Array sizes [cite: 5]
        self.max_tamano = max(self.tamanos)
        self.arreglo_base = self.build_arreglo(self.max_tamano)  # Base array
        self.algoritmos = {
            "bubble": SortMethods().sort_bubble,
            "bubbleMejorado": SortMethods().sort_bubble_optimized,
            "seleccion": SortMethods().sort_selection,
            "insercion": SortMethods().sort_insertion,
            "shell": SortMethods().sort_shell
        }
        self.resultados = []
        self.benchmarking = Benchmarking()

    def build_arreglo(self, tamano: int) -> list[int]:
        """Genera una lista de números enteros aleatorios."""

        return [random.randint(0, tamano) for _ in range(tamano)]  # Generate random numbers

    def run(self):
        """
        Ejecuta los algoritmos de clasificación para cada tamaño de matriz y almacena los resultados.
        """

        for tamano in self.tamanos:
            arr = self.arreglo_base[:tamano].copy()  # Get the first 'tamano' elements [cite: 6]

            for nombre, algoritmo in self.algoritmos.items():
                tiempo = self.benchmarking.medir_tiempo(algoritmo, arr.copy())  # Time the execution [cite: 5]
                self.resultados.append((tamano, nombre, tiempo))
                print(f"Tamano: {tamano}, Algoritmo: {nombre}, Tiempo: {tiempo:.4f} segundos")  # Output to console [cite: 18]

    def graficar_resultados(self):
         """
         Grafica los resultados usando matplotlib.
         """
         tiempos = {}
         for tamano in self.tamanos:
            tiempos[tamano] = {nombre: [] for nombre in self.algoritmos}

         for tamano, nombre, tiempo in self.resultados:
            tiempos[tamano][nombre].append(tiempo)

         plt.figure(figsize=(10, 6))

         for nombre in self.algoritmos:
            plt.plot(self.tamanos, [sum(tiempos[tamano][nombre]) / len(tiempos[tamano][nombre]) for tamano in self.tamanos], marker='o', label=nombre)

         plt.xlabel('Tamaño del arreglo')
         plt.ylabel('Tiempo de ejecución (s)')
         plt.title('Comparación de algoritmos de ordenamiento')
         plt.legend()
         plt.grid(True)
         plt.show()

if __name__ == "__main__":
    app = App()
    app.run()
    app.graficar_resultados()