from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass


class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total_price = 0
        self.observers = []

    def add_item(self, item):
        self.items.append(item)
        self.total_price += item.price
        self.notify_observers()

    def remove_item(self, item):
        self.items.remove(item)
        self.total_price -= item.price
        self.notify_observers()

    def attach(self, observer):
        self.observers.append(observer)
        for items in observer:
            self.add_item(items)

    def detach(self, observer):
        self.observers.remove(observer)
        for items in observer:
            self.remove_item(items)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self)

    def get_total_price(self):
        self.total_price - self.calculate_discount()
        self.notify_observers()

    def calculate_discount(self):
        if self.total_price > 100:
            return self.total_price * 0.1
        else:
            return 0


# class DiscountCalculator(Observer):
#     def update(self, subject):
#         total_price = subject.get_total_price()
#
#         print(f"Total price: {total_price}")


