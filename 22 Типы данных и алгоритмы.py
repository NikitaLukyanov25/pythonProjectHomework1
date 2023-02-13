# a = 'Hello world'
# print(a.lower().islower())
import math

# a = 2
# print(type(a))

# a = {'sg': 'qwe'} # dict

                 # АЛГОРИТМЫ!

# Евклидовый алгоритм
# def e_alg(a: int, b: int) ->int:
#     while a != 0 and b != 0:
#         if a<b:
#             b %= a
#         else:
#             a %= b
#     return a + b
# print(e_alg(30, 40))

# def bi_s(a: int, array: list) ->int:
#     left, right = 0, len(array)
#     while left < right:
#         middle = (left+right) //2
#         if array[middle] < a:
#             left = middle + 1
#         else:
#             right = middle
#     return left
# print(bi_s(7, [1,2,3,4,5,6,7,8,9,12,14,25]))


# Массив
# arr =[1,2,3,4,5,6,7,8,9,10]
# arr =[i for i in range(10)]
# arr.append(10)
# arr.extend((11,12,13))
# arr.pop(13)
# print(arr)

#
# Самый простой, самый эффективный алгоритм, к которому все стремятся,
# — это константный алгоритм.
#
# Константным, или постоянным по времени, называется алгоритм,
# который выполняет необходимое действие всегда за одинаковое
# количество времени (с точностью до небольшого множителя,
# вызванного техническими характеристиками вычислительной машины).
# -присваивание;
# -арифметические операции;
# -логические операции;
# -сравнение объектов;
# -некоторые другие действия, которые мы рассмотрим в ходе изучения модуля.

# Логарифмический алгоритм
# n = 10000
# print(n ** 2 /(n * math.log(n, 2)))

          #СТЕК
# def p(n):
#     if n == 10:
#         return
#     else:
#         p(n+1)
#         print(n)
# p(4)

# pars = {")": "(", "]": "["}
#
#
# def par_checker_mod(string):
#     stack = []
#
#     for s in string:
#         if s in "([":
#             stack.append(s)
#         elif s in ")]":
#             if len(stack) > 0 and stack[-1] == pars[s]:
#                 stack.pop()
#             else:
#                 return False
#     return len(stack) == 0

               #  ОЧЕРЕДЬ!!
# N_max = int(input("Определите размер очереди:"))
# queue = [0 for _ in range(N_max)] # инициализируем список с нулевыми элементами
# order = 0 # будем хранить сквозной номер задачи
# head = 0 # указатель на начало очереди
# tail = 0 # указатель на элемент следующий за концом очереди
# def is_empty(): # очередь пуста?
#     # да, если указатели совпадают и в них содержится ноль
#     return head == tail and queue[head] == 0
# def size(): # получаем размер очереди
#     if is_empty(): # если она пуста
#         return 0 # возвращаем ноль
#     elif head == tail: # иначе, если очередь не пуста, но указатели совпадают
#         return N_max # значит очередь заполнена
#     elif head > tail: # если хвост очереди сместился в начало списка
#         return N_max - head + tail
#     else: # или если хвост стоит правее начала
#         return tail - head
# def add():  # добавляем задачу в очередь
#     global tail, order
#     order += 1  # увеличиваем порядковый номер задачи
#     queue[tail] = order  # добавляем его в очередь
#     print("Задача №%d добавлена" % (queue[tail]))
#     # увеличиваем указатель на 1 по модулю максимального числа элементов
#     # для зацикливания очереди в списке
#     tail = (tail + 1) % N_max
# def show(): # выводим приоритетную задачу
#     print("Задача №%d в приоритете" % (queue[head]))
# def do(): # выполняем приоритетную задачу
#     global head
#     print("Задача №%d выполнена" % (queue[head]))
#     queue[head] = 0 # после выполнения зануляем элемент по указателю
#     head = (head + 1) % N_max # и циклично перемещаем указатель
# while True:
#     cmd = input("Введите команду:")
#     if cmd == "empty":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             print("В очереди есть задачи")
#     elif cmd == "size":
#         print("Количество задач в очереди:", size())
#     elif cmd == "add":
#         if size() != N_max:
#             add()
#         else:
#             print("Очередь переполнена")
#     elif cmd == "show":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             show()
#     elif cmd == "do":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             do()
#     elif cmd == "exit":
#         for _ in range(size()):
#             do()
#         print("Очередь пустая. Завершение работы")
#         break
#     else:
#         print("Введена неверная команда")
# def is_empty(): # очередь пуста?
#     # да, если указатели совпадают и в них содержится ноль
#     return head == tail and queue[head] == 0
# def size(): # получаем размер очереди
#     if is_empty(): # если она пуста
#         return 0 # возвращаем ноль
#     elif head == tail: # иначе, если очередь не пуста, но указатели совпадают
#         return N_max # значит очередь заполнена
#     elif head > tail: # если хвост очереди сместился в начало списка
#         return N_max - head + tail
#     else: # или если хвост стоит правее начала
#         return tail - head
# def add():
#     global tail, order
#     order += 1
#     queue[tail] = order
#     print('Задача №%d добавлен' % (queue[tail]))
#     tail = (tail + 1) % N_max
# def show():  # выводим приоритетную задачу
#     print("Задача №%d в приоритете" % (queue[head]))
# def do():
#     global head
#     print("Задача №%d выполнена" % (queue[head]))
#     queue[head] = 0
#     head = (head + 1) % N_max

# G = {"Адмиралтейская" :
#          {"Садовая" : 4},
#      "Садовая" :
#          {"Сенная площадь" : 3,
#           "Спасская" : 3,
#           "Адмиралтейская" : 4,
#           "Звенигородская" : 5},
#      "Сенная площадь" :
#          {"Садовая" : 3,
#           "Спасская" : 3},
#      "Спасская" :
#          {"Садовая" : 3,
#           "Сенная площадь" : 3,
#           "Достоевская" : 4},
#      "Звенигородская" :
#          {"Пушкинская" : 3,
#           "Садовая" : 5},
#      "Пушкинская" :
#          {"Звенигородская" : 3,
#           "Владимирская" : 4},
#      "Владимирская" :
#          {"Достоевская" : 3,
#           "Пушкинская" : 4},
#      "Достоевская" :
#          {"Владимирская" : 3,
#           "Спасская" : 4}}
# D = {k : 100 for k in G.keys()} # расстояния
# start_k = 'Адмиралтейская' # стартовая вершина
# D[start_k] = 0 # расстояние от неё до самой себя равно нулю
# U = {k : False for k in G.keys()} # флаги просмотра вершин
# P = {k : None for k in G.keys()}
# for _ in range(len(D)):
#     # выбираем среди непросмотренных наименьшее по расстоянию
#     min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])
#
#     for v in G[min_k].keys(): # проходимся по всем смежным вершинам
#         if D[v]>D[min_k]+G[min_k][v]:
#            D[v] = D[min_k]+G[min_k][v]
#            P[v] = min_k
#     U[min_k] = True # просмотренную вершину помечаем
# pointer = "Владимирская" # куда должны прийти
# while pointer is not None: # перемещаемся, пока не придём в стартовую точку
#     print(pointer)
#     pointer = P[pointer]

# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left_child = None
#         self.right_child = None
#
#     def insert_left(self, next_value):
#         if self.left_child is None:
#             self.left_child = BinaryTree(next_value)
#         else:
#             new_child = BinaryTree(next_value)
#             new_child.left_child = self.left_child
#             self.left_child = new_child
#         return self
#
#     def insert_right(self, next_value):
#         if self.right_child is None:
#             self.right_child = BinaryTree(next_value)
#         else:
#             new_child = BinaryTree(next_value)
#             new_child.right_child = self.right_child
#             self.right_child = new_child
#         return self
#
#     def in_order(self):
#         if self.left_child is not None:  # если левый потомок существует
#             self.left_child.in_order()  # рекурсивно вызываем функцию
#
#         print(self.value)  # процедура обработки
#
#         if self.right_child is not None:  # если правый потомок существует
#             self.right_child.in_order()  # рекурсивно вызываем функцию
#
#
# # A_node = BinaryTree('A').insert_left('B').insert_right('C')
# node_root = BinaryTree(2).insert_left(7).insert_right(5)
# node_7 = node_root.left_child.insert_left(2).insert_right(6)
# node_6 = node_7.right_child.insert_left(5).insert_right(11)
# node_5 = node_root.right_child.insert_right(9)
# node_9 = node_5.right_child.insert_left(4)
#
# node_root.in_order()


# def find(array, element):
#     for i, a in enumerate(array):
#         if a == element:
#             return i
#     return False
# def count(array, element):
#     count = 0
#     for a in array:
#         if a == element:
#              count += 1
#     return count
# array = list(map(int, input('List').split()))
# element = int(input('element'))
#
# print(find(array, element))
# print(count(array, element))

# Двоичный поиск
# def binary_search(array, element, left, right):
#     if left > right:  # если левая граница превысила правую,
#         return False  # значит элемент отсутствует
#
#     middle = (right + left) // 2  # находимо середину
#     if array[middle] == element:  # если элемент в середине,
#         return middle  # возвращаем этот индекс
#     elif element < array[middle]:  # если элемент меньше элемента в середине
#         # рекурсивно ищем в левой половине
#         return binary_search(array, element, left, middle - 1)
#     else:  # иначе в правой
#         return binary_search(array, element, middle + 1, right)
#
# import random  # модуль, с помощью которого перемешиваем массив
#
# # пусть имеем массив всего лишь из 9 элементов
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
#
# is_sort = False  # станет True, если отсортирован
# count = 0  # счетчик количества перестановок
#
# while not is_sort:  # пока не отсортирован
#     count += 1  # прибавляем 1 к счётчику
#
#     random.shuffle(array)  # перемешиваем массив
#
#     # проверяем, отсортирован ли
#     is_sort = True
#     for i in range(len(array) - 1):
#         if array[i] > array[i + 1]:
#             is_sort = False
#             break
#
# print(array)
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(count)
# # 290698

# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# count = 0
# for i in range(len(array)):  # проходим по всему массиву
#     idx_max = i  # сохраняем индекс предположительно минимального элемента
#     for j in range(i, len(array)):
#         count -= 1
#         if array[j] > array[idx_max]:
#             idx_max = j
#     if i != idx_max:  # если индекс не совпадает с минимальным, меняем
#         array[i], array[idx_max] = array[idx_max], array[i]
#
# print(count)
# print(array)

             # Пузырек
# array = [2, 3, 5, 4, 6, 1, 9, 8, 7]
# count = 0
# for i in range(len(array)):
#     count += 1
#     for j in range(len(array) - i - 1):
#         if array[j] > array[j + 1]:
#             array[j], array[j + 1] = array[j + 1], array[j]
#
# print(array)
# print(count)

          # СОРТИРОВКА ВСТАВКАМИ
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# count = 0
# for i in range(1,len(array)):
#     x=array[i]
#     idx = i
#     while idx >0 and array[idx-1]>x:
#         count += 1
#         array[idx] = array[idx-1]
#         idx-=1
# array[idx]=x
#
# print(array)
# print(count)


               # ВСТАВКА СЛИЯНИЯМИ
# def merge_sort(L):  # "разделяй"
#     if len(L) < 2:  # если кусок массива равен 2,
#         return L[:]  # выходим из рекурсии
#     else:
#         middle = len(L) // 2  # ищем середину
#         left = merge_sort(L[:middle])  # рекурсивно делим левую часть
#         right = merge_sort(L[middle:])  # и правую
#         return merge(left, right)  # выполняем слияние
#
#
# def merge(left, right):  # "властвуй"
#     result = []  # результирующий массив
#     i, j = 0, 0  # указатели на элементы
#
#     # пока указатели не вышли за границы
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     # добавляем хвосты
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#
#     return result

# БЫСТРАЯ СОРТИРОВКА
# def qsort(array, left, right):
#     middle = (left + right) // 2
#
#     p = array[middle]
#     i, j = left, right
#     while i <= j:
#         while array[i] < p:
#             i += 1
#         while array[j] > p:
#             j -= 1
#         if i <= j:
#             array[i], array[j] = array[j], array[i]
#             i += 1
#             j -= 1
#
#     if j > left:
#         qsort(array, left, j)
#     if right > i:
#         qsort(array, i, right)