# def say_hello(name):
#     return f"Hello {name}"
#
# def be_awesome(name):
#     return f"Yo {name}, together we are the awesomest!"
#
# def greet_bob(greeter_func):
#     return greeter_func("Bob")
#
# print(greet_bob(say_hello))
# print( greet_bob(be_awesome))

# def parent():
#     print("Printing from the parent() function")
#
#     def first_child():
# #         print("Printing from the first_child() function")
# #
# #     def second_child():
# #         print("Printing from the second_child() function")
# #
# #     second_child()
# #     first_child()
# # print(parent())
#
# <<<<<<< HEAD
# def my_decorator(func):
#     def wrapper():
#         print("Начало выполнения функции.")
#         func()
#         print("Конец выполнения функции.")
#
#     return wrapper
#
#
# #Эту функцию мы будем декорировать
# def my_first_decorator():
# 	print("Это мой первый декоратор!")
#
# my_first_decorator = my_decorator(my_first_decorator)
#
# my_first_decorator()

# def my_decorator(func):
#     def wrapper():
#         print("Начало выполнения функции.")
#         func()
#         print("Конец выполнения функции.")
#
#     return wrapper
#
#
# #Эту функцию мы будем декорировать
# def my_first_decorator():
# 	print("Это мой первый декоратор!")
#
# my_first_decorator = my_decorator(my_first_decorator)
#
# my_first_decorator()
from decorators import do_twice


@do_twice
def test_twice():
    print("Это вызов функции test_twice!")

# @do_twice
# def test_twice(str):
#     print("Этот вызов возвращает строку {0}".format(str))

