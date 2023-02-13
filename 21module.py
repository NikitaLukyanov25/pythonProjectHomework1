# у обЬекта есть 2 характеристики
# 1) Атрибут
# 2) Поведение
# объект - попугай
# свойства : имя, возраст и тд
# попугай поет и танцует
# DRY
# класс - шаблон объекта

# class Parrot:
#     pass
#
# # Объект - экземпляр класса
# obj = Parrot()

# class Parrot:
#     species = 'Птица'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# # создаем экземпляр класса
# kesha = Parrot('Кеша', 10)
# cookie = Parrot('Куки', 15)
# # получаем доступ к атрибутам класса
# print(f'Кеша - {kesha.__class__.species}')
# print(f'Куки тоже - {cookie.__class__.species}')
# # получаем доступ к атрибутам экземпляра
# print(f'{kesha.name}-{kesha.age} летний попугай')
# print(f'{cookie.name}-{cookie.age} летний попугай')

# Методы ==функции == действие!
# class Parrot:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def sing(self, song):
#         return f'{self.name} поет {song}'
#     def dance(self):
#         return f'{self.name} танцует'
# kesha = Parrot('Кеша', 14)
# print(kesha.sing('wildways'))
# print(kesha.dance())

# Метод Init отвечает за инициализацию

#Наследование
# родительский класс
# class bird:
#     def __init__(self):
#         print("птица готова")
#     def whoisthis(self):
#         print('птица')
#     def swim(self):
#         print('плывет быстрее')
# #дочерний класс
# class penguin(bird):
#     def __init__(self):
#         super().__init__()
#         print('пингвин готов')
#     def whoisthis(self):
#         print('пингвин')
#     def run(self):
#         print('бежит быстрее')
# peggy = penguin()
# peggy.whoisthis()
# peggy.swim()
# peggy.run()


#инкапсуляция
# _ , __
# class computer:
#    def __init__(self):
#        self.__maxprice = 250
#    def sell(self):
#         print(f'цена продажи {self.__maxprice}')
#    def setmaxprice(self, price):
#         self.__maxprice = price
# c = computer()
# c.sell()
# # изменение цены
# c.__maxprice = 1000
# c.sell()
# # исп функцию изменения цены
# c.setmaxprice(1100)
# c.sell()

# полиморфизм
# # позволяет исп функцию для разных форм(типы данных)
#
# class Parrot:
#     def fly(self):
#         print('попугай умеет летать')
#     def swim(self):
#         print('попугай не умеет плавать')
#
# class penguin:
#     def fly(self):
#         print('пингвин не умеет летать')
#     def swim(self):
#         print('пингвин умеет плавать')
# def flyingtest(bird):
#     bird.fly()
# kesha = Parrot()
# peggy = penguin()
# # передача объектов в качестве аргументов
# flyingtest(kesha)
# flyingtest(peggy)

 # наследование
 # class baseclass:
 #     тело родительского
 # class docherniy:
 #     тело дочернего

# class polygon:
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]
#     def inputSides(self):
#         self.sides = [float(input('стороHа' + str(i+1)+ ':')) for i in range(self.n)]
#     def dispSides(self):
#         for i in range(self.n):
#             print('сторона', i + 1, ' - ', self.sides[i])
# class Triangle(polygon):
#     def __init__(self):
#         polygon.__init__(self, 3)
#           super().__init__(3)
#     def findArea(self):
#         a, b, c = self.sides
#         s = (a+b+c)/2
#         area = (s*(s-a)*(s-b)*(s-c)**0.5)
#         print('площадь треугольника', area)
# t = Triangle()
# t.inputSides()
# t.dispSides()
# t.findArea()

# Isinstance() - возвращает тру если объект является частью род класса

# Множественное наследование
# class Base1:
#   pass
# class Base2:
#   pass
# clasa multi(base1, base2):
#   pass

# class Event:
#     def __init__(self, timestamp, event_type, session_id):
#         self.timestamp = timestamp
#         self.type = event_type
#         self.session_id = session_id
# events = [
#     {
#      "timestamp": 1554583508000,
#      "type": "itemViewEvent",
#      "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#      "timestamp": 1555296337000,
#      "type": "itemViewEvent",
#      "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#      "timestamp": 1549461608000,
#      "type": "itemBuyEvent",
#      "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
# ]
#
# for event in events:
#     event_obj = Event(timestamp=event.get('timestamp'),
#         event_type = event.get('type'),
#         session_id = event.get('session_id'))
#     print(event_obj.timestamp)




