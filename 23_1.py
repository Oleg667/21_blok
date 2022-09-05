from decorators import do_twice

@do_twice
def test_twice_without_params():
    print("Этот вызов без параметров")


@do_twice
def test_twice_2_params(str1='1', str2='2'):
    print("В этой функции 2 параметра - {0} и {1}".format(str1, str2))

@do_twice
def test_twice(str='single'):
    print("Этот вызов возвращает строку {0}".format(str))

test_twice_without_params()
test_twice_2_params("1", "2")
test_twice("single")