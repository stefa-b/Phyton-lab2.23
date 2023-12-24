# есть такая разновидность потоков, которые называются демоны. Python приложение не будет закрыто до тех пор, пока в
# нем работает хотя бы один недемонический поток. Для того, чтобы потоки не мешали остановке приложения (т.е. чтобы они
# останавливались вместе с завершением работы программы) необходимо при создании объекта Thread аргументу daemon
# присвоить значение True, либо после создания потока, перед его запуском присвоить свойству deamon значение True.

from threading import Thread
from time import sleep

if __name__ == "__main__":
    def func():
        for i in range(5):
            print(f"from child thread: {i}")
            sleep(0.5)

    th = Thread(target=func, daemon=True)
    th.start()
    print("App stop")