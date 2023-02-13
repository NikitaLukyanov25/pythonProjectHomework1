# def absolut(num):
#     if num >= 0:
#         return num
#     else:
#         return -num
# print(absolut(5))
# print(absolut(-32))


# def my_func():
#     x=10
#     print('value in func', x)
# x=20
# my_func()
# print('value out func', x)


#Аргументы функций
# def greet(name,age):
#     print('hello ' + name + '.Welcome in my home!' + 'IT`s me ' + age + ' year.')
# greet('Nick', '27')


# def gret(*names):
#     for name in names:
#         print('hello', name)
# gret('Nick', 'Mark')


# def adder(*nums):
#     sum = 0
#     for n in nums:
#         sum += n
#     print('sum =', sum)
# adder(3,5,6,7,8)

# x = "глобальная"
# def foo():
#   print('x in func', x)
# foo()
# print('x out func', x)

# x = 'global variable'
# def foo():
#     global x
#     y = 'local var'
#     x = x * 2
#     print(x)
#     print(y)
# foo()

#nonlocal
# def outer():
#     x = ' Локальная переменная'
#     def inner():
#         nonlocal x
#         x = "нелокальная переменная"
#         print('вложенная фун', x)
#     inner()
#     print(':', x)
# outer()

#ЗАМЫКАНИЕ.
# def say():
#     greeting = 'Privet'
#     print(hex(id(greeting)))
#     def display():
#         print(hex(id(greeting)))
#     return display
# fn = say()
# fn()
# # print(fn.__closure__)


#Декораторы
# def net_price(price, tax):
#     return price * (1 + tax)
#
# def currency(fn):
#     def wrapper(*args, **kwargs):
#         result = fn(*args, **kwargs)
#         return f'${result}'
#     return wrapper
# net_price = currency(net_price)
# print(net_price(100, 0.05))

#isogram
# def is_isogram(string):
#     string = string.lower()
#     for letter in string:
#         if string.count(letter) > 1:
#             return False
#         return True
# print(is_isogram('abcdafc'))