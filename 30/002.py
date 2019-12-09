class Product:

    def __init__(self, name, price, sale=20):
        self.name = self.validate_name(name)
        self._price = self.validate_price(price)
        self.sale = (100 - sale)/100


    @property
    def price(self):
        return self._price * self.sale

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


class Client:

    def __init__(self,  budget):
        self.budget = self.validate_budget(budget)


    def check_class(self):
        pass

    @staticmethod
    def validate_budget(budget):
        if (isinstance(budget, float) or isinstance(budget, int)) and budget > 0:
            return budget
        raise Exception("Too small budget. Sorry")

    def sales(self, product):

        return product.price


    def count_product(self, prod):
        prods = self.budget / self.sales(prod)
        return int(prods)



class VIPClient(Client):
    def __init__(self, budget):
        super().__init__(budget)


class SuperVIPClient(VIPClient):
    def __init__(self, budget):
        super().__init__(budget)



our_prod = Product('bread', 10, 15)

client1 = Client(100.1)
print(client1.count_product(our_prod))

client2 = VIPClient(1000.1)
print(client2.count_product(our_prod))

client3 = SuperVIPClient(10000.1)
print(client3.count_product(our_prod))
