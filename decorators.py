# def do_twice(func):
#     def wrapper(str):
#         func(str)
#         func(str)
#     return wrapper
def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper