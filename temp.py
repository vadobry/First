# Python3 программа для поиска средних значений
# все уровни в двоичном дереве.
# Импорт очереди
from queue import Queue
# Вспомогательный класс, который выделяет
# новый узел с заданными данными и
# Нет левого и правого указателей.
class newNode:
    def __init__(self, data):
        self.val = data
        self.left = self.right = None
# Функция для печати среднего значения
# Количество узлов на каждом уровне
def averageOfLevels(root):
    # Уровень прохождения уровня
    q = Queue()
    q.put(root)
    while (not q.empty()):
        # Вычислить сумму узлов и
        # количество узлов в текущем
        # уровень.
        Sum = 0
        count = 0
        temp = Queue()
        while (not q.empty()):
            n = q.queue[0]
            q.get()
            Sum += n.val
            count += 1
            if (n.left != None):
                temp.put(n.left)
            if (n.right != None):
                temp.put(n.right)
        q = temp
        print((Sum * 1.0 / count), end = " ")
# Код драйвера
if __name__ == '__main__':
    # Давайте построим двоичное дерево
    # № 4
    # / /
    # № 2 9
    # / / /
    # 3 5 7
    root = None
    root = newNode(4)
    root.left = newNode(2)
    root.right = newNode(9)
    root.left.left = newNode(3)
    root.left.right = newNode(8)
    root.right.right = newNode(7)
    averageOfLevels(root)
# Этот код предоставлен PranchalK