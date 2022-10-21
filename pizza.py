from enum import Enum


class PizzaSize(Enum):
    small: int = 120
    medium: int = 200
    large: int = 280

    def __str__(self) -> str:
        return self.name

    @property
    def price(self):
        return self.value


class Pizza:
    """A pizza with a size and optional toppings."""

    def __init__(self, size):
        self.size: PizzaSize = size
        self.toppings = []

    def get_price(self):
        """Price of pizza depends on size and number of toppings."""
        price = self.size.price + 20*len(self.toppings)
        return price
    
    def add_topping(self, topping):
        """Add a topping to the pizza"""
        if topping not in self.toppings:
            self.toppings.append(topping)

    def __str__(self) -> str:
        # create printable description of the pizza such as
        # "small pizza with muschroom" or "small plain pizza"
        description = str(self.size)
        if self.toppings:
            description += " pizza with "+ ", ".join(self.toppings)
        else:
            description += " plain cheeze pizza"
        return description