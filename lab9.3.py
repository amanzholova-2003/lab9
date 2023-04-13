from functools import reduce

my_list = [1, 2, 3, 4, 5]

# пример использования функции map
squared_list = list(map(lambda x: x ** 2, my_list))
print(squared_list)

# пример использования функции filter
even_list = list(filter(lambda x: x % 2 == 0, my_list))
print(even_list)

# пример использования функции reduce
product = reduce(lambda x, y: x * y, my_list)
print(product)
