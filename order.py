class PersonalPurchase:
    def __init__(self, cost, item):
        self.cost = cost
        self.item = item


class Order:
    def __init__(self):
        self.advances = dict()
        self.orders = dict()
        self.credits = dict()
        self.debts = dict()

    def new_purchase(self, name: str, item: str, cost: float):
        if name in self.orders:
            self.orders[name].append(PersonalPurchase(cost, item))
        else:
            self.orders[name] = [PersonalPurchase(cost, item)]

    def new_advance(self, name: str, advance: float):
        self.advances[name] = advance

    def new_divided_purchase(self, people: list, item: str, total_cost: float):
        single_cost = round(total_cost / len(people), 2)
        for name in people:
            self.new_purchase(name, item, single_cost)

    def calc_debts(self):
        credits = dict()
        debts = dict()
        for name in set(list(self.advances.keys()) + list(self.orders.keys())):
            credits[name] = (self.advances[name] if name in self.advances else 0) \
                            - sum(order.cost for order in self.orders[name])
            if credits[name] < 0:
                debts[name] = -credits[name]
                del credits[name]

        self.credits = credits
        self.debts = debts
        print("Credits ")
        print(self.credits)
        print("\nDebts")
        print(self.debts)

    def calc_transfers(self):
        remaining_debts = self.debts
        remaining_credits = self.credits
        while list(remaining_debts.values()) != [0] * len(remaining_debts.keys()):
            max_creditore = max(remaining_credits, key=remaining_credits.get)
            max_debitore = max(remaining_debts, key=remaining_debts.get)
            resto = round(remaining_credits[max_creditore] - remaining_debts[max_debitore], 2)
            if resto < 0:
                print(max_creditore + " receivs " + str(remaining_credits[max_creditore]) + " from " + max_debitore)
                remaining_credits[max_creditore] = 0
                remaining_debts[max_debitore] = -resto
            else:
                print(max_creditore + " receives " + str(remaining_debts[max_debitore]) + " from " + max_debitore)
                remaining_credits[max_creditore] = resto
                remaining_debts[max_debitore] = 0
            print(remaining_debts)
            print(remaining_credits)
            print("\n")


order = Order()
# Report what every person has to pay for their personal purchase
order.new_purchase("John", "", 12.5)
order.new_purchase("Alice", "", 12.5)
order.new_purchase("Margaret", "", 12.5)

# Report a divided purchase, for example expedition costs or a divided item
order.new_divided_purchase(["John",
                         "Alice",
                         "Margaret"], "", 3.5)

# Report the advanced that someone placed
order.new_advance("John", 20.0)
order.new_advance("Margaret", 20.0)
order.new_advance("Alice", 5.0)

# Calc open debts
order.calc_debts()
# Calc how much one has to give to another
order.calc_transfers()
