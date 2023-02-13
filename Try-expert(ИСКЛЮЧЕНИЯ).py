# 1)Исключения — это такие особенные классы, которые как и любые
# классы можно наследовать. Если вы хотите ловить несколько исключений,
# то сначала ловите потомков, а потом родителей, чтобы ничего не упустить.
# 2)Чтобы создать собственный класс, нужно просто написать пустой класс и наследовать
# его от класса Exception, этого будет достаточно.
# 3)Не обязательно отлавливать сам класс, при необходимости можно отлавливать
# его родителя, это тоже будет работать, но вы можете упустить важную информацию.

# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#   	+-- StopIteration
#   	+-- StopAsyncIteration
#   	+-- ArithmeticError
#   	|	FloatingPointError
#   	|	OverflowError
#   	|	ZeroDivisionError
#   	+-- AssertionError
#   	+-- AttributeError
#   	+-- BufferError
#   	+-- EOFError
#   	+-- ImportError
#   	|	+-- ModuleNotFoundError
#   	+-- LookupError
#   	|	+-- IndexError
#   	|	+-- KeyError
#   	+-- MemoryError
#   	+-- NameError
#   	|	+-- UnboundLocalError
#   	+-- OSError
#   	|	+-- BlockingIOError
#   	|	+-- ChildProcessError
#   	|	+-- ConnectionError
#   	|	|	+-- BrokenPipeError
#   	|	|	+-- ConnectionAbortedError
#   	|	|	+-- ConnectionRefusedError
#   	|	|	+-- ConnectionResetError
#   	|	+-- FileExistsError
#   	|	+-- FileNotFoundError
#   	|	+-- InterruptedError
#   	|	+-- IsADirectoryError
#   	|	+-- NotADirectoryError
#   	|	+-- PermissionError
#   	|	+-- ProcessLookupError
#   	|	+-- TimeoutError
#   	+-- ReferenceError
#   	+-- RuntimeError
#   	|	+-- NotImplementedError
#   	|	+-- RecursionError
#   	+-- SyntaxError
#   	|	+-- IndentationError
#   	|     	+-- TabError
#   	+-- SystemError
#   	+-- TypeError
#   	+-- ValueError
#   	|	+-- UnicodeError
#   	|     	+-- UnicodeDecodeError
#   	|     	+-- UnicodeEncodeError
#   	|     	+-- UnicodeTranslateError
#   	+-- Warning
#        	+-- DeprecationWarning
#        	+-- PendingDeprecationWarning
#        	+-- RuntimeWarning
#        	+-- SyntaxWarning
#        	+-- UserWarning
#        	+-- FutureWarning
#        	+-- ImportWarning
#        	+-- UnicodeWarning
#        	+-- BytesWarning
#        	# +-- ResourceWarning

#  СТАНДАРТНЫЙ ШАБЛОН ПОИСКА ИСКЛЮЧЕНИЙ
# class ParentException(Exception):  # создаём пустой класс – исключения потомка, наследуемся от exception
#     pass
# class ChildException(ParentException):  # создаём пустой класс – исключение наследника, наследуемся от ParentException
#     pass
# try:
#     raise ChildException("message")  # поднимаем исключение-наследник
# except ParentException as e:  # ловим его родителя
#     print(e)  # выводим информацию об исключении

# class ParentException(Exception):
#     def __init__(self, message,
#                  error):  # допишем к нашему пустому классу конструктор, который будет печатать дополнительно в консоль информацию об ошибке.
#         super().__init__(message)  # помним про вызов конструктора родительского класса
#         print(f"Errors: {error}")  # печатаем ошибку
# class ChildException(ParentException):  # создаём пустой класс – исключение наследника, наследуемся от ParentException
#     def __init__(self, message, error):
#         super().__init__(message, error)
# try:
#     raise ChildException("message", "error")  # поднимаем исключение-наследник, передаём дополнительный аргумент
# except ParentException as e:
#     print(e)

# class NonPositiveDigitException(ValueError):
#     pass
#
#
# class Square:
#     def __init__(self, a):
#         if a <= 0:
#             raise NonPositiveDigitException('Неправильно указанна сторона квадрата')