# !!!!!!!
class Product:
    '''Добавить класс VIPProduct наследованный от Product, на него скидка не расспростаняется'''
    def __init__(self, name, price, discount=0.8):
        self.name = self.validate_name(name)
        self.price = self.validate_price(price)
        self.discount = discount

    @staticmethod
    def validate_name(name):
        if isinstance(name, str):
            return name
        raise Exception("Not a string")

    @staticmethod
    def validate_price(price):
        if isinstance(price, float) or isinstance(price, int):
            return price
        raise Exception("Not a number")


class VipProduct(Product):

    def __init__(self, name, price, discount=1):
        super().__init__(name=name, price=price, discount=discount)


class Client:

    def __init__(self, budget):
        self.budget = self.validate_budget(budget)

    @staticmethod
    def validate_budget(budget):
        if (isinstance(budget, float) or isinstance(budget, int)) and budget > 0:
            return budget
        raise Exception("Too small budget. Sorry")

    def count_product(self, prod):
        prods = self.budget / prod.price
        return int(prods)


class VIPClient(Client):
    def __init__(self, budget):
        super().__init__(budget)

    def count_product(self, prod):
        return int(super().count_product(prod) / prod.discount)


class SuperVIPClient(VIPClient):
    def __init__(self, budget):
        super().__init__(budget)

    def count_product(self, prod):
        return int(super().count_product(prod) / prod.discount)


our_prod = Product('bread', 10)

client1 = Client(100.1)
print(client1.count_product(our_prod))

client2 = VIPClient(1000.1)
print(client2.count_product(our_prod))

client3 = SuperVIPClient(10000.1)
print(client3.count_product(our_prod))


not_our_prod = VipProduct('WIPbread', 50)

print(client1.count_product(not_our_prod))
print(client2.count_product(not_our_prod))
print(client3.count_product(not_our_prod))
