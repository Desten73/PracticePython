class Product:
    def __init__(self, name, weight, category):
        self.__name = name
        self.__weight = weight
        self.__category = category

    def __str__(self):
        return f"{self.__name}, {self.__weight}, {self.__category}"

    def get_name(self):
        return self.__name


class Shop:
    __file_name = "products.txt"

    def get_products(self):
        file = open(self.__file_name, "r")
        res = file.read()
        file.close()
        return res

    def add(self, *products):
        textInFile = self.get_products()
        for product in products:
            if str(product) in textInFile:
                print(f"Продукт {product.get_name()} уже есть в магазине")
            else:
                file = open(self.__file_name, "a")
                file.write(str(product) + "\n")
                file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
