import time


class Benchmarking:

    def medir_tiempo(self, func, array: list[int]) -> float:
        start_time = time.time()
        func(array)  
        end_time = time.time()
        return end_time - start_time
