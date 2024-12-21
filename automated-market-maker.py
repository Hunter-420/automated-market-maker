import sys


class InitialAssets:
    def __init__(self):
        self.assets = []

    def add_assets(self, name, base_quantity, face_value):
        self.assets.append(
                {
                    "name": name,
                    "base_quantity": base_quantity,
                    "face_value": face_value
                }
            )

    def get_all_assets(self):
        return self.assets

    def constant_value(self):
        value = 1
        for asset in self.assets:
            value *= asset["base_quantity"]
        return value


class LiquidityPool:
    def __init__(self):
        self.pool = []

    def add_pool(self, name, quantity):
        self.pool.append(
                {
                    "name": name,
                    "quantity": quantity
                }
            )

    def get_all_pool(self):
        return self.pool

    def find_pool(self, name):
        for fruit in self.pool:
            if fruit["name"] == name:
                return fruit
        return None

    def update_pool(self, name, quantity):
        for fruit in self.pool:
            if fruit["name"] == name:
                fruit["quantity"] = quantity


class FruitExchange(InitialAssets, LiquidityPool):
    def __init__(self):
        InitialAssets.__init__(self)
        LiquidityPool.__init__(self)

    def exchange(self, sell_fruit, buy_fruit, sell_quantity):
        sell_fruit_details = self.find_pool(sell_fruit)
        buy_fruit_details = self.find_pool(buy_fruit)

        if not sell_fruit_details:
            print(f"{sell_fruit} not found in liquidity pool \n")
            sys.exit(1)

        if not buy_fruit_details:
            print(f"{buy_fruit} not found in liquidity pool \n")
            sys.exit(1)

        update_pool = self.constant_value()/(sell_fruit_details["quantity"] + sell_quantity)
        exchanged_quantity = int(sell_fruit_details["quantity"] - update_pool)
        if exchanged_quantity < 0:
            print(f"sufficient {buy_fruit} quantity is not in liquidity pool decrease the quantity of {sell_fruit}")
            sys.exit(1)

        self.update_pool(buy_fruit, update_pool)
        self.update_pool(sell_fruit, sell_fruit_details["quantity"] + sell_quantity)
        return [sell_quantity, sell_fruit, exchanged_quantity, buy_fruit]


# creating an instance of FruitExchange
exchange = FruitExchange()

# adding to assits
exchange.add_assets("Orange", 50000, 1)
exchange.add_assets("Apple", 50000, 1)

# adding to a Liquidity Pool
exchange.add_pool("Orange", 50000)
exchange.add_pool("Apple", 50000)

# exchange apple with Orange
exchanged = exchange.exchange("Apple", "Orange", 50000000000)
print(f"exchange {exchanged[0]} {exchanged[1]} with {exchanged[2]} {exchanged[3]} \n")







