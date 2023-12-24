# С использованием многопоточности для заданного значения x найти сумму ряда S с точностью члена ряда по абсолютному
# значению ε=10-7 и произвести сравнение полученной суммы с контрольным значением функции для двух бесконечных рядов.

import threading
import math

class SeriesThread(threading.Thread):
    def __init__(self, x, epsilon):
        threading.Thread.__init__(self)  # Инициализация объекта потока
        self.x = x # Значение x для ряда
        self.epsilon = epsilon # Заданная точность для вычислений
        self.result = 0 # Инициализация переменной для хранения суммы ряда

    def run(self):
        n = 0  # Инициализация переменной n (степень в ряде)
        term = (self.x ** (n))  # Вычисление первого члена ряда

        # Вычисление суммы ряда до достижения заданной точности epsilon
        while abs(term) > self.epsilon:
            self.result += term
            n += 1
            term = (self.x ** ( n))

def main():
    x = 0,7
    epsilon = 1e-7

    # Задаем контрольное значение
    control_value = 1/(1-x)

    # Создаем поток для вычисления суммы ряда
    series_thread = SeriesThread(x, epsilon)

    # Запускаем поток
    series_thread.start()

    # Ждем завершения потока
    series_thread.join()

    # Получаем результат
    series_sum = series_thread.result

    # Сравниваем результат с контрольным значением
    if abs(series_sum - control_value) < epsilon:
        print(f"Сумма ряда: {series_sum}")
        print(f"Контрольное значение: {control_value}")
        print("Результат совпадает с контрольным значением.")
    else:
        print("Результат не совпадает с контрольным значением.")

if __name__ == "__main__":
    main()