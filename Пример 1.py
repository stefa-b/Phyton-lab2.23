# необходимо импортировать нужные модули. После этого объявить функцию func(), которая выводит пять раз сообщение с
# числовым маркером с задержкой в 500 мс. Далее создать объект класса Thread, в нем, через параметр target, указать,
# какую функцию запускать как поток и запустить его. В главном потоке добавить код вывода сообщений с интервалом
# в 1000 мс.

from threading import Thread
from time import sleep

if __name__ == "__main__":
    def func():
        for i in range(5):
             print(f"from child thread: {i}")
             sleep(0.5)
        th = Thread(target=func)
        th.start()
    for i in range(5):
        print(f"from main thread: {i}")
        sleep(1)