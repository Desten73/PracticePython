def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


test_function()
# inner_function() - ошибка, т.к. inner_function находится в другой области видимости
